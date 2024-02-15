from datetime import datetime

# Чтение .txt в словарь ("Дата", "Цена")
def dataReader(fName):
    # Инициализация словаря
    dataOpen = {}
    dataClose = {}
    volume = {}

    # Чтение файла и занесение его в словарь
    with open(fName, "r") as f:
        for line in f:
            info = line.split(' ')
            dataOpen[datetime.strptime(info[0], "%d.%m.%Y-%H:%M")] = float(info[1].replace('\n', ''))
            dataClose[datetime.strptime(info[0], "%d.%m.%Y-%H:%M")] = float(info[2].replace('\n', ''))
            volume[float(info[2].replace('\n', ''))] = float(info[3].replace('\n', ''))
    return [dataOpen, dataClose, volume]

def priceAnalizer(dataOpen, dataClose):
    # Ключи словаря
    priceOpen = list(dataOpen.values())[0]
    priceClose = list(dataClose.values())[-1]

    message = f"  · Цена входа: <b>{priceOpen}</b>$\n  · Цена закрытия: <b>{priceClose}</b>$\n"

    if priceOpen > priceClose:
        message += f"  · Прирост: 📉<b>{round((((priceClose/priceOpen)-1)*100),3)}</b>%"
    elif priceOpen < priceClose:
        message += f"  · Прирост: 📈<b>{round((((priceClose/priceOpen)-1)*100),3)}</b>%"
    else:
        message += f"  · Прирост: <b>{((priceOpen/priceClose)-1)*100}</b>%"

    return message

def distributionDensity(d):
    # массив цен отсортированнных по возрастанию
    prices = list(d.values())
    prices.sort()

    retD = {}

    startVal = prices[0]
    counter = 0
    for i in range(len(prices)):
        if startVal == prices[i]:
            counter += 1
        else:
            retD[startVal] = counter

            startVal = prices[i]
            counter = 1

        retD[startVal] = counter


    return retD
