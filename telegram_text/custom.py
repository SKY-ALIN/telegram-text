from typing import Callable

from .bases import Chain, Element, NEW_LINE
from .styles import InlineCode


class TOMLSection(Chain):
    def __init__(self, name: str, *elements: Element, style: Callable[[str], Element] = InlineCode):
        super().__init__(style(f"[{name}]"), *elements, sep=NEW_LINE)
