from qna_bot import run_llm
import streamlit as st
from streamlit_chat import message

st.header("Welcome to About Shashi Kiran Bot")

prompt = st.text_input(
    "Prompt", placeholder="What do you want to know about Shashi Kiran.."
)
st.spinner("getting information..")
generated_response = run_llm(query=prompt)
st.text(prompt)
st.text(generated_response)

# st.spinner("getting information..")
# generated_response = run_llm(query=prompt)
# message(prompt, is_user=True)
# message(generated_response)

# if "user_prompt_history" not in st.session_state:
#     st.session_state["user_prompt_history"] = []
#
# if "chat_answers_history" not in st.session_state:
#     st.session_state["chat_answers_history"] = []
#
# if prompt:
#     with st.spinner("getting information.."):
#         generated_response = run_llm(query=prompt)
#         st.session_state["user_prompt_history"].append(prompt)
#         st.session_state["chat_answers_history"].append(generated_response)
#
# if st.session_state["chat_answers_history"]:
#     for generated_response, user_query in zip(
#         st.session_state["chat_answers_history"],
#         st.session_state["user_prompt_history"],
#     ):
#         message(user_query, is_user=True)
#         message(generated_response)
