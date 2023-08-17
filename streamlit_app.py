from src.rest.controller import Controller
import streamlit as st
from src.data_model.question import Question
from src.data_model.answer import Answer

class UI:
    def __init__(self):
        self.controller = Controller()

    def chat(self):
        # First
        st.session_state['context'] = []


        st.title("💬 Chatbot")
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "I can help to answer questions about GEN AI documentation. What is your answer?"}]

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        if prompt := st.chat_input():
            q = Question(question=prompt,
                         context=st.session_state['context']
                         )
            st.session_state['messages'].append({"role": "user", "content": prompt})

            answer:Answer = self.controller.chat(q)
            st.session_state['context'] = answer.past_conversations
            full_answer = f"{answer.answer} Retrieved from: {answer.source}"
            st.session_state['messages'].append({"role": "assistant", "content": full_answer})

            st.chat_message("assistant").write(full_answer)


ui = UI()
ui.chat()
