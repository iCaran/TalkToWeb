# 💬 Chat with Web!

#### A tool for you to go beyond just reading articles or websites.

This tool uses [BardAPI](https://github.com/dsdanielpark/Bard-API/) ↗ to summarize any article, website or link you may provide it. Apart from that, you can treat it as a normal conversation with a chatbot (Bard in this case), since that is what it essentially is.

This tool is intended to be used as a research tool, where you take the topics discussed in an article or website, and then start a whole thread or a rabbit hole based on it. Similar to [Chat With Youtube](https://github.com/iCaran/Chat-With-Youtube/) ↗

## 🔔 IMPORTANT UPDATE

### UPDATE - Bard API issues

Google has been messing with their internal apis, and [breaking the bardapi](https://github.com/dsdanielpark/Bard-API/issues/80) ↗.
Thanks to the constant effort of [dsdanielpark](https://github.com/dsdanielpark) the api is fixed and maintained consistently.

If you're a new installer and have never run `setup.bat` or `./setup.sh` before this, do so and after wards in a cmd/terminal run the following command, and do this everytime the script breaks
`pip install bardapi` or `pip install --upgrade bardapi`

Old users are recommended to the same to keep this script functioning.

## 🚀 Quickstart

1. Make sure you have [Python 3.8](https://www.python.org/downloads/release/python-3810/) ↗ installed. This tool works reliably only with Python 3.8

2. Grab a Google Bard API access token (read how [here](https://github.com/dsdanielpark/Bard-API#readme) ↗, or see below), paste it inside `token.txt`.

3. Download the latest release:
   - 💻 Windows: [TalkToWeb-Win.zip](https://github.com/iCaran/TalkToWeb/releases/download/v1.0.0/TalkToWeb-Win.zip) ↗
   - 🐧 Linux: [TalkToWeb-Lin.tar.xz](https://github.com/iCaran/TalkToWeb/releases/download/v1.0.0/TalkToWeb-Lin.tar.xz) ↗

4. Extract and run the setup script:
   - Windows: Double-click `setup.bat`
   - Linux: `chmod +x setup.sh and ./setup.sh`
    - then, `chmod +x chat.sh`

5. Talk to Bard or Summarize an article/website:
    Windows: Double click `chat.bat` and when prompted, enter a URL or type a prompt
    Linux: `./chat.sh` and when prompted, enter a URL or type a prompt

6. Sit back and enjoy your conversations!

## 🔑 Getting a Bard Token     

1. Visit https://bard.google.com/  
2. Press F12 to open the dev console     
3. Go to *Session* -> *Application* -> *Cookies*         
4. Copy the value of the `__Secure-1PSID` cookie   
5. Paste that value into the file named `token.txt`   

> **Warning:** Do not share your Bard token with anyone!
