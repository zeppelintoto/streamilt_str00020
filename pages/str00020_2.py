import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

#
# リロード制御 ボタンを押下までリロードしない
with st.form(key='profile_form'):
        name2 = st.text_input('名前２')
        address = st.text_input('住所')
        
        # セレクトボックス
        age_category = st.selectbox(
                '年齢層',
                ('子供（18歳未満）', '大人（18歳以上）')
        )
        age_category2 = st.radio(
                '性別',
                ('男','女')
        )
        
        # 複数選択
        hobby = st.multiselect(
                '趣味',
                ('スポーツ', '読書', 'プログラミング', '映画', '料理')
        )
        
        # チェックボックス
        che_box = st.checkbox('メールマガジンを購読する')
        
        # スライダー
        height = st.slider('身長', min_value=110, max_value=210)
        
        # 日付
        start_date = st.date_input(
                '開始日',
                datetime.date(2022, 7, 1)
        )
        
        # カラーピッカー
        color = st.color_picker('テーマカラー', '#00f900')
        
        submit_btn2 = st.form_submit_button('送信')
        cancel_btn2 = st.form_submit_button('キャンセル')
        if submit_btn2:
                st.text(f'welcome!{name2}さん!{address}に書籍を送りました')
                st.text(f'年齢層:{age_category}')
                st.text(f'性別:{age_category2}')
                st.text(f'趣味:{",".join(hobby)}')
                st.text(f'購読:{che_box}')
                st.text(f'身長:{height}')
                st.text(f'日付:{start_date}')
                


