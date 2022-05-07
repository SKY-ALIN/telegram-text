from typing import Callable

from .bases import Chain, Element, NEW_LINE
from .styles import PlainText


class OrderedList(Chain):
    def __init__(self, *elements: Element, style: Callable[[str], Element] = PlainText, sep: str = NEW_LINE):
        elements = [
            style(f"{n}.") + element
            for n, element in enumerate(elements, start=1)
        ]
        super().__init__(*elements, sep=sep)
