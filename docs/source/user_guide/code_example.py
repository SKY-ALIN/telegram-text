import os
from typing import Optional, Tuple
from time import time
from datetime import datetime

from telebot import TeleBot
from telegram_text import Bold, Chain, Code, InlineCode, Italic, Underline

API_TOKEN = os.getenv('API_TOKEN')  # Your bot secret token

bot = TeleBot(API_TOKEN)


def execute_python_code(code: str) -> Tuple[Optional[float], Optional[Exception]]:
    """Execute code and return execution time and exception.

    Note:
        Calculation is not perfect, It does not take into account the time it
        takes to translate the string into byte-code.

    Warning:
        This function is not safe, never use it in production.
    """
    try:
        start = time()
        exec(code)
        end = time()
    except Exception as e:
        return None, e

    # Calculate execution time in ms, round it and return
    return round((end - start) * 1000, 2), None


@bot.message_handler()
def format_python_to_pretty_code_block(message):
    # Get user's message
    code = message.text

    # Remember time when we start
    start_time = datetime.now()

    # Execute code
    execution_time, exception = execute_python_code(code)

    # Build a statistics part of the response
    if exception is None:
        # Case when code was executed successfully
        statistics_msg = Chain(
            Italic(f"Execution time: {execution_time} ms"),
            Italic(start_time.ctime()),
            sep='\n',
        )
    else:
        # Case when we got a exception
        statistics_msg = Chain(
            Bold("Runtime error:"),
            InlineCode(f"{exception.__class__.__name__}:\n{exception}\n"),
            Italic(start_time.ctime()),
            sep='\n',
        )

    # Build the response
    msg = Chain(
        Bold("=====") + Underline(Bold("Python Code")) + Bold("====="),
        Code(code, language='python'),
        Bold("======") + Underline(Bold("Statistics")) + Bold("======"),
        statistics_msg,
        Bold("====================="),
        sep='\n\n',
    )

    # Send response to the user
    bot.send_message(
        message.chat.id,  # Chat id
        msg.to_markdown(),  # Render response to MarkdownV2
        parse_mode="MarkdownV2",  # Specify parsing mode to Telegram API
    )


# Start our bot!
if __name__ == "__main__":
    bot.infinity_polling()
