[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f1197825376)
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)


# Бот для NotPixel



# 🔥🔥 Используйте Python версии 3.10 - 3.11.5 🔥🔥

> 🇪🇳 README in english available [[here](https://github.com/Cybertat1on/NotPixel/blob/main/README.md)]

> [!WARNING]
> В качестве оплаты за этот скрипт я беру 10% ваших рефералов, чтобы уменьшить процент рефералов, вы можете настроить эту переменную PERCENT_OF_REFERRALS_FOR_CREATORS_OF_THE_SOFT.

## Функционал  
| Функционал                                                	 | Поддерживается  |
|-------------------------------------------------------------|:----------------:|
| Многопоточность                                             |        ✔️        |
| Привязка прокси к сессии                                    |        ✔️        |
| Авто реферрал                                               |        ✔️        |
| Авто клейм                                                  |        ✔️        |
| Авто покраска                                               |        ✔️        |
| Автозакрашивание определенного пикселя для получения x3 PX  |        ✔️        |
| Автозадание                                                 |        ✔️        |
| Авто апгрейд                                                |        ✔️        |
| Ночной режим                 							                        |        ✔️        |
| Поддержка пирограммы .session 		                            |        ✔️        |

## [Настройки](https://github.com/Cybertat1on/NotPixel/blob/main/.env-example/)
|                     Настройки                     |                                                                     Описание                                                                     |
|:-------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:|
|               **API_ID / API_HASH**               |                               Данные платформы, с которой будет запущена сессия Telegram (по умолчанию - android)                                |
|            **USE_RANDOM_DELAY_IN_RUN**            |                                                     Рандом после запуска (по умолчанию - True)                                                   |
|              **RANDOM_DELAY_IN_RUN**              |                                        Рандомная задержка в секундах для запуска (по умолчанию - [5, 30]                                         |
|             **SLEEP_TIME_IN_MINUTES**             |                                   Рандомная задержка в минутах между циклами (по умолчанию - [20, 40, 60, 80])                                   |
|                    **USE_REF**                    |                                 Регистрировать ваши аккаунты по вашей реф. ссылке или нет (по умолчанию - False)                                 |
|                    **REF_ID**                     |                                     Ваш реферальный аргумент (идет после app/startapp? в вашей реф. ссылке)                                      |
| **PERCENT_OF_REFERRALS_FOR_CREATORS_OF_THE_SOFT** |                                   Процент рефов который будет дан разработчику этого софта (по умолчанию - 10)                                   |
|              **USE_PROXY_FROM_FILE**              |                                     Использовать ли прокси из файла `bot/config/proxies.txt` (True / False)                                      |
|               **ENABLE_AUTO_TASKS**               |                                           Включить ли автоматическое выполнение тасков (True / False)                                            |
|               **ENABLE_AUTO_DRAW**                |                                             Включить ли автоматическое выполнение игр (True / False)                                             |
|        **UNSAFE_ENABLE_JOIN_TG_CHANNELS**         |                                        Включить ли автоматическое подключение к тг каналам (True / False)                                        |
|              **ENABLE_CLAIM_REWARD**              |                                             Включить ли автоматический збор ревардов (True / False)                                              |
|              **ENABLE_AUTO_UPGRADE**              |                                                Включить ли автоматический апгрейд  (True / False)                                                |
|                  **ENABLE_SSL**                   |           Включить проверку ssl сертификатов (думаю может помочь с решением SSL: CERTIFICATE_VERIFY_FAILED ошибки)  (default - False)            |
|               **DISABLE_IN_NIGHT**                |                                                Отсанавливать скрипт ночью (по умолчанию - False)                                                 |
|                  **NIGHT_TIME**                   |                                 Ночное время в какое скрипт будет остановлен  [от, до] (по умолчанию - [23, 6])                                  |
|         **ENABLE_RANDOM_CUSTOM_TEMPLATE**         |                                                  Использовать рандомный шаблон (default - True)                                                  |
|          **ENABLE_DRAW_CUSTOM_TEMPLATE**          |                                         Включение рисования по случайному шаблону (по умолчанию - True)                                          |
|                 **ENERGY_LIMIT_MAX**              |                                         Максимальный уровень улучшения «Energy Limit» (по умолчанию - 6)                                         |
|               **PAINT_REWARD_MAX**                |                                         Максимальный уровень улучшения «Paint Reward» (по умолчанию - 5)                                         |
|              **RE_CHARGE_SPEED_MAX**              |                                       Максимальный уровень улучшения «Recharging Speed» (по умолчанию - 7)                                       |

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
