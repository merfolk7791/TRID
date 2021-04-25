from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
import asyncio
import random
import requests
from bs4 import BeautifulSoup
import json


bot = Bot(token="1762303078:AAFNw-cvwCbOcDWsQwwQHwflXGbWk1qq3og")
dp = Dispatcher(bot)

###############################################################################################################parsing crypto_news
crylinks = []
response = requests.get('https://www.rbc.ru/crypto/').text

soup = BeautifulSoup(response, 'lxml')

block1 = soup.find('div', class_ = 'g-overflow')
block2 = block1.find_all('div', class_ = 'item js-index-exclude')

for i in block2:
	block = i.find('a', class_ = 'item__link')
	blo = block.get('href')
    
	crylinks.append(blo)


#######################################################################################################################parsing_crypto

URL = 'https://coinmarketcap.com/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept':'*/*'}

for_json = []


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    tbody = soup.find('tbody')
    items = tbody.find_all('tr')
    counter = 0
    for item in items:
        name = item.find_all('td')[2].text[:-3].strip()
        price = item.find_all('td')[3].text.strip()
        h24_percent = item.find_all('td')[4].text.strip()
        marker_cap = item.find_all('td')[6].text.strip()
        volume_24h = item.find_all('td')[7].text.strip()
        circulating_Supply = item.find_all('td')[8].text.strip()
        for_json.append({
            'name': name,
            'price': price,
            'h24_percent': h24_percent,
            'marker_cap': marker_cap,
            'volume_24h': volume_24h,
            'circulating_Supply': circulating_Supply
            })
        counter += 1
        if counter > 9:
            break


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')

parse()

priice_bit = for_json[0]['price']
priice_eth = for_json[1]['price']
priice_bin_coin = for_json[2]['price']
priice_tether = for_json[3]['price']
priice_xrp = for_json[4]['price']
priice_cardano = for_json[5]['price']
priice_dogecoin = for_json[6]['price']
priice_polkadot = for_json[7]['price']

######################################################################################################################### get proxy 


link = "http://foxtools.ru/Proxy?page="
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept':'*/*'}


a = []
ips = []
ports = []
anon_degrees = []
countries = []
req_types = []

for i in range(1, 4):
    z = link + str(i)
    a.append(z)

for i in a:
    response = requests.get(i, headers=HEADERS, params=None).text
    soup = BeautifulSoup(response, 'lxml')

    block_without_class = soup.find('tbody').find_all('tr', class_ = '') # тд-шки без классов
    block_with_class = soup.find('tbody').find_all('tr', class_ = 'alt') # тд-шки с классами


    for j in range(1, len(block_with_class)):
        
        with_class = block_with_class[j].find_all('td', style='text-align:center') # собираю циклом каждый блок тд-шки
        without_class = block_without_class[j].find_all('td', style='text-align:center') # тож самое
        for_countries_wout_class = block_without_class[j].find_all('td', style='text-align:left;')
        for_countries_with_class = block_with_class[j].find_all('td', style='text-align:left;')

        
        countries.append(for_countries_with_class[0].text)
        countries.append(for_countries_with_class[0].text)

        
        ip_without_class = without_class[1].text             
        ip_with_class = with_class[1].text 
        
        ips.append(ip_without_class)
        ips.append(ip_with_class)

        port_without_class = without_class[2].text
        port_with_class = with_class[2].text

        ports.append(port_without_class)
        ports.append(port_with_class)

        anon_degree_woutClass = without_class[3].text.strip()
        anon_degree_withClass = with_class[3].text.strip()

        anon_degrees.append(anon_degree_woutClass)
        anon_degrees.append(anon_degree_withClass)

        req_type_withClass = with_class[4].text.strip()
        req_type_woutClass = without_class[4].text.strip()

        req_types.append(req_type_woutClass)
        req_types.append(req_type_withClass)



    ip_port = []
    for i in ips:
        for z in ports:
            ipp = i +':'+ z
            if ipp not in ip_port:
                ip_port.append(ipp)
print("Скрипт запущен")





###############################################################################################
cookiesmile = u'\U0001F36A'
quot = open(r"/home/faust/Рабочий стол/bot-tg/1.txt", "r")
quotes = quot.readlines()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Бот сделан командой TRID.'),
        ],
        [
            KeyboardButton(text='Курсы криптовалют 📈'),
            KeyboardButton(text='Крипто Новости 🗞')
        ],
        [
            KeyboardButton(text='Прокси 🛠'),
            KeyboardButton(text='Совет дня 🦉')
        ]
    ],
    resize_keyboard=True
)

cursobmena = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            KeyboardButton(text='bitcoin', callback_data= 'bitcoin'),
            KeyboardButton(text='etherium', callback_data='etherium')
        ],
        [
            KeyboardButton(text='binance coin', callback_data='binance coin'),
            KeyboardButton(text='tether', callback_data='tether')
        ],
        [
            KeyboardButton(text='xrp', callback_data='xrp'),
            KeyboardButton(text='cardano', callback_data='cardano')
        ],
        [
            KeyboardButton(text='dogecoin', callback_data='dogecoin'),
            KeyboardButton(text='polkadot', callback_data='polkadot')
        ],

        ],
)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Здравствуйте!\nЯ универсальный бот предоставляющий оперативную информацию на рынке ценных криптовалют!"+cookiesmile, reply_markup=menu)


@dp.message_handler(lambda message: message.text.lower().startswith('курс'))
async def choose_cours(message: types.Message):
    await message.answer('Напишите название валюты, курс которой вас интересует',reply_markup=cursobmena)



@dp.message_handler(lambda message: message.text.lower().startswith('прокси'))
async def choose_cours(message: types.Message):
    await message.answer(ip_port)
        
@dp.message_handler(lambda message: message.text.lower().startswith('совет'))
async def choose_cours(message: types.Message):
    await message.answer('Цитаты известных людей, которые помогут вам сделать правильный выбор\n\n'+ random.choice(quotes))


@dp.message_handler(lambda message: message.text.lower().startswith('крипто новости'))
async def choose_cours(message: types.Message):
    for i in crylinks:
        await message.answer(i)


@dp.callback_query_handler()
async def valuta(cb:types.callback_query.CallbackQuery):
    s = 'Курс криптовалюты {} :'.format(cb.data)
    if cb.data == 'bitcoin':
        await cb.message.answer(s+priice_bit)
    elif cb.data == 'etherium':
        await cb.message.answer(s+priice_eth)
    elif cb.data == 'binance coin':
        await cb.message.answer(s+priice_bin_coin)
    elif cb.data == 'tether':
        await cb.message.answer(s+priice_tether)
    elif cb.data == 'xrp':
        await cb.message.answer(s+priice_xrp)
    elif cb.data == 'cardano':
        await cb.message.answer(s+priice_cardano)
    elif cb.data == 'dogecoin':
        await cb.message.answer(s+priice_dogecoin)
    elif cb.data == 'polkadot':
        await cb.message.answer(s+priice_polkadot)
    else:
        await cb.message.answer('Вы ввели неизвестную крипто-валюту')


asyncio.run(dp.start_polling())
