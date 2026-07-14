import streamlit as st

st.set_page_config(page_title="Al Ahsa Heritage Game", page_icon="🌴")

st.title("🌴 لعبة تراث الأحساء")
st.subheader("Al Ahsa Heritage Tic-Tac-Toe")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.player = "🌴"

wins = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def winner():
    b = st.session_state.board
    for w in wins:
        a,b1,c = w
        if b[a] != "" and b[a]==b[b1]==b[c]:
            return b[a]
    return None

def draw():
    return "" not in st.session_state.board

def click(i):
    if st.session_state.board[i]=="":
        st.session_state.board[i]=st.session_state.player
        st.session_state.player="🏺" if st.session_state.player=="🌴" else "🌴"

for r in range(3):
    cols=st.columns(3)
    for c in range(3):
        i=r*3+c
        cols[c].button(
            st.session_state.board[i] if st.session_state.board[i] else " ",
            key=i,
            on_click=click,
            args=(i,),
            use_container_width=True
        )

w=winner()

if w:
    st.success(f"🏆 الفائز هو {w}")
elif draw():
    st.info("🤝 تعادل")

if st.button("🔄 ابدأ من جديد"):
    st.session_state.board=[""]*9
    st.session_state.player="🌴"
    st.rerun()
