import logging
from aiogram.utils import executor
from bot import dp

# Configure logging
logging.basicConfig(level=logging.INFO)

# Console message about bot's start state
async def launch(_):
    print('<Bot is running>')
    # Тут бахаем бд

# Import of user parts
from handlers import user
# Initialize user's handler function
user.register_handlers_user(dp)


"""
If the bot wasn't online, after launch it
skips all messages written earlier
Function <launch> will be executed
"""
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = launch)
