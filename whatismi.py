
import streamlit as st
st.set_page_config(
    page_title="다중지능 검사",
    page_icon= ":clipboard:"
)



# st.title("다중지능이란:question:")
# st.subheader("다음 영상을 보며 다중지능이 무엇인지 알아보고")
#st.subheader("다중 지능이 왜 중요한지 생각해봅시다.")

image1 = "./image/000.jpg"
st.image(image1)
video_url = "https://youtu.be/dSQXsBFXNZY?si=E91GkozdGKyqDsaJ"
st.video(video_url)

st.subheader("")
image11 = "./image/001.jpg"
st.image(image11)
st.subheader("")


#대인관계지능', '자연친화지능', '자기이해지능', '음악지능', '신체운동지능', '논리수학지능', '공간지능', '언어지능'

mi = [
    {
        "name" : "대인관계지능",
        "image": "./image/011.jpg"
    },
    {
        "name" : "자연친화지능",
        "image": "./image/012.jpg",
    },
    {
        "name" : "자기이해지능",
        "image": "./image/013.jpg"
    },
    {
        "name" : "음악지능",
        "image": "./image/014.jpg"
    },
    {
        "name" : "신체운동지능",
        "image": "./image/015.jpg"
    },
    {
       "name" : "논리수학지능",
       "image": "./image/016.jpg"
    },
    {
       "name" : "공간지능",
       "image": "./image/017.jpg"
    },
    {
       "name" : "언어지능",
       "image": "./image/018.jpg"
    },
]

tab_names = [m["name"] for m in mi]  
tabs = st.tabs(tab_names)

# Iterate through tabs and display content
for i, tab in enumerate(tabs):
    with tab:
        st.image(mi[i]["image"], use_column_width=True)


