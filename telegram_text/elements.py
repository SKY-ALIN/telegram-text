from typing import Callable

from .bases import Element, PlainText


class Hashtag(Element):
    def __init__(self, text: str, style_fabric: Callable[[str], Element] = PlainText):
        self.text = style_fabric('#' + text.lstrip('#'))

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return self.text.to_markdown()

    def to_html(self) -> str:
        return self.text.to_html()
