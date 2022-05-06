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
    def __init__(self, text: Union[str, AbstractElement]):
        if isinstance(text, str):
            text = PlainText(text)
        self.text: AbstractElement = text

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def __str__(self) -> str:
        return self.to_markdown()

    def __repr__(self) -> str:
        text = str(self.text) if isinstance(self.text, PlainText) else repr(self.text)
        return f"<{self.__class__.__name__}: {text}>"


class Bold(Style):
    def to_markdown(self) -> str:
        return f"*{self.text.to_markdown()}*"

    def to_html(self) -> str:
        return f"<b>{self.text.to_html()}</b>"


class Italic(Style):
    def to_markdown(self) -> str:
        return f"_{self.text.to_markdown()}_"

    def to_html(self) -> str:
        return f"<i>{self.text.to_html()}</i>"


class Underline(Style):
    pass
