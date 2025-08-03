import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# テキスト関連
st.title('テストアプリ str00010')
st.caption('これはテストです')

# 画像
image = Image.open('./data/001.jpg')
st.image(image, width=200)
