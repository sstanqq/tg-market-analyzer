import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

import random

# from scipy.stats import gaussian_kde

matplotlib.style.use('ggplot')

colors = ['#577eff', '#fc4c58', '#6cfc4c', '#40b512', '#1560d1', '#bf1ad9', '#d6136e']

# Шрифт
hfont = {'fontname':'Times New Roman'}

def graphDrawing(path, fName, openData, closeData):

    # ser.plot.density()
    sns.lineplot(openData, color = colors[0], alpha = .2)
    sns.lineplot(closeData, color = colors[1], alpha = .2)
    plt.title('График цены открытия и цены закрытия', **hfont)
    plt.xlabel('Дата', **hfont)
    plt.ylabel('Цена', **hfont)

    plt.tight_layout()
    plt.savefig(f'{path}\{fName}')

    # Очищаем график
    plt.clf()

# График плотности распредления
def graphDensity(path, fName, dataOpen, dataClose):

    sns.kdeplot(dataOpen, color = colors[0], fill = True, alpha = .5)
    sns.kdeplot(dataClose, color = colors[1], fill = True, alpha = .5)
    plt.title('Плотность распределения цены', **hfont)
    plt.xlabel('Цена', **hfont)
    plt.ylabel('Плотность', **hfont)

    plt.tight_layout()
    plt.savefig(f'{path}\{fName}')

    # Очищаем график
    plt.clf()

def distSer(path, fName, dataOpen, dataClose):
    sns.lineplot(dataOpen, color = colors[2], markers=True, alpha = .8)
    sns.lineplot(dataClose, color = colors[1], markers=True, alpha = .8)

    plt.title('Ряд распредления', **hfont)
    plt.xlabel('Цена', **hfont)
    plt.ylabel('Кол-во повторений', **hfont)

    plt.tight_layout()
    plt.savefig(f'{path}\{fName}')

    # Очищаем график
    plt.clf()


def graphPrice(path, fName, dataOpen, dataClose):
    sns.lineplot(dataOpen, color = colors[2], alpha = .8)
    sns.lineplot(dataClose, color = colors[1], alpha = .8)
    plt.title('График валютной пары', **hfont)
    plt.xlabel('Время', **hfont)
    plt.ylabel('Цена', **hfont)

    plt.tight_layout()
    plt.savefig(f'{path}\{fName}')

    # Очищаем график
    plt.clf()


def grapghVolume(path, fName, data):
    sns.lineplot(data, color = colors[3], alpha = .2)
    plt.title('График цены открытия и цены закрытия', **hfont)
    plt.xlabel('Цена', **hfont)
    plt.ylabel('Объем', **hfont)

    plt.tight_layout()
    plt.savefig(f'{path}\{fName}')

    # Очищаем график
    plt.clf()


# def graphDrawing(path, fName, data):
#
#     x = list(data.keys())
#     y = list(data.values())
#
#     ser = pd.Series(x)
#     # ser.plot.density()
#     sns.kdeplot(x, color =colors[1],fill=True, alpha = .5)
#     plt.title('Плотность распределения цены', **hfont)
#     plt.xlabel('Цены', **hfont)
#     plt.ylabel('Плотность', **hfont)
#
#     plt.tight_layout()
#     plt.savefig(f'{path}\{fName}')
#
#     # Очищаем график
#     plt.clf()
