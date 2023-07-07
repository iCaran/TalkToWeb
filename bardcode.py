from bardapi import Bard
import requests
import os
from extractor import extract_article_text

class bardSesh():
    def __init__(self):
        # Specify the file path where the token is stored
        self.token_file_path = 'token.txt'

    def bardSession(self, error_color = "\033[91m"):
        global bard

        # Check if the token file exists
        if not os.path.exists(self.token_file_path):
            print(error_color + 'Token file not found:', self.token_file_path)
            print(error_color + 'Please create a file named "token.txt" and store your token in it.')
            exit()

        with open(self.token_file_path, 'r') as file:
            token = file.read().strip()

        session = requests.Session()
        session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
        session.cookies.set("__Secure-1PSID", token)
        # session.cookies.set("__Secure-1PSID", token)

        try:
            bard = Bard(token=token, session=session, timeout=30)
        except Exception as e:
            print(error_color + "Couldn't connect, perhaps check your internet connection, or try with a different bard token.")
            print(error_color + "Something went wrong. Error:", str(e))
            exit()

    def getResponse(self, quompt, error_color = "\033[91m"):
        try:
            return bard.get_answer(quompt)['content']
        except Exception as e:
            print(error_color + "Something went wrong. Perhaps the Internet Connection was Lost. Error:", str(e))
            print()
            print("If the error looks weird, perhaps the bard api broke, try raising an issue.")
            exit()
        # return bard.get_answer(quompt)['content']

    def ai_summary(self, title,  text_to_summarize):
        # Call the API to generate the summary
        prompt = "Please summarize this article, but try to maintain every detail as much as possible, and try to make the summary as long as possible. The title of this article is '" + title + "'. Here is the article text: \n\n"
        summary = self.getResponse(prompt+text_to_summarize)
        return summary

    def on_submit(self, url):
        title, text = extract_article_text(url)
        if text=="":
            return '', ''
        summary = self.ai_summary(title, text)
        return title, summary  
