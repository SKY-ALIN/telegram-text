"""This file contains unofficial, but very useful markup elements."""

from typing import Callable

from .bases import Chain, Element, NEW_LINE
from .styles import InlineCode


class TOMLSection(Chain):
    """Section element in :code:`.toml` format.

    Args:
        text (str):
            Section name.
        elements (Tuple[Element]):
            Sections elements.
            Separator is :const:`telegram_text.bases.NEW_LINE`.
        style (Callable[[str], Element]):
            Style factory that will be applied to name.
            :class:`telegram_text.styles.InlineCode` by default.
    """

    def __init__(self, text: str, *elements: Element, style: Callable[[str], Element] = InlineCode):
        super().__init__(style(f"[{text}]"), *elements, sep=NEW_LINE)
