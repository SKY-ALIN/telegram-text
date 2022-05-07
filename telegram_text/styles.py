from abc import ABC
from typing import Union, Optional

from .bases import Element, PlainText


class Style(Element, ABC):
    markdown_symbol: str = NotImplemented
    html_tag: str = NotImplemented
    html_class: str = None

    def __init__(self, text: Union[str, Element]):
        if isinstance(text, str):
            text = PlainText(text)
        if self.__class__ is text.__class__:
            text = text.text
        self.text: Element = text

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return f"{self.markdown_symbol}{self.text.to_markdown()}{self.markdown_symbol}"

    def to_html(self) -> str:
        class_str = f' class="{self.html_class}"' if self.html_class else ''
        return f'<{self.html_tag}{class_str}>{self.text.to_html()}</{self.html_tag}>'

    def __str__(self) -> str:
        return self.to_markdown()

    def __repr__(self) -> str:
        text = str(self.text) if isinstance(self.text, PlainText) else repr(self.text)
        return f"<{self.__class__.__name__}: {text}>"


class Bold(Style):
    markdown_symbol = '*'
    html_tag = 'b'


class Italic(Style):
    markdown_symbol = '_'
    html_tag = 'i'


class Underline(Style):
    markdown_symbol = '__'
    html_tag = 'u'


class Strikethrough(Style):
    markdown_symbol = '~'
    html_tag = 's'


class Spoiler(Style):
    markdown_symbol = '||'
    html_tag = 'span'
    html_class = 'tg-spoiler'


class InlineCode(Style):
    markdown_symbol = '`'
    html_tag = 'code'


class Code(Style):
    markdown_symbol = '```'

    def __init__(self, text: str, language: str = None):
        super().__init__(text)
        self.language: str = language or ''
        self.html_class: Optional[str] = f'language-{language}' if language else None

    def to_markdown(self) -> str:
        return f"{self.markdown_symbol}{self.language}\n{self.text.to_markdown()}\n{self.markdown_symbol}"

    def to_html(self) -> str:
        class_str = f' class="{self.html_class}"' if self.html_class else ''
        # if lang isn't specified, we don't use <code> tag according to Telegram docs
        if class_str:
            return f'<pre><code{class_str}>{self.text.to_html()}</code></pre>'
        return f'<pre>{self.text.to_html()}</pre>'
