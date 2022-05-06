from telegram_text.styles import (
    Bold,
    PlainText,
)

testing_string = "Hello world!"


def test_plain_text():
    obj = PlainText(testing_string)
    assert obj.text == testing_string
    assert str(obj) == testing_string
    assert obj.to_plain_text() == testing_string
    assert obj.to_markdown() == testing_string
    assert obj.to_html() == testing_string


def test_bold():
    obj = Bold(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '*' + testing_string + '*'
    assert obj.to_markdown() == '*' + testing_string + '*'
    assert obj.to_html() == '<b>' + testing_string + '</b>'
