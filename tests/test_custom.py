from telegram_text.custom import TOMLSection
from telegram_text.styles import Italic


def test_toml_section():
    obj = TOMLSection("Menu", Italic("Some description..."))
    assert obj.to_plain_text() == (
        "[Menu]\n"
        "Some description..."
    )
    assert obj.to_markdown() == (
        "`[Menu]`\n"
        "_Some description\\.\\.\\._"
    )
