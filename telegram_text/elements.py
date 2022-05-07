from typing import Callable

from .bases import Element, PlainText


class Link(Element):
    def __init__(self, text: str, url: str, style: Callable[[str], Element] = PlainText):
        self.text = text
        self.url = url
        self.style = style

    def to_plain_text(self) -> str:
        return self.style(f"{self.text} {self.url}").to_plain_text()

    def to_markdown(self) -> str:
        return self.style(f"[{self.text}]({self.url})").to_markdown()

    def to_html(self) -> str:
        return self.style(f'<a href="{self.url}">{self.text}</a>').to_html()


class InlineUser(Link):
    def __init__(self, text: str, user_id: int, style: Callable[[str], Element] = PlainText):
        url = f"tg://user?id={user_id}"
        super().__init__(text=text, url=url, style=style)


class Hashtag(Element):
    def __init__(self, text: str, style: Callable[[str], Element] = PlainText):
        self.text = style('#' + text.lstrip('#'))

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return self.text.to_markdown()

    def to_html(self) -> str:
        return self.text.to_html()
