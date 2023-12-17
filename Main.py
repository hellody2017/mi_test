import streamlit as st
from st_pages import Page

def show_pages(pages):
    # 페이지 목록을 생성하고 반환
    return [page.title for page in pages]

def show_content(selected_page, pages):
    # 선택된 페이지 호출
    for page in pages:
        if page.title == selected_page:
            page.show_content()

st.set_page_config(
    page_title="다중지능 검사",
    page_icon=":clipboard:"
)

# 페이지 목록 생성
pages = [
    Page("Main.py", "사용하기 전에", ":warning:"),
    Page("whatismi.py", "다중지능이란", ":mag_right:"),
    Page("mitest.py", "다중지능검사", ":writing_hand:"),
    Page("miapp.py", "직업탐구", ":writing_hand:"),
]

# 페이지 목록을 보여주기
selected_page = st.sidebar.selectbox("페이지 선택", show_pages(pages))

# 선택된 페이지 내용을 표시
show_content(selected_page, pages)

st.header("주의사항:warning:")
image3 = "./image/warning.jpg"
st.image(image3, use_column_width=True)












# import streamlit as st
# from st_pages import Page, Section, show_pages, add_page_title

# st.set_page_config(
#     page_title="다중지능 검사",
#     page_icon= ":clipboard:"
# )

# show_pages(
#     [ 
#         Page("Main.py","사용하기 전에",":warning:"),
#         Page("whatismi.py","다중지능이란",":mag_right:" ),
#         Page("mitest.py","다중지능검사",":writing_hand:"),
#         Page("miapp.py", "직업탐구", ":writing_hand:"),
#     ]
# )

# selected_page = st.sidebar.selectbox("페이지 선택", [page.title for page in pages])

# for page in pages:
#     if page.title == selected_page:
#         page.show_content()

# st.header("주의사항:warning:")
# image3 = "./image/warning.jpg"
# st.image(image3,use_column_width=True)
