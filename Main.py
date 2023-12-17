# st_pages 모듈에서 가져올 수 있는 코드가 없으므로 예시로 직접 정의하는 경우
class Page:
    def __init__(self, title, content, icon):
        self.title = title
        self.content = content
        self.icon = icon

    def show_content(self):
        print(self.content)

# 나머지 코드는 그대로 유지
import streamlit as st

def show_pages(pages):
    return [page.title for page in pages]

def show_content(selected_page, pages):
    for page in pages:
        if page.title == selected_page:
            page.show_content()

st.set_page_config(
    page_title="다중지능 검사",
    page_icon=":clipboard:"
)

pages = [
    Page("Main.py", "사용하기 전에", ":warning:"),
    Page("whatismi.py", "다중지능이란", ":mag_right:"),
    Page("mitest.py", "다중지능검사", ":writing_hand:"),
    Page("miapp.py", "직업탐구", ":writing_hand:"),
]

#selected_page = st.sidebar.selectbox("페이지 선택", show_pages(pages))

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
