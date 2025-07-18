import streamlit as st
import time
import random

def choice():
    if st.session_state.count < 6:
            if st.session_state.count == 1:
                return 1
            elif st.session_state.count == 2:
                return 1
            elif st.session_state.count == 3:
                return 3
            elif st.session_state.count == 4:
                return 2
            elif st.session_state.count == 5:
                return 1
            
    if st.session_state.count < 10 and st.session_state.count >= 6:
            if st.session_state.count == 6:
                return 1
            elif st.session_state.count == 7:
                return 3
            elif st.session_state.count == 8:
                return 2
            elif st.session_state.count == 9:
                return 1
    if st.session_state.count < 14 and st.session_state.count >= 10:
            if st.session_state.count == 10:
                return 1
            elif st.session_state.count == 11:
                return 3
            elif st.session_state.count == 12:
                return 2
            elif st.session_state.count == 13:
                return 1
    if st.session_state.count < 18 and st.session_state.count >= 14:
            if st.session_state.count == 14:
                return 1
            elif st.session_state.count == 15:
                return 3
            elif st.session_state.count == 16:
                return 2
            elif st.session_state.count == 17:
                return 1
    if st.session_state.count < 22 and st.session_state.count >= 18:
            if st.session_state.count == 18:
                return 1
            elif st.session_state.count == 19:
                return 3
            elif st.session_state.count == 20:
                return 2
            elif st.session_state.count == 21:
                return 1
    if st.session_state.count < 26 and st.session_state.count >= 22:
            if st.session_state.count == 22:
                return 1
            elif st.session_state.count == 23:
                return 3
            elif st.session_state.count == 24:
                return 2
            elif st.session_state.count == 25:
                return 1
    if st.session_state.count < 30 and st.session_state.count >= 26:
            if st.session_state.count == 26:
                return 1
            elif st.session_state.count == 27:
                return 3
            elif st.session_state.count == 28:
                return 2
            elif st.session_state.count == 29:
                return 1
    if st.session_state.count == 0:
         return 2
    if st.session_state.count == 30:
        return 1

def set_win():
    st.session_state.count = st.session_state.count + say
    st.success(f"귀하가 {say}를 말해 현재 숫자는 {st.session_state.count}이 되었습니다.")
    
    if st.session_state.count >= 31:
         st.error("귀하가 31(또는 그 이상)을 말해 실패하였습니다.")
         return
    comp_choice = choice()
    if st.session_state.count < 31:
        st.session_state.count = st.session_state.count + comp_choice
        st.success(f"컴퓨터가 {comp_choice}를 말해 현재 숫자는 {st.session_state.count}이 되었습니다")

    if st.session_state.count >= 31:
        st.success("컴퓨터가 31(또는 그 이상)을 말해 성공하였습니다.")
        return

if "count" not in st.session_state:
    st.session_state.count = 0



st.set_page_config(page_title="31을 말하면 지는 게임", layout="centered", page_icon="두더지.png")
st.markdown("**게임 규칙**")
st.markdown("31을 말하면 집니다")
say = st.slider("말할 숫자",1,3,2)

if st.button("제출하기"):
    set_win()
    
if st.session_state.count >= 31:
    if st.button("다시하기"):
         st.session_state.count = 0
