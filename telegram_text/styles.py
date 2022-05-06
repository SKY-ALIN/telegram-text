from abc import ABC
from typing import Union

from .elements import AbstractElement


class PlainText(AbstractElement):
    def __init__(self, text: Union[str, AbstractElement]):
        if isinstance(text, AbstractElement):
            text = text.to_plain_text()
        self.text: str = text

    def to_plain_text(self) -> str:
        return self.text

    def to_markdown(self) -> str:
        return self.text

    def to_html(self) -> str:
        return self.text

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.text}>"


class Style(AbstractElement, ABC):
    MARKDOWN_SYMBOL: str = NotImplemented
    HTML_TAG: str = NotImplemented

    def __init__(self, text: Union[str, AbstractElement]):
        if isinstance(text, str):
            text = PlainText(text)
        self.text: AbstractElement = text

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return f"{self.MARKDOWN_SYMBOL}{self.text.to_markdown()}{self.MARKDOWN_SYMBOL}"

    def to_html(self) -> str:
        return f"<{self.HTML_TAG}>{self.text.to_html()}</{self.HTML_TAG}>"

    def __str__(self) -> str:
        return self.to_markdown()

    def __repr__(self) -> str:
        text = str(self.text) if isinstance(self.text, PlainText) else repr(self.text)
        return f"<{self.__class__.__name__}: {text}>"


class Bold(Style):
    MARKDOWN_SYMBOL = '*'
    HTML_TAG = 'b'


class Italic(Style):
    MARKDOWN_SYMBOL = '_'
    HTML_TAG = 'i'


class Underline(Style):
    MARKDOWN_SYMBOL = '__'
    HTML_TAG = 'u'


class Strikethrough(Style):
    pass
