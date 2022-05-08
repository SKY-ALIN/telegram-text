# telegram-text
**Python markup module for Telegram messenger.
This module provides a rich list of components to build any possible
markup fast and render it to specific _html_ or _MarkdownV2_ formats.**

[![versions](https://img.shields.io/pypi/pyversions/telegram-text.svg)](https://github.com/SKY-ALIN/telegram-text)
![example workflow](https://github.com/SKY-ALIN/telegram-text/actions/workflows/tests.yml/badge.svg)
![example workflow](https://github.com/SKY-ALIN/telegram-text/actions/workflows/code-quality.yml/badge.svg)
[![codecov](https://codecov.io/SKY-ALIN/SKY-ALIN/telegram-text/branch/0.1.0-docs/graph/badge.svg?token=BK0ASC89B9)](https://codecov.io/SKY-ALIN/SKY-ALIN/telegram-text)
[![PyPI version fury.io](https://badge.fury.io/py/telegram-text.svg)](https://pypi.org/project/telegram-text/)
[![license](https://img.shields.io/github/license/SKY-ALIN/telegram-text.svg)](https://github.com/SKY-ALIN/telegram-text/blob/main/LICENSE)

---

### Installation
Install using `pip install telegram-text` or `poetry add telegram-text`

### Basic Example

```python
from telegram_text import Bold, Italic, Underline

text = Underline(Bold("Bold") + "and" + Italic("italic") + "with underline.")
```

### Advanced Example

```python
from telegram_text import Bold, Chain, Italic, TOMLSection, Hashtag, Link, UnorderedList

description = "A Channel about software developing and distributing. Subscribe to follow new technologies."
tags: dict[str, str] = {...}  # Tags description with following format `tag: tag_description`
links: dict[str, str] = {...}  # Links with following format `text: url`

menu = Chain(
    TOMLSection(
        'Menu',
        Italic(description),
    ),
    TOMLSection(
        'Tags',
        *[Hashtag(tag, style=Bold) + f"- {about}" for tag, about in tags.items()],
    ),
    TOMLSection(
        'Links',
        UnorderedList(*[Link(text, url) for text, url in links.items()]),
    ),
    sep='\n\n'
)


```

---

Full documentation and reference are available at 
[telegram-text.alinsky.tech](https://telegram-text.alinsky.tech)