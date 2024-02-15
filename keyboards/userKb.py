from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton

user_menu_datacol = InlineKeyboardButton('Сбор данных ⛏', callback_data='collect')
user_menu_dataProc = InlineKeyboardButton('Обработка данных ⚙️', callback_data='proc')

doc_proc = InlineKeyboardButton('Обработка данных ⚙️', callback_data='procDoc')

period_1m_but = InlineKeyboardButton('Минута', callback_data='1m')
period_30m_but = InlineKeyboardButton('30 минут', callback_data='30m')
period_1h_but = InlineKeyboardButton('Час', callback_data='1h')
period_1d_but = InlineKeyboardButton('День', callback_data='1d')
period_1w_but = InlineKeyboardButton('Неделя', callback_data='1w')
period_1M_but = InlineKeyboardButton('Месяц', callback_data='1M')

period_2hour_but = InlineKeyboardButton('Два часа', callback_data='2HOUR')
period_12hour_but = InlineKeyboardButton('Двенадцать часов', callback_data='12HOUR')
period_1day_but = InlineKeyboardButton('Один день', callback_data='1DAY')
period_2day_but = InlineKeyboardButton('Два дня', callback_data='2DAY')
period_3day_but = InlineKeyboardButton('Три дня', callback_data='3DAY')
period_1week_but = InlineKeyboardButton('Неделя', callback_data='1WEEK')
period_2week_but = InlineKeyboardButton('Две недели', callback_data='2WEEK')
period_1month_but = InlineKeyboardButton('Месяц', callback_data='1MONTH')
period_6month_but = InlineKeyboardButton('Полгода', callback_data='6MONTH')
period_1year_but = InlineKeyboardButton('Год', callback_data='1YEAR')

inline_user_main_menu_keyboard = InlineKeyboardMarkup()
inline_doc_proc_keyboard = InlineKeyboardMarkup()
inline_int_keyboard = InlineKeyboardMarkup()
inline_period_keyboard = InlineKeyboardMarkup()

inline_user_main_menu_keyboard.add(user_menu_datacol).add(user_menu_dataProc)
inline_doc_proc_keyboard.add(doc_proc)
inline_int_keyboard.row(period_1m_but, period_30m_but).row(period_1h_but, period_1d_but).row(period_1w_but, period_1M_but)
inline_period_keyboard.row(period_2hour_but, period_12hour_but).row(period_1day_but, period_2day_but, period_3day_but).row(period_1week_but, period_2week_but).row(period_1month_but, period_6month_but).add(period_1year_but)
