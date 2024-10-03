[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f1197825376
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)


# Бот для FriendsFactory



# 🔥🔥 Используйте Python версии 3.10 - 3.11.5 🔥🔥

> 🇪🇳 README in english available [here](README-EN)

## Features  
| Feature                                               	     | Supported  |
|----------------------------------------------------------------|:----------------:|
| Многопоточность                                                |        ✔️        |
| Привязка прокси к сессии                                       |        ✔️        |
| Авто реферрал                                                  |        ✔️        |
| Авто клейм                                                     |        ✔️        |
| Авто покраска                                                  |        ✔️        |
| Автозакрашивание определенного пикселя для получения x3 PX     |        ✔️        |
| Автозадание                                                    |        ✔️        |
| Авто апгрейд                                                   |        ✔️        |
| Ночной режим                 							         |        ✔️        |
| Поддержка пирограммы .session 		                         |        ✔️        |

## [Settings](https://github.com/Cybertat1on/NotPixel/blob/main/.env-example)
| Settings 					      | Description 																								  |
|---------------------------------|:-------------------------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**   	      | Данные платформы, с которой будет запущена сессия Telegram (по умолчанию - android)                            | 
| **SLEEP_TIME**         	      | Время сна между циклами (по умолчанию - [3000, 8000])       										    	  |      
| **REF_LINK**         	          | Поместите сюда свою реф-ссылку   (10% для меня)                                                                     |
| **X3POINTS**					  | Автоматическое закрашивание определенного пикселя для получения x3 PX (по умолчанию: True)								  |
| **AUTO_TASK**                   | Автоматическое выполнение заданий (по умолчанию: True)                                                    |
| **AUTO_UPGRADE_PAINT_REWARD**   | Автоматическое повышение награды за покраску, если это возможно (по умолчанию: True)                              |
| **AUTO_UPGRADE_RECHARGE_SPEED** | Автоматическое повышение скорости перезарядки, если это возможно (по умолчанию: True)               	          |
| **AUTO_UPGRADE_RECHARGE_ENERGY**| Автоматическое повышение лимита энергии, если это возможно (по умолчанию: True)                       	          |
| **NIGHT_SLEEP**           	  | Дополнительный сон ночью (по умолчанию - True) 																	  |
| **NIGHT_SLEEP_START_TIME** 	  | Время (час) начала ночного режима (по умолчанию - [0, 2])         											  |
| **NIGHT_SLEEP_END_TIME**  	  | Время (час) окончания ночного режима (по умолчанию - [5, 7])          											  |
| **USE_PROXY_FROM_FILE**   	  | Использовать ли прокси из файла bot/config/proxies.txt (True / False  

## Быстрый старт 📚

Для быстрой установки и последующего запуска - запустите файл `run.bat` на **Windows** или `run.sh` на **Линукс**

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/release/python-3100/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт [**my.telegram.org**](https://my.telegram.org/auth) и войдите в систему, используя свой номер телефона.
2. Выберите `API development tools` и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/Cybertat1on/NotPixel) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/Cybertat1on/NotPixel.git
cd NotPixel
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux ручная установка
```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/NotPixel >>> python3 main.py --action (1/2)
# Or
~/NotPixel >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```


# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/NotPixel >>> python main.py --action (1/2)
# Или
~/NotPixel >>> python main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```
# Termux ручная установка
```
> pkg update && pkg upgrade -y
> pkg install python rust git -y
> git clone https://github.com/Cybertat1on/NotPixel.git
> cd Fabrika-Friends-Factory
> pip install -r requirements.txt
> python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```termux
~/NotPixel > python main.py --action (1/2)
# Or
~/NotPixel > python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session 
```