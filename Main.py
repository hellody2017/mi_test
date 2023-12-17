
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

def show_pages(pages):
    # 페이지를 표시하는 로직을 여기에 추가

    # pages 변수를 반환
    return pages
    
st.set_page_config(
    page_title="다중지능 검사",
    page_icon= ":clipboard:"
)
# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
#add_page_title()- 각각의 페이지에 제목이 들어가는 기능 

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [ 
        Page("Main.py","사용하기 전에",":warning:"),
        Page("whatismi.py","다중지능이란",":mag_right:" ),
        Page("mitest.py","다중지능검사",":writing_hand:"),
        Page("miapp.py", "직업탐구", ":writing_hand:"),
    ]
)

selected_page = st.sidebar.selectbox("페이지 선택", [page.title for page in pages])

# 선택된 페이지 호출
for page in pages:
    if page.title == selected_page:
        page.show_content()

st.header("주의사항:warning:")
image3 = "./image/warning.jpg"
st.image(image3,use_column_width=True)
