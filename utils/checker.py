def timeCheck(data):
    curSymb = data[0]
    int = ''
    if data[1] == '1m':
        int = '1 минута'
    elif data[1] == '30m':
        int = '30 минут'
    elif data[1] == '1h':
        int = '1 час'
    elif data[1] == '1d':
        int = '1 день'
    elif data[1] == '1w':
        int = '1 неделя'
    elif data[1] == '1M':
        int = '1 месяц'

    per = ''
    if '2 hours' in data[2]:
        per = '2 часа'
    elif '12 hours' in data[2]:
        per = '12 часов'
    elif '1 day' in data[2]:
        per = '1 день'
    elif '2 days' in data[2]:
        per = '2 дня'
    elif '3 days' in data[2]:
        per = '3 дня'
    elif '1 week' in data[2]:
        per = '1 неделя'
    elif '2 weeks' in data[2]:
        per = '2 недели'
    elif '1 month' in data[2]:
        per = '1 месяц'
    elif '6 months' in data[2]:
        per = 'Полгода'
    elif '1 year' in data[2]:
        per = '1 год'

    return [curSymb, int, per]
