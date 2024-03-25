# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

#st.title('Unit 4. Input Widgets')
#st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')
st.title('동귀를 위한 사이트 💕🐭')
st.caption('a.k.a 민지🐰 실습 자료')

st.header('1. button')
if st.button('동귀 안녕'):
    st.write('오늘도 화이띵 ❤️❤️❤️❤️❤️❤️❤️❤️😍😍 -민지가-')
else: st.write('빨리 눌러봐')

st.header('2. Radio Button')
genre = st.radio('좋아하는 장르를 선택하세요',
                ('민지','킴민지','모로무'))
if genre == '민지':
    st.write('나도 덩귀 좋아행😘😘')
elif genre =='킴민지':
    st.write('짜식이 나를 조아하기능ㅋ😎✌️')
else:
    st.write('나도 올레무 ❤️💕')


st.header('3. Checkbox')    # 😄
st.write('어떤 연금에 가입하시겠습니까')
agree = st.checkbox('민지 50년 만기 연금')
disagree=st.checkbox('안합니다.')
if agree:
    st.write('짜식이ㅋ','😄'*10)
else: st.write('')
if disagree: st.write('???🫥😑😶🤨 다시생각해봐')
else: st.write('')


st.header('4. toggle')
on = st.toggle('삼성생명 1등 SFP 되기')
if on:
    st.write('강동귀 SFP 0차월 신기록 달성!🙌🙌😄')


st.header('5. Select box')
option = st.selectbox('민지가 좋아하는 것',('덩귀🐭', '강덩귀', '강댕귀🐶', '귀동강👂', '올타임레전드 강동귀 ❤️💕'))
st.write('Minji loves', option)

st.header('6. Multi select')
options = st.multiselect('좋아하는 것을 모두 선택하세요',['민지', '만두', '모로무', 
                                            '뿌링클', '서핑', '클라이밍', '헬스', '🐭기네'])
st.write('DG likes ', ', '.join(options))




# st.header('7. Input: Text/Number')

# st.subheader('**_text_input_**')
# title =


# st.subheader('**_number_input_**')
# number = 


# st.header('8. Date input')
# ymd = 


# st.header('9. Slider')

# st.subheader('**_Slider- 이전 구간_**')
# age = 


# st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
# values = 


# st.subheader('**_년 월 일 사이 구간_**')

# slider_date = 






# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\4-1.input.py