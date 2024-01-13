"""All classes in this file provide similar signatures.

They all have :code:`text: str` and
:code:`style: Callable[[Union[str, Element]], Element])` arguments.

:code:`style` is a factory that will be applied to the element.
"""

from typing import Callable, Union

from .bases import Element, PlainText, Text


class Link(Element):
    """Inline link element.

    Args:
        text (str):
            Text of link.
        url (str):
            Web address on the internet.
        style (Callable[[Union[str, Element]], Element]):
            Style factory which will be applied to the element.
            :class:`telegram_text.bases.PlainText` by default.
    """

    def __init__(self, text: str, url: str, style: Callable[[Union[str, Element]], Element] = PlainText):
        self.text: Element = style(text)
        self.url = url

    def to_plain_text(self) -> str:
        return f"{self.text.to_plain_text()} ({self.url})"

    def to_markdown(self) -> str:
        return f"[{self.text.to_markdown()}]({self.url})"

    def to_html(self) -> str:
        return f'<a href="{self.url}">{self.text.to_html()}</a>'


class InlineUser(Link):
    """Inline link to user with specific for Telegram url
    (:code:`tg://user?id={}`).

    Args:
        text (str):
            Text of link.
        user_id (int):
            Identifier of user.
        style (Callable[[Union[str, Element]], Element]):
            Style factory which will be applied to the element.
            :class:`telegram_text.bases.PlainText` by default.
    """

    def __init__(self, text: str, user_id: int, style: Callable[[Union[str, Element]], Element] = Text):
        url = f"tg://user?id={user_id}"
        super().__init__(text=text, url=url, style=style)


class _Reference(Element):
    def __init__(self, text: str, style: Callable[[str], Element] = PlainText):
        self.text = style(text)

    def to_plain_text(self) -> str:
        return self.text.to_plain_text()

    def to_markdown(self) -> str:
        return self.text.to_markdown()

    def to_html(self) -> str:
        return self.text.to_html()


class User(_Reference):
    """Link to user by nickname.

    Args:
        text (str):
            Nickname of user.
        style (Callable[[Union[str, Element]], Element]):
            Style factory which will be applied to the element.
            :class:`telegram_text.bases.PlainText` by default.
    """

    def __init__(self, text: str, style: Callable[[Union[str, Element]], Element] = PlainText):
        text = '@' + text.lstrip('@')
        super().__init__(text, style=style)


class Hashtag(_Reference):
    """Hashtag link element.

    Args:
        text (str):
            Hashtag name.
        style (Callable[[Union[str, Element]], Element]):
            Style factory which will be applied to the element.
            :class:`telegram_text.bases.PlainText` by default.
    """

    def __init__(self, text: str, style: Callable[[Union[str, Element]], Element] = PlainText):
        text = '#' + text.lstrip('#')
        super().__init__(text, style=style)


class Emoji(Element):
    """Custom Telegram emoji.

    Custom emoji entities can only be used by bots that purchased additional
    usernames on `Fragment <https://fragment.com/>`_.

    Args:
        emoji_id (int):
            Id of the custom emoji.
        default (str):
            Alternative value for the custom emoji.
            The emoji will be shown instead of the custom emoji in places
            where a custom emoji cannot be displayed (e.g., system
            notifications) or if the message is forwarded by a non-premium user.
    """

    def __init__(self, emoji_id: int, default: str):
        self.emoji_id = emoji_id
        self.default = default

    def to_plain_text(self) -> str:
        return self.default

    def to_markdown(self) -> str:
        return f"![{self.default}](tg://emoji?id={self.emoji_id})"

    def to_html(self) -> str:
        return f'<tg-emoji emoji-id="{self.emoji_id}">{self.default}</tg-emoji>'
