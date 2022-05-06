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
