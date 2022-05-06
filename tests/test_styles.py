from telegram_text.styles import (
    PlainText,
)


def test_plain_text():
    string = "Hello world!"
    obj = PlainText(string)
    assert obj.text == string
    assert str(obj) == string
    assert obj.to_plain_text() == string
    assert obj.to_markdown() == string
    assert obj.to_html() == string
