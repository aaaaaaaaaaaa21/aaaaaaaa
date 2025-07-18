import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="31을 말하면 지는 게임",
    layout="centered",
    page_icon="🐹"
)

# 초기화
if "count" not in st.session_state:
    st.session_state.count = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = ""

st.title("31을 말하면 지는 게임")
st.markdown("**규칙**: 1~3 사이의 숫자를 말하며, 마지막 31을 말하는 사람이 집니다.")

def reset_game():
    st.session_state.count = 0
    st.session_state.game_over = False
    st.session_state.message = ""

def computer_turn(last_say):
    """항상 4 - last_say를 선택하여 전략적으로 플레이"""
    # 남은 숫자 계산
    remain = 31 - st.session_state.count
    # 기본 4−사용자 수, 단 남은 수가 4 미만일 땐 남은 수만 말함
    choice = min(remain, max(1, 4 - last_say))
    st.session_state.count += choice
    return choice

# 메인 UI
st.write(f"현재 숫자: **{st.session_state.count}**")

# 사용자 턴
if not st.session_state.game_over:
    say = st.slider("말할 숫자 선택", 1, 3, 1, key="user_say")
    if st.button("제출하기"):
        # 사용자 수 더하기
        st.session_state.count += say
        
        # 사용자 패배 확인
        if st.session_state.count >= 31:
            st.session_state.message = "🎉 컴퓨터 승리! (사용자가 31을 말함)"
            st.session_state.game_over = True
        else:
            # 컴퓨터 턴
            comp = computer_turn(say)
            if st.session_state.count >= 31:
                st.session_state.message = f"😢 사용자 승리! (컴퓨터가 {comp}를 말해 31 이상)"
                st.session_state.game_over = True
            else:
                st.session_state.message = f"컴퓨터가 {comp}를 말했습니다."

# 결과 및 다시하기
if st.session_state.message:
    st.markdown(f"**{st.session_state.message}**")
if st.session_state.game_over:
    if st.button("다시하기"):
        reset_game()

