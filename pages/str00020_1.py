import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

code = '''
import streamlit as st

st.title('テストアプリ')
'''
st.code(code, language='python')