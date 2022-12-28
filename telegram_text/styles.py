from typing import Type, Union

from abc import ABC

from .bases import Element, PlainText, Text


class Style(Element, ABC):
    """Class that inherits each style. it isolates a part of logic how to
    render styles.

    Args:
        text (Union[str, telegram_text.bases.Element]):
            Text or Element to which the style will be applied.
    """

    markdown_symbol: str
    html_tag: str
    html_class: Union[str, None] = None
    base_style_fabric: Union[Type[Text], Type['Style']] = PlainText

    def __init__(self, text: Union[str, Element]):
        if isinstance(text, str):
            text = self.base_style_fabric(text)
        if isinstance(text, Style) and self.__class__ is text.__class__:
            text = text.text
        self.text: Element = text

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return f"{self.markdown_symbol}{self.text.to_markdown()}{self.markdown_symbol}"

    def to_html(self) -> str:
        class_str = f' class="{self.html_class}"' if self.html_class else ''
        return f'<{self.html_tag}{class_str}>{self.text.to_html()}</{self.html_tag}>'

    def __repr__(self) -> str:
        text = f"'{self.text}'" if isinstance(self.text, self.base_style_fabric) else repr(self.text)
        return f"<{self.__class__.__name__}: {text}>"


class Bold(Style):
    """Bold text. Example: **bold text**."""

    markdown_symbol = '*'
    html_tag = 'b'


class Italic(Style):
    """Italic text. Example: *italic text*."""

    markdown_symbol = '_'
    html_tag = 'i'


class Underline(Style):
    """Underline text. Example: :underline:`underline text`."""

    markdown_symbol = '__'
    html_tag = 'u'


class Strikethrough(Style):
    """Strikethrough text. Example: :strike:`strikethrough text`."""

    markdown_symbol = '~'
    html_tag = 's'


class Spoiler(Style):
    """Spoiler text. We can't provide an example because it's a very specific
    for Telegram messenger formatting.
    """

    markdown_symbol = '||'
    html_tag = 'span'
    html_class = 'tg-spoiler'


class InlineCode(Style):
    """Inline code text. Example: :code:`inline code`."""

    markdown_symbol = '`'
    html_tag = 'code'
    base_style_fabric = Text


class Code(Style):
    """Code block for many lines of text. Telegram doesn't support frontend
    language-specific highlights, but according to documentation, it provides
    an opportunity to specify a language. Perhaps, the Telegram team will add
    support for this in the future.

    Args:
        text (str):
            Text of code block.
        language (Optional[str]):
            Leave it empty if you don't want to specify a language.
    """

    markdown_symbol = '```'
    html_tag = 'code'
    base_style_fabric = Text

    def __init__(self, text: str, language: Union[str, None] = None):
        super().__init__(text)
        self.language: str = language or ''
        self.html_class: Union[str, None] = f'language-{language}' if language else None

    def to_markdown(self) -> str:
        return f"{self.markdown_symbol}{self.language}\n{self.text.to_markdown()}{self.markdown_symbol}"

    def to_html(self) -> str:
        # if lang isn't specified, we don't use <code> tag according to Telegram docs
        if self.html_class:
            return f'<pre>{super().to_html()}</pre>'
        return f'<pre>{self.text.to_html()}</pre>'
