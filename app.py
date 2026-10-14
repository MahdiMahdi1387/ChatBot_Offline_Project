import streamlit as st
import utils as ut

st.title('STREAMLIT CHATBOT')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role' : 'ai',
                                      'content' : 'How can I help You?'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input('Enter Your Question')
model = 'gemma3:1b'
if prompt:

    new_prompt = prompt + ' Describe your answer with detail and shape.' 
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role' : 'user',
                                        'content' : prompt})

    with st.spinner('Generating response...'):
        response = ut.call_ollama_model(new_prompt, model)

    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role': 'ai',
                                        'content' : response})

if st.button('DELETE HISTORY'):
    st.session_state['messages'] = [{'role': 'ai',
                                    'content': 'How can I help You?'}]
