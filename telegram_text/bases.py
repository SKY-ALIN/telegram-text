from typing import Union

from abc import ABC, abstractmethod

NEW_LINE = '\n'  #: New line character constant.
SPACE = ' '  #: Space character constant.


class AbstractElement(ABC):
    """The interface every component implements."""

    @abstractmethod
    def __add__(self, other: Union[str, "Element"]) -> "Chain":
        """Return a new :class:`Chain` object when sum
        :code:`<Element object> + <Element object>`. You can also use it with
        :obj:`str` object, then this method will wrap a :obj:`str` with
        :class:`PlainText` object.
        """
        raise NotImplementedError

    @abstractmethod
    def to_plain_text(self) -> str:
        """Format the element to plain text without escaping, tags or special
        characters.
        """
        raise NotImplementedError

    @abstractmethod
    def to_markdown(self) -> str:
        """Format the element to Markdown/MarkdownV2 format according to
        Telegram specification with escaping if necessary.
        """
        raise NotImplementedError

    @abstractmethod
    def to_html(self) -> str:
        """Format the element to html according to Telegram specification."""
        raise NotImplementedError


class Element(AbstractElement, ABC):
    """Base class every component must inherit."""

    def __add__(self, other: Union[str, "Element"]) -> "Chain":
        if isinstance(other, str):
            other = PlainText(other)
        return Chain(self, other)

    def __radd__(self, other: str) -> "Chain":
        return PlainText(other).__add__(self)

    def __eq__(self, other: object) -> bool:
        """Equality function to write
        :code:`<Element object> == <Element object>`.
        """
        if not isinstance(other, Element):
            return NotImplemented
        return type(self) is type(other) and self.to_plain_text() == other.to_plain_text()

    def __str__(self) -> str:
        """Call :meth:`.to_markdown` function."""
        return self.to_markdown()


class Text(Element):
    """Basic text component. We don't recommend you use this outside the code
    of this module because this class doesn't include escaping logic, it means
    Telegram API may reject you.
    """

    def __init__(self, text: Union[str, Element]):
        if isinstance(text, Element):
            text = text.to_plain_text()
        self.text: str = text

    def to_plain_text(self) -> str:
        return self.text

    def to_markdown(self) -> str:
        """Return original text without escaping."""
        return self.text

    def to_html(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: '{self.text}'>"


class PlainText(Text):
    """Basic text element you can safely use. This element implements escaping
    logic.
    """

    escaping_chars = ('_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!')
    """Tuple of character that will be escaped according to Telegram specification."""

    def _escape(self, text: str) -> str:
        escaping_prefix = '\\'
        mapping = str.maketrans({char: escaping_prefix + char for char in self.escaping_chars})
        return "".join(char.translate(mapping) for char in text)

    def to_markdown(self) -> str:
        """Format the element to Markdown/MarkdownV2 format according to
        Telegram specification with escaping if necessary.
        """
        return self._escape(self.text)


class Chain(Element):
    """Combination between a few elements.

    Args:
        elements (Tuple[Element]): Any objects with :class:`AbstractElement` interface.
        sep (str): The separator between elements. :const:`SPACE` by default.
    """

    def __init__(self, *elements: Element, sep: str = SPACE):
        self.elements = elements
        self.sep = sep

    def __add__(self, other: Union[str, Element]) -> "Chain":
        if isinstance(other, str):
            other = PlainText(other)

        if self.sep == SPACE:  # Optimization for default separator
            return Chain(*self.elements, other)
        return Chain(self, other)

    def __contains__(self, item: Element) -> bool:
        """Magic method to write :code:`if <Element object> in <Chain object>`."""
        return item in self.elements

    def to_plain_text(self) -> str:
        return self.sep.join(element.to_plain_text() for element in self.elements)

    def to_markdown(self) -> str:
        return self.sep.join(element.to_markdown() for element in self.elements)

    def to_html(self) -> str:
        return self.sep.join(element.to_html() for element in self.elements)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}: "
            f"{' + '.join(repr(element) for element in self.elements)}, "
            f"sep='{self.sep}'>"
        )
