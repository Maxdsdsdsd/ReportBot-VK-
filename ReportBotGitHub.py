from ast import arg
from colorama import Fore, Style, init
import requests, json, os, threading, random, time

os.system("cls||clear")

init(convert=True)

def logo():
    print(f"""{Fore.CYAN} ██▀███  ▓█████  ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██ ▒ ██▒▓█   ▀ ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██ ░▄█ ▒▒███   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▀▀█▄  ▒▓█  ▄ ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░██▓ ▒██▒░▒████▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
  ░▒ ░ ▒░ ░ ░  ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ▒░▒   ░   ░ ▒ ▒░     ░    
  ░░   ░    ░   ░░       ░ ░ ░ ▒    ░░   ░   ░       ░    ░ ░ ░ ░ ▒    ░      
   ░        ░  ░             ░ ░     ░               ░          ░ ░           
                                                          ░                   
{Style.RESET_ALL}
                                {Fore.LIGHTCYAN_EX}Version: 1.0{Style.RESET_ALL}\n
""")

with open('config.json', 'r') as cfg:
    config = json.load(cfg)
error_tag = f"{Fore.RED}[ERRO]{Style.RESET_ALL} "
good_tag = f"{Fore.GREEN}[GOOD]{Style.RESET_ALL} "

tokens = [""]
api_link = "https://api.vk.com/" + "method/"
method = api_link + "reports.add"

def report(timeout1):
    while (True):
        type = config['type']
        owner_id = config['owner_id']
        item_id = config['item_id']
        reason = config['reason']

        for i in range(len(tokens)):
            time.sleep(timeout1)
            request_report = requests.get(f"{method}?v=5.133&client_id=6287487&type={type}&owner_id={owner_id}&item_id={item_id}&reason={reason}&access_token={tokens[i]}")
            if request_report.status_code != 200:
                print(error_tag + "Request status_code: " + request_report.status_code)
                return
            respone = request_report.text
            if respone[12] != '1':
                print(error_tag + "Error respone: " + request_report.text)
            else:
                print(good_tag + f"Successfully Reported {i} (Code: {respone[12]})")
    
logo()

timeout = float(input("Timeout: "))

report(timeout)