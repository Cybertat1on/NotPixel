[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/notpixel/app?startapp=f1197825376)
[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CyberToolz)

#  Bot for NotPixel
![start-notpixel](https://github.com/user-attachments/assets/e0450f23-4df2-4620-b82e-202ad31b6040)

# 🔥🔥 PYTHON version must be 3.10 - 3.11.5 🔥🔥

## Features  
| Feature                                                     | Supported  |
|---------------------------------------------------------------|:----------------:|
| Multithreading                                                |        ✔️        |
| Proxy binding to session                                      |        ✔️        |
| Auto Referral                                                 |        ✔️        |
| Auto claim                                                    |        ✔️        |
| Auto paint                                                    |        ✔️        |
| Auto paint specific pixel to get x3 PX                        |        ✔️        |
| Auto task                                                     |        ✔️        |
| Auto upgrade                                                  |        ✔️        |
| Night sleep mode                 							    |        ✔️        |
| Support for pyrogram .session                     	        |        ✔️        |

## [Settings](https://github.com/Cybertat1on/NotPixel/blob/main/.env-example)
| Settings 					      | Description 																								  |
|---------------------------------|:-------------------------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**   	      | Platform data from which to run the Telegram session (default - android)                                      | 
| **SLEEP_TIME**         	      | Sleep time between cycles (by default - [3000, 8000])        										    	  |      
| **REF_LINK**         	          | Put your ref link here  (10% for me)                                                              |
| **X3POINTS**					  | Auto paint specific pixel to get 3x px (default: True)														  |
| **AUTO_TASK**                   | Auto do tasks (default: True)                                                                                 |
| **AUTO_UPGRADE_PAINT_REWARD**   | AUTO upgrade paint reward if possible (default: True)                                              	          |
| **AUTO_UPGRADE_RECHARGE_SPEED** | AUTO upgrade recharge speed if possible (default: True)                                         	          |
| **AUTO_UPGRADE_RECHARGE_ENERGY**| AUTO upgrade energy limit if possible (default: True)                                          		          |
| **NIGHT_SLEEP**           	  | Extra sleep at night (by default - True)																	  |
| **NIGHT_SLEEP_START_TIME** 	  | Time (hour) when Night mode starts (by default - [0, 2])          											  |
| **NIGHT_SLEEP_END_TIME**  	  | Time (hour) when Night mode ends (by default - [5, 7])           											  |
| **USE_PROXY_FROM_FILE**   	  | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                                    |


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
~/NotPixel >>> python3 main.py --action (1/2)
# Or
~/NotPixel >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
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
~/NotPixel >>> python main.py --action (1/2)
# Or
~/NotPixel >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Termux manual installation
```
> pkg update && pkg upgrade -y
> pkg install python rust git -y
> git clone https://github.com/Cybertat1on/NotPixel.git
> cd Fabrika-Friends-Factory
> pip install -r requirements.txt
> python main.py
```

You can also use arguments for quick start, for example:
```termux
~/NotPixel > python main.py --action (1/2)
# Or
~/NotPixel > python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session 
```
