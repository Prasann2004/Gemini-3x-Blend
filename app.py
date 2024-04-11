from Gemma_3x_bend.Gemini_3x_blend import Gemini_3x_blend     
import streamlit as st
st.title("Gemini 3x Blend")

user_quest = st.text_input("Ask a technical question:")
btn = st.button("Ask")

if btn and user_quest:
    result = Gemini_3x_blend(user_quest)
    st.subheader("Response : ")
    st.text(result)