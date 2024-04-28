"""Package defining all the IMAP parsing and response classes."""

from __future__ import annotations

import re
from abc import abstractmethod, ABCMeta
from collections.abc import Sequence
from typing import Any, TypeVar, Generic, TypeAlias, Protocol

from .exceptions import NotParseable, UnexpectedType
from .state import ParsingState
from ..bytes import Writeable

__all__ = ['ParsedT', 'AnyParseable', 'ParseableT', 'ParseableTyepT_co',
           'AnyParseableType', 'Params', 'Parseable', 'ExpectedParseable',
           'Space', 'EndLine']

#: Type variable used for specifying the data parsed by a :class:`Parseable`
#: sub-class.
ParsedT = TypeVar('ParsedT')

#: Type alias for an unspecified parseable object.
AnyParseable: TypeAlias = 'Parseable[Any]'

#: Type variable used for parseable objects.
ParseableT = TypeVar('ParseableT', bound='AnyParseable')

#: Covariant type variable used for parseable classes.
ParseableTypeT_co = TypeVar('ParseableTypeT_co', bound='AnyParseable',
                            covariant=True)

#: Type alias for an unspecified parseable type.
AnyParseableType: TypeAlias = 'ParseableType[Any]'


class ParseableType(Protocol[ParseableTypeT_co]):
    """A parseable type has a :meth:`.parse` method for reading something from
    the given buffer. This is usually, but not always, a :func:`type` where the
    :meth:`.parse` method is a class method that returns an instance of the
    type.

    Note:
        Until mypy supports using abstract classes when a ``type[...]`` is
        expected (discussed
        `here <https://github.com/python/mypy/issues/4717>`_), this is needed
        as a stopgap.

    """

    def parse(self, buf: memoryview, params: Params) \
            -> tuple[ParseableTypeT_co, memoryview]:
        """Parses something from the beginning of the buffer. The parsed object
        is returned as well as the remaining data in the buffer.

        Args:
            buf: The bytes containing the data to be parsed.
            params: The parameters used by some parseable types.

        Raises:
            :exc:`~pymap.parsing.exceptions.NotParseable`

        """
        ...


class Params:
    """Parameters used and passed around among the :meth:`~Parseable.parse`
    methods.

    Args:
        state: The mutable parsing state.
        expected: The types that are expected to be parsed..
        list_limit: The maximum number of items in a parsed list.
        command_name: The name of the command currently being parsed, if any.
        uid: The next parsed command came after a ``UID`` command.
        charset: Strings should be decoded using this character set.
        tag: The next parsed command uses this tag bytestring.
        max_append_len: The maximum allowed length of the message body to an
            ``APPEND`` command.
        allow_continuations: Allow literal strings that require continuation
            data.

    """

    __slots__ = ['state', 'expected', 'list_limit', 'command_name', 'uid',
                 'charset', 'tag', 'max_append_len', 'allow_continuations']

    def __init__(self, state: ParsingState | None = None, *,
                 expected: Sequence[AnyParseableType] | None = None,
                 list_limit: int | None = None,
                 command_name: bytes | None = None,
                 uid: bool = False,
                 charset: str | None = None,
                 tag: bytes | None = None,
                 max_append_len: int | None = None,
                 allow_continuations: bool = True) -> None:
        super().__init__()
        self.state = state or ParsingState()
        self.expected = expected or []
        self.list_limit = list_limit
        self.command_name = command_name
        self.uid = uid
        self.charset = charset
        self.tag = tag or b'*'
        self.max_append_len = max_append_len
        self.allow_continuations = allow_continuations

    def _set_if_none(self, kwargs: dict[str, Any],
                     attr: str, value: Any) -> None:
        if value is not None:
            kwargs[attr] = value
        else:
            kwargs[attr] = getattr(self, attr)

    def copy(self, state: ParsingState | None = None, *,
             expected: Sequence[AnyParseableType] | None = None,
             list_limit: int | None = None,
             command_name: bytes | None = None,
             uid: bool | None = None,
             charset: str | None = None,
             tag: bytes | None = None,
             max_append_len: int | None = None,
             allow_continuations: bool | None = None) -> Params:
        """Copy the parameters, possibly replacing a subset."""
        kwargs: dict[str, Any] = {}
        self._set_if_none(kwargs, 'state', state)
        self._set_if_none(kwargs, 'expected', expected)
        self._set_if_none(kwargs, 'list_limit', list_limit)
        self._set_if_none(kwargs, 'command_name', command_name)
        self._set_if_none(kwargs, 'uid', uid)
        self._set_if_none(kwargs, 'charset', charset)
        self._set_if_none(kwargs, 'tag', tag)
        self._set_if_none(kwargs, 'max_append_len', max_append_len)
        self._set_if_none(kwargs, 'allow_continuations', allow_continuations)
        return Params(**kwargs)


class Parseable(Generic[ParsedT], Writeable, metaclass=ABCMeta):
    """Represents a parseable data object from an IMAP stream. The sub-classes
    implement the different data formats.

    This base class will be inherited by all necessary entries in the IMAP
    formal syntax section.

    """

    _whitespace_pattern = re.compile(br' +')
    _atom_pattern = re.compile(
        br'[\x21\x23\x24\x26\x27\x2B-\x5B\x5E-\x7A\x7C\x7E]+')

    __slots__: list[str] = []

    @property
    @abstractmethod
    def value(self) -> ParsedT:
        """The primary value associated with the parsed data."""
        ...

    @classmethod
    def _whitespace_length(cls, buf: memoryview, start: int = 0) -> int:
        match = cls._whitespace_pattern.match(buf, start)
        if match:
            return match.end(0) - start
        return 0

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, (bytes, memoryview)):
            return bytes(self) == other
        return NotImplemented

    @classmethod
    @abstractmethod
    def parse(cls: type[Parseable[ParsedT]], buf: memoryview, params: Params) \
            -> tuple[Parseable[ParsedT], memoryview]:
        """Implemented by sub-classes to define how to parse the given buffer.

        Args:
            buf: The bytes containing the data to be parsed.
            params: The parameters used by some parseable types.

        """
        ...


class ExpectedParseable(Parseable[None], metaclass=ABCMeta):
    """Non-instantiable class, used to parse a buffer from a list of
    expected types.

    """

    __slots__: list[str] = []

    @classmethod
    def parse(cls, buf: memoryview, params: Params) \
            -> tuple[AnyParseable, memoryview]:
        """Parses the given buffer by attempting to parse the list of
        :attr:`~Params.expected` types until one of them succeeds,
        then returns the parsed object.

        Args:
            buf: The bytes containing the data to be parsed.
            params: The parameters used by some parseable types.

        """
        for data_type in params.expected:
            try:
                return data_type.parse(buf, params)
            except NotParseable:
                pass
        raise UnexpectedType(buf)


class Space(Parseable[int]):
    """Represents at least one space character.

    Args:
        length: The number of spaces parsed.

    """

    __slots__ = ['length']

    def __init__(self, length: int) -> None:
        super().__init__()
        self.length = length

    @property
    def value(self) -> int:
        """The number of spaces parsed."""
        return self.length

    @classmethod
    def parse(cls, buf: memoryview, params: Params) \
            -> tuple[Space, memoryview]:
        ret = cls._whitespace_length(buf)
        if not ret:
            raise NotParseable(buf)
        return cls(ret), buf[ret:]

    def __bytes__(self) -> bytes:
        return b' ' * self.length


class EndLine(Parseable[bytes]):
    """Represents the end of a parsed line. This will only parse if the buffer
    has zero or more space characters followed by a new-line sequence.

    Args:
        preceding_spaces: The number of space characteres before the newline.
        carriage_return: Whether the newline included a carriage return.

    Attributes:
        preceding_spaces: The number of space characteres before the newline.
        carriage_return: Whether the newline included a carriage return.

    """

    _pattern = re.compile(br' *(\r?)\n')

    __slots__ = ['preceding_spaces', 'carriage_return']

    def __init__(self, preceding_spaces: int = 0,
                 carriage_return: bool = True) -> None:
        super().__init__()
        self.preceding_spaces = preceding_spaces
        self.carriage_return = carriage_return

    @property
    def value(self) -> bytes:
        """The endline bytestring."""
        return b'\r\n' if self.carriage_return else b'\n'

    @classmethod
    def parse(cls, buf: memoryview, params: Params) \
            -> tuple[EndLine, memoryview]:
        match = cls._pattern.match(buf)
        if not match:
            raise NotParseable(buf)
        preceding_spaces = match.start(1)
        carriage_return = bool(match.group(1))
        return cls(preceding_spaces, carriage_return), buf[match.end(0):]

    def __bytes__(self) -> bytes:
        return b' ' * self.preceding_spaces + self.value
