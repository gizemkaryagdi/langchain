import streamlit as st
from streamlit_chat import message
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory
                                                  )

if 'conversation' not in st.session_state:
    st.session_state['conversation']=None
if 'messages' not in st.session_state:
    st.session_state['messages']=[]


st.set_page_config(page_title="ChatGPT Clone",page_icon=":robot_face:")
st.markdown("<hi style='text-align: center;'>Size nasıl yardımcı olabilirim? </h1>",unsafe_allow_html=True)

st.sidebar.title("🥳")
api_key=st.sidebar.text_input("API anahtarınız nedir?", type="password")
summarise_button=st.sidebar.button("Gönder",key="summarise")
if summarise_button:
    summarise_placeholder=st.sidebar.write("Seninle sohbet etmek çok güzel😻:\n\n"+"Merhaba!")

from dotenv import load_dotenv
load_dotenv()

def getresponse(user_input):

    if st.session_state['conversation'] is None:

        llm=ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.6,
        )

        st.session_state['conversation'] = ConversationChain(
        llm=llm,
            verbose=True,
            memory=ConversationBufferMemory()
        )

    response=st.session_state['conversation'].predict(input=user_input)
    print(st.session_state['conversation'].memory.buffer)

    return response

response_container=st.container()
container=st.container()

with container:
    with st.form(key="my_form",clear_on_submit=True):
        user_input=st.text_area("Sizin sorunuz:",key='input',height=100)
        submit_button=st.form_submit_button(label='Gönder')
        if submit_button:
            st.session_state['messages'].append(user_input)
            model_response=getresponse(user_input)
            st.session_state['messages'].append(model_response)
            st.write(st.session_state['messages'])

            answer=getresponse(user_input)
            with response_container:
                for i in range(len(st.session_state['messages'])):
                               if(i%2)==0:
                                    message(st.session_state['messages'][i],is_user=True,key=str(i)+'_user')
                               else:
                                    message(st.session_state['messages'][i],key=str(i)+'_AI')

