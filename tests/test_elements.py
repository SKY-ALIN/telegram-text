from telegram_text.bases import PlainText
from telegram_text.elements import Emoji, Hashtag, InlineUser, Link, User
from telegram_text.styles import Bold, Italic


def test_link():
    assert Link("link text", "https://Alinsky.tech/").to_markdown() == "[link text](https://Alinsky.tech/)"
    assert Link("link text", "https://Alinsky.tech/").to_html() == '<a href="https://Alinsky.tech/">link text</a>'


def test_inline_user():
    assert InlineUser("some user", 1).to_markdown() == "[some user](tg://user?id=1)"
    assert InlineUser("some user", 1).to_html() == '<a href="tg://user?id=1">some user</a>'


def test_hashtag_creation():
    assert Hashtag("hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("#hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("hashtag").to_markdown() == "\\#hashtag"
    assert Hashtag("#hashtag").to_markdown() == "\\#hashtag"
    assert Hashtag("hashtag").to_html() == "#hashtag"
    assert Hashtag("#hashtag").to_html() == "#hashtag"


def test_hashtag_style_fabric():
    assert Hashtag("hashtag", style=PlainText).to_markdown() == "\\#hashtag"
    assert Hashtag("hashtag", style=Bold).to_markdown() == "*\\#hashtag*"
    assert Hashtag("hashtag", style=Italic).to_markdown() == "_\\#hashtag_"
    assert Hashtag("hashtag", style=lambda string: Bold(Italic(string))).to_markdown() == "*_\\#hashtag_*"
    assert Hashtag("hashtag", style=lambda string: Bold(Italic(string))).to_plain_text() == "#hashtag"


def test_hashtag_main_styling():
    assert Bold(Hashtag("hashtag")).to_markdown() == "*\\#hashtag*"
    assert Italic(Hashtag("hashtag")).to_markdown() == "_\\#hashtag_"
    assert Bold(Italic(Hashtag("hashtag"))).to_markdown() == "*_\\#hashtag_*"
    assert Bold(Italic(Hashtag("hashtag"))).to_plain_text() == "#hashtag"


def test_user_creation():
    assert User("user").to_plain_text() == "@user"
    assert User("@user").to_plain_text() == "@user"
    assert User("user").to_markdown() == "@user"
    assert User("@user").to_markdown() == "@user"
    assert User("user").to_html() == "@user"
    assert User("@user").to_html() == "@user"


def test_user_style_fabric():
    assert User("user", style=PlainText).to_markdown() == "@user"
    assert User("user", style=Bold).to_markdown() == "*@user*"
    assert User("user", style=Italic).to_markdown() == "_@user_"
    assert User("user", style=lambda string: Bold(Italic(string))).to_markdown() == "*_@user_*"
    assert User("user", style=lambda string: Bold(Italic(string))).to_plain_text() == "@user"


def test_user_main_styling():
    assert Bold(User("user")).to_markdown() == "*@user*"
    assert Italic(User("user")).to_markdown() == "_@user_"
    assert Bold(Italic(User("user"))).to_markdown() == "*_@user_*"
    assert Bold(Italic(User("user"))).to_plain_text() == "@user"


def test_custom_emoji():
    emoji = Emoji(emoji_id=5368324170671202286, default="👍")
    assert emoji.to_plain_text() == "👍"
    assert emoji.to_markdown() == "![👍](tg://emoji?id=5368324170671202286)"
    assert emoji.to_html() == '<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>'
