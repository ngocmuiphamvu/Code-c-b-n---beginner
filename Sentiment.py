import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob
import seaborn as sns
import networkx as nx
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
import logging
import json
from datetime import datetime
from pathlib import Path
import os
