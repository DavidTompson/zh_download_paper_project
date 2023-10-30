import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from tqdm import tqdm
import pyautogui
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from enum import Enum
import pyperclip
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import os
import nltk
from nltk.corpus import stopwords
from .utils.browser_config import BrowserConfig

class DownloadPaper:
    def __init__(self, path) -> None:
        self.path=path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.driver=None
        self.result=[]


    def download_from_url(self):
        """直接从谷歌学术下载"""
        pass

    def download_from_scihub(self):
        """url下载失败时使用此方法，"""
        pass
    
    def download_from_cnki(self):
        """判断用户输入为中文时输入为此方法"""
        pass

    def start_browser(self, wait_time=10):
        # 创建ChromeOptions对象
        browser_config = BrowserConfig()
        options = browser_config.options
        # 创建Chrome浏览器实例
        self.driver = webdriver.Chrome(options=options)
        # 等待页面加载完成
        self.driver.implicitly_wait(wait_time)
