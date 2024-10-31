[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f1197825376)
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)

#  Bot for NotPixel
![start-notpixel](https://github.com/user-attachments/assets/e0450f23-4df2-4620-b82e-202ad31b6040)

# 🔥🔥 PYTHON version must be 3.10 - 3.11.5 🔥🔥

> 🇷 🇺 README in russian available [[here](https://github.com/Cybertat1on/NotPixel/blob/main/README-RU.md)]


## Features  
| Feature                                                    | Supported  |
|--------------------------------------------------------------|:----------------:|
| Multithreading                                               |        ✔️        |
| Proxy binding to session                                     |        ✔️        |
| Auto Referral                                                |        ✔️        |
| Auto claim                                                   |        ✔️        |
| Auto paint                                                   |        ✔️        |
| Auto paint specific pixel to get x3 PX                       |        ✔️        |
| Auto task                                                    |        ✔️        |
| Auto upgrade                                                 |        ✔️        |
| Night sleep mode                 							   |        ✔️        |
| Get actual templates list(in browser)                        |        ✔️        |
| Support for pyrogram .session                     	       |        ✔️        |

## [Settings](https://github.com/Cybertat1on/NotPixel/blob/main/.env-example)

|                     Settings                      |                                                                 Description                                                                 |
|:-------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
|               **API_ID / API_HASH**               |                                  Platform data from which to run the Telegram session (default - android)                                   |
|            **USE_RANDOM_DELAY_IN_RUN**            |                                                          Random after start (default - True)                                                |
|              **RANDOM_DELAY_IN_RUN**              |                                             Random seconds delay for start(default is [5, 30])                                              |
|             **SLEEP_TIME_IN_MINUTES**             |                                         Random minutes delay between cycles (default is [120, 180])                                         |
|                    **USE_REF**                    |                                         Register accounts with ur referral or not (default - False)                                         |
|                    **REF_ID**                     |                                  Your referral argument (comes after app/startapp? in your referral link)                                   |
| **PERCENT_OF_REFERRALS_FOR_CREATORS_OF_THE_SOFT** |                                         Give some referrals for creator of the soft (default - 10)                                          |
|              **USE_PROXY_FROM_FILE**              |                                Whether to use a proxy from the `bot/config/proxies.txt` file (True / False)                                 |
|               **ENABLE_AUTO_TASKS**               |                                                      Enable auto tasks (True / False)                                                       |
|               **ENABLE_AUTO_DRAW**                |                                                     Enable auto drawing (True / False)                                                      |
|        **UNSAFE_ENABLE_JOIN_TG_CHANNELS**         |                                              Enable auto joining to tg channels (True / False)                                              |
|              **ENABLE_CLAIM_REWARD**              |                                                 Enable auto claim of rewards (True / False)                                                 |
|              **ENABLE_AUTO_UPGRADE**              |                                                    Enable auto upgrading (True / False)                                                     |
|              **ENABLE_SERVER_MODE**               |                           Stable mode to get more x3 but work only with few hardcoded templates (default - False)                           |
|                  **ENABLE_SSL**                   |        Enable verification of ssl certificates (sometimes it can help with SSL: CERTIFICATE_VERIFY_FAILED error)  (default - False)         |
|               **DISABLE_IN_NIGHT**                |                                                  Disable script in night (default - False)                                                  |
|                   **NIGHT_TIME**                  |                                                  Night time [from, to] (default - [23, 6])                                                  |
|         **ENABLE_RANDOM_CUSTOM_TEMPLATE**         |                                                   Use random templating (default - True)                                                    |
|          **ENABLE_DRAW_CUSTOM_TEMPLATE**          |                                            Enable drawing by random templating (default - True)                                             |
|               **ENERGY_LIMIT_MAX**                |                                                MAX Lvl Energy «Limit upgrade» (default - 6)                                                 |
|               **PAINT_REWARD_MAX**                |                                                MAX Lvl Paint «Reward upgrade» (default - 5)                                                 |
|              **RE_CHARGE_SPEED_MAX**              |                                              MAX Lvl Recharging «Speed upgrade» (default - 7)                                               |

## Quick Start 📚

To fast install libraries and run bot - open `run.bat` on **Windows** or `run.sh` on **Linux**

## Prerequisites
Before you begin, make sure you have the following installed:
- [**Python**](https://www.python.org/downloads/release/python-3100/) **version 3.10**

## Obtaining API Keys
1. Go to [**my.telegram.org**](https://my.telegram.org/auth) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

## Installation
You can download the [**repository**](https://github.com/Cybertat1on/NotPixel) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/Cybertat1on/NotPixel.git
cd NotPixel
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/NotPixel >>> python3 main.py --action (1/3)
# Or
~/NotPixel >>> python3 main.py -a (1/3)

# 1 - Run clicker
# 2 - Creates a session
# 3 - Get actual templates list(in browser)
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/NotPixel >>> python main.py --action (1/3)
# Or
~/NotPixel >>> python main.py -a (1/3)

# 1 - Run clicker
# 2 - Creates a session
# 3 - Get actual templates list(in browser)
```
