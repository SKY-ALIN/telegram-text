from abc import ABC, abstractmethod


class AbstractElement(ABC):
    @abstractmethod
    def to_plain_text(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_markdown(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_html(self) -> str:
        raise NotImplementedError
