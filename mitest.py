import streamlit as st
st.set_page_config(
    page_title="다중지능 검사",
    page_icon= ":clipboard:"
)

def calculate_intelligence_scores(answers):
    intelligence_scores = {
        '대인관계지능': answers[0] + answers[4]+ answers[37]+ answers[38]+ answers[40]+ answers[43]+ answers[48],
        '자연친화지능': answers[1] + answers[6]+ answers[22]+ answers[44]+ answers[46]+ answers[49]+ answers[52],
        '자기이해지능': answers[2] + answers[23]+ answers[26]+ answers[28]+ answers[34]+ answers[45]+ answers[47],
        '음악지능': answers[5] + answers[8]+ answers[13]+ answers[36]+ answers[41]+ answers[53]+ answers[54],
        '신체운동지능': answers[7] + answers[9]+ answers[17]+ answers[32]+ answers[42]+ answers[54]+ answers[57],
        '논리수학지능': answers[14] + answers[16]+ answers[18]+ answers[20]+ answers[21]+ answers[25]+ answers[59],
        '공간지능': answers[15] + answers[24]+ answers[27]+ answers[30]+ answers[50]+ answers[55]+ answers[60],
        '언어지능': answers[10] + answers[12]+ answers[19]+ answers[31]+ answers[33]+ answers[35]+ answers[51],
    }
    sorted_intelligence_scores = sorted(intelligence_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_intelligence_scores

def main():
    st.title('Step.2 다중지능 테스트')

    # Initialize session_state if not already done
    if 'selected_intelligences' not in st.session_state:
        st.session_state.selected_intelligences = []

    # Variable to track selected intelligences
    selected_intelligences = st.session_state.selected_intelligences

    # 다중지능 예상 순서 선택
    st.sidebar.title('Step.1 예상하기')
    selected_intelligences = st.sidebar.multiselect(
        '검사를 진행하기 전에 다중지능 순위를 예상해봅시다. 강점지능이라고 생각하는 순으로 클릭해보세요.',
        ['대인관계지능', '자연친화지능', '자기이해지능', '음악지능', '신체운동지능', '논리수학지능', '공간지능', '언어지능']
    )

    # Update session_state with selected_intelligences
    st.session_state.selected_intelligences = selected_intelligences

    if len(selected_intelligences) != 8:
        st.warning('예상 순위를 먼저 선택하고 검사를 진행해주세요. (8개를 모두 선택해야 합니다.)')
        return

    st.sidebar.title('다중지능 예상 순위')
    for i, intelligence in enumerate(selected_intelligences):
        st.sidebar.markdown(f'{i + 1}. **{intelligence}**')

    # 다중지능 검사 진행
    #st.write('\n\n### 질문을 잘 읽고 답하시오.')
    answers = [0] * 61
    questions = [
        '나는 어떤 친구가 도움이 필요한 친구인지 잘 알아차리는 것 같다.',
        '내가 제일 좋아하는 텔레비전 프로그램은 자연에 관한 다큐멘터리이다.',
        '나는 내가 피곤한지, 기분이 좋은지 나쁜지를 금방 안다.',
        '나는 무슨 일이든지 잘한다.',
        '나는 친구들 사이의 싸움을 잘 해결하고 화해시키는 사람이다.',
        '나는 숨쉬기, 빠르기, 셈 여림, 감정을 잘 살려서 노래 부른다.',
        '나는 수의사, 원예사, 일기 예보관 등 자연과 관련된 직업을 갖고 싶다.',
        '나는 무용이나 운동을 배우려고 노력하고 있다.',
        '나는 악보에 나오는 여러 기호의 뜻을 잘 알고 있다.',
        '나는 몸놀림이나 손놀림이 민첩하다.',
        '나는 또래 친구들이 모르는 낱말의 뜻을 잘 안다.',
        '나는 때때로 예의없게 행동하는 친구와 싸우고 싶다.',
        '나는 다른 친구가 쓴 글 속에서 맞춤법에 맞지 않은 표현이나 잘못된 문장을 잘 찾아낸다.',
        '나는 누가 연주를 잘하는지, 못하는지 또는 노래를 잘 하는지, 못하는지 알 수 있다.',
        '나는 다른 과목보다는 수학이나 과학을 더 잘한다.',
        '나는 길을 잘 찾는다.',
        '나는 논리 정연하고 토론을 잘 한다.',
        '나는 운동을 잘한다는 말을 자주 듣는다.',
        '나는 어떤 일의 원인이나 이유를 밝히는 것이 재미있다.',
        '나는 글을 잘 쓴다고 칭찬받는다.',
        '나는 음식점이나 가게에서 거스름돈 계산을 잘한다.',
        '나는 선생님 말씀에 따라 과학실험을 잘한다.',
        '나는 다른 어떤 곳보다 동물원이나 식물원 가는 것을 좋아한다.',
        '나는 나 혼자만의 시간이 꼭 필요하다.',
        '나는 만들기나 그림 그리는 것을 좋아한다.',
        '나는 다른 사람의 말 속에서 틀린 점이나 말이 맞지 않는 것을 잘 찾아낸다.',
        '나는 위인전을 읽고 배울 점을 찾는 것을 좋아한다.',
        '나는 어떤 것이든 한두 번만 보고 비슷하게 그릴 수 있다.',
        '나는 집이나 학교에서의 내가 해야 할 역할이 무엇인지 안다.',
        '나는 어려움에 있는 모든 사람을 돕는다.',
        '나는 고장난 기계나 물건을 잘 고친다.',
        '나는 커서 시인이나 작가, 아나운서가 될 소질이 있는 것 같다.',
        '나는 십자수, 조각, 조립과 같이 섬세한 손놀림이 필요한 활동을 잘할 수 있다.',
        '나는 국어 시간이나 글쓰기 시간을 좋아한다.',
        '나는 어떤 일에 실패했을 때 다음에는 그런 일이 생기지 않도록 깊이 생각한다.',
        '나는 책이나 글을 읽으면 빨리 이해한다.',
        '나는 악기를 쉽게 배운다.',
        '나는 친구들의 고민거리를 들어주거나 도와주는 것을 좋아한다.',
        '나는 친구든, 선생님이든, 형제든 누구하고도 잘 지낸다.',
        '나는 놀이나 게임에서 이기고 싶다.',
        '나는 친구와 싸웠을 때 어떻게든 다시 화해하려고 노력한다.',
        '나는 집에서 항상 음악을 즐겨 듣는다.',
        '나는 개그맨, 연예인, 가족이나 주변 사람들의 행동을 잘 흉내낼 수 있다.',
        '나는 다른 사람들로부터 다정하고 친절하다는 소리를 듣는다.',
        '나는 탐험을 좋아한다.',
        '나는 하루를 돌아보며 앞으로의 생활을 계획하는 일을 좋아한다.',
        '나는 혼자서 곤충기록이나 식물기록 일지를 만든 적이 있다.',
        '나는 평소에 나의 능력이나 재능을 키우기 위해 노력한다.',
        '나는 친구들 사이에서 인기가 많다.',
        '나는 집에서 양파나 꽃 기르기, 곤충 기르기, 애완견 기르기 등 무엇인가를 기른다.',
        '나는 공부할 때 그림을 그리거나 개념지도(마인드맵)를 그려가며 외운다.',
        '나는 말을 잘한다는 소리를 듣는다.',
        '나는 날씨, 기후, 음식의 맛을 다른 사람보다 잘 안다.',
        '나는 어떤 음악을 들으면 그 곡의 빠르기나 음의 높낮이를 알 수 있다.',
        '나는 롤러 브레이드, 자전거 등 몸을 많이 움직이는 놀이를 좋아한다.',
        '나는 내 방이나 내 물건을 재미있고 예쁘게 꾸민다.',
        '나는 절대로 거짓말하지 않는다.',
        '나는 어떤 운동이라도 몇 번만 해보면 잘할 수 있다.',
        '나는 방과후 활동으로 노래 배우기, 피아노 같은 악기 배우기 등을 하고 싶다.',
        '나는 어떤 것을 그냥 외우기보다는 이유를 따지면서 외우는 것이 더 좋다.',
        '다른 사람들은 내게 그림 그리기나 만들기를 잘한다고 말한다.'
    ]

    for i, question in enumerate(questions):
        st.subheader(f'{i + 1}. {question}')
        unique_key = f'question_{i + 1}'
        selected_option = st.radio(
            '',
            options=['(1) 전혀 그렇지 않다', '(2) 거의 그렇지 않다', '(3) 보통이다', '(4) 대체로 그렇다', '(5) 매우 그렇다'],
            index=None,  # 기본값을 선택하지 않음
            key=unique_key  # 고유한 키 할당
        )

        # Convert selected option to score
        answers[i] = int(selected_option[1]) if selected_option is not None else 0

    # "결과 계산" 버튼을 클릭할 때 모든 질문에 대한 응답이 있는지 확인
    if st.button('결과 알아보기'):
        if all(answers):
            intelligence_scores = calculate_intelligence_scores(answers)
            #st.write('\n\n### 내가 예상했던 다중지능 순위와 비교해보세요.\n')
            st.subheader('내가 예상했던 다중지능 순위와 비교해보세요.', divider='rainbow')
            for intelligence, score in intelligence_scores:
                st.subheader(f'{intelligence}: {score}')
        else:
            st.warning('모든 질문에 응답한 후 "결과 알아보기"를 클릭하세요.')

if __name__ == '__main__':
    main()
           
