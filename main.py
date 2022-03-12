import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title("Streamit超入門")

st.write("プログレスバーの表示")
'Start!!'

latest_interaction = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interaction.text(f'Interaction {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expand1 = st.expander('問い合わせ1')
expand1.write('問い合わせ1回答')
expand2 = st.expander('問い合わせ2')
expand2.write('問い合わせ2回答')
expand3 = st.expander('問い合わせ3')
expand3.write('問い合わせ3回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0 ,100, 50)

# 'あなたの趣味:',text
# 'コンディション：',condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open("test.jpg")
#     st.image(img, caption='景色', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50.50] + [35.69, 139.70],
#    columns=["lat", "lon"])
#
##st.table(df.style.highlight_max(axis=0))
#st.map(df)

