from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from bot import bot

from config import PRIVATE_ID

from utils import dataProcessing
from utils import dataCollector
from utils.graphs import graphDrawing, grapghVolume, graphDensity, graphPrice, distSer
from utils.checker import timeCheck

from keyboards.userKb import inline_user_main_menu_keyboard, inline_doc_proc_keyboard,\
                             inline_int_keyboard, inline_period_keyboard

inputData = ['BTCUSDT']

# Стартовое сообщение
async def startMes(message : types.Message):
    await message.answer("<b>Меню</b> 🔎", reply_markup=inline_user_main_menu_keyboard)

# Загрузка txt файла
async def txtRec(message : types.Message):
    if (message.from_user.id != PRIVATE_ID):
        await message.reply("<i>У вас недостаточно прав</i>")
    else:
        if (message.document.mime_type == "text/plain"):
            fName = message.document.file_name

            # Скачиваем полученный документ
            await message.document.download(destination_file=f"temp\input\{fName}")

            # Словари с основными данными
            openDataDict = dataProcessing.dataReader(f"temp\input\{fName}")[0]
            closeDataDict = dataProcessing.dataReader(f"temp\input\{fName}")[1]
            volume = dataProcessing.dataReader(f"temp\input\{fName}")[2]
            # densityDict = dataProcessing.distributionDensity(dataDict)
            # Рисуем график
            graphDrawing("temp", "test.png", openDataDict, closeDataDict)
            grapghVolume("temp", "test1.png", volume)

            # Отправляем сохраненный график плотности
            # await bot.send_photo(message.from_user.id, types.InputFile(r'temp\test.png'), caption="<b>Анализ цены: </b>\n" + str(dataProcessing.priceAnalizer(dataDict)))
            await message.answer_photo(types.InputFile(r'temp\test.png'))
            await message.answer_photo(types.InputFile(r'temp\test1.png'))

            # Очищаем словари
            openDataDict.clear()
            closeDataDict.clear()
            volume.clear()
        else:
            await message.reply(f"Вы отправили <b>недопустимый формат документа</b>.\n\nДля корректной работы отправьте документ с расширением <i>.xlsx</i>.")

# Сбор данных
async def datacol_button(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите интервал измерений', reply_markup=inline_int_keyboard)

# Интервалы измерений
async def min_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('1m')

async def min30_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('30m')

async def hour_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('1h')

async def day_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('1d')

async def week_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('1w')

async def month_but(call : types.CallbackQuery):
    await call.message.edit_text(f'<b>Сбор данных</b>⛏\n\n'\
                                  'Выберите период измерений', reply_markup=inline_period_keyboard)
    inputData.append('1M')

# Периоды измерений
async def per2hour_but(call : types.CallbackQuery):
    inputData.append('2 hours ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per12hour_but(call : types.CallbackQuery):
    inputData.append('12 hours ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per1day_but(call : types.CallbackQuery):
    inputData.append('1 day ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per2day_but(call : types.CallbackQuery):
    inputData.append('2 days ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per3day_but(call : types.CallbackQuery):
    inputData.append('3 days ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per1week_but(call : types.CallbackQuery):
    inputData.append('1 week ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per2week_but(call : types.CallbackQuery):
    inputData.append('2 weeks ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per1month_but(call : types.CallbackQuery):
    inputData.append('1 month ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per6month_but(call : types.CallbackQuery):
    inputData.append('6 months ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')

async def per1year_but(call : types.CallbackQuery):
    inputData.append('1 year ago UTC')
    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных начат</i> 📲')

    path = "temp"
    fName = "data.txt"

    data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
    dataCollector.writeInfo(path, fName, data)

    doc = open((path + "\\" + fName), "rb")

    mesData = timeCheck(inputData)

    await call.message.edit_text(f'<b>Сбор данных</b> ⛏\n\n'\
                                  '<i>Сбор данных завершен</i> ✔\n\n'\
                                  'Валютная пара: <b>' + mesData[0] + '</b>\n'
                                  'Интервал: <b>' + mesData[1] + '</b>\n'\
                                  'Период измерений: <b>' + mesData[2] + '</b>')

    await call.message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
    doc.close()

    inputData.clear()
    inputData.append('BTCUSDT')


# Обработка данных из полученного документа
async def procdoc_button(call : types.CallbackQuery):
    fName = "data.txt"

    path = "temp"
    densityName = "density.png"
    priceName = 'price.png'
    distSerName = 'distSer.png'

    # Словари с основными данными
    dataOpen = dataProcessing.dataReader(path + "\\" + fName)[0]
    dataClose = dataProcessing.dataReader(path + "\\" + fName)[1]

    densityDataOpen = dataProcessing.distributionDensity(dataOpen)
    densityDataClose = dataProcessing.distributionDensity(dataClose)

    # Рисуем график
    graphDensity(path, densityName, dataOpen, dataClose)
    graphPrice(path, priceName, dataOpen, dataClose)
    distSer(path, distSerName, densityDataOpen, densityDataClose)

    # Отправляем сохраненный график плотности
    await call.message.answer_photo(types.InputFile(path + "\\" + priceName), caption= f"<b>Анализ цены</b>\n\n{dataProcessing.priceAnalizer(dataOpen, dataClose)}")
    await call.message.answer_photo(types.InputFile(path + "\\" + densityName), caption= f"<b>Плотности</b>")
    await call.message.answer_photo(types.InputFile(path + "\\" + distSerName), caption= f"<b>Ряд распределения</b>")

    # Очищаем словари
    dataOpen.clear()
    dataClose.clear()

    # await call.message.answer("<b>Меню</b> 🔎", reply_markup=inline_user_main_menu_keyboard)

# Остальные сообщения
# async def anMes(message : types.Message):
#     if '{' in message.text:
#         inputData = message.text.replace("{", "").replace("}", "").split(";")
#
#         path = "temp"
#         fName = "test.txt"
#
#         data = dataCollector.getKlines(inputData[0], inputData[1], inputData[2])
#         dataCollector.writeInfo(path, fName, data)
#
#         doc = open((path + "\\" + fName), "rb")
#         await message.answer_document(doc, "<i>Собранные данные</i>", reply_markup=inline_doc_proc_keyboard)
#         doc.close()

# Registaration of all user's handlers
def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(startMes, commands = ['start', 'restart'])
    # dp.register_message_handler(anMes, content_types=['text'])
    dp.register_message_handler(txtRec, content_types=['document'])

    dp.register_callback_query_handler(datacol_button, lambda c: c.data == 'collect')
    dp.register_callback_query_handler(procdoc_button, lambda c: c.data == 'procDoc')

    dp.register_callback_query_handler(min_but, lambda c: c.data == '1m')
    dp.register_callback_query_handler(min30_but, lambda c: c.data == '30m')
    dp.register_callback_query_handler(hour_but, lambda c: c.data == '1h')
    dp.register_callback_query_handler(day_but, lambda c: c.data == '1d')
    dp.register_callback_query_handler(week_but, lambda c: c.data == '1w')
    dp.register_callback_query_handler(month_but, lambda c: c.data == '1M')

    dp.register_callback_query_handler(per2hour_but, lambda c: c.data == '2HOUR')
    dp.register_callback_query_handler(per12hour_but, lambda c: c.data == '12HOUR')
    dp.register_callback_query_handler(per1day_but, lambda c: c.data == '1DAY')
    dp.register_callback_query_handler(per2day_but, lambda c: c.data == '2DAY')
    dp.register_callback_query_handler(per3day_but, lambda c: c.data == '3DAY')
    dp.register_callback_query_handler(per1week_but, lambda c: c.data == '1WEEK')
    dp.register_callback_query_handler(per2week_but, lambda c: c.data == '2WEEK')
    dp.register_callback_query_handler(per1month_but, lambda c: c.data == '1MONTH')
    dp.register_callback_query_handler(per6month_but, lambda c: c.data == '6MONTH')
    dp.register_callback_query_handler(per1year_but, lambda c: c.data == '1YEAR')
