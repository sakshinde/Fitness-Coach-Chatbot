<<<<<<< HEAD:.streamlit/fitness_coach.py
#import libraries
import openai 
import streamlit as st
from streamlit_chat import message    #streamlit_chat is a streamlit component developed for chats

openai.api_key = st.secrets["api_secret"]

   #declaring a variable "api_secret" for the api key

#creating a function to call the api

def generate_response(prompt):
    completions = openai.Completion.create(      #completions = variable
        engine = "text-davinci-003",             #text-davinci-003 is openai writeup formatting, grammar etc checking tool
        prompt = prompt,                        
        max_tokens = 1024,                       #input size
        n = 1,
        stop = None,
        temperature = 0.3,                       #this decides the randomness of the chatbot answers
    )
    message = completions.choices[0].text        
    return message

st.title("Fitfinity,your Virtual Fitness Coach!")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hola!, Tell me something about fitness.",key="input")
    return input_text    

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

       for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')







=======
#import libraries
import openai 
import streamlit as st
from streamlit_chat import message    #streamlit_chat is a streamlit component developed for chats

openai.api_key = "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"    #declaring a variable "api_secret" for the api key

#creating a function to call the api

def generate_response(prompt):
    completions = openai.Completion.create(      #completions = variable
        engine = "text-davinci-003",             #text-davinci-003 is openai writeup formatting, grammar etc checking tool
        prompt = prompt,                        
        max_tokens = 1024,                       #input size
        n = 1,
        stop = None,
        temperature = 0.3,                       #this decides the randomness of the chatbot answers
    )
    message = completions.choices[0].text        
    return message

st.title("Fitfinity,your Virtual Fitness Coach!")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hola! Tell me something about fitness.",key="input")
    return input_text    

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

       for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')







>>>>>>> 08bc0d28ffb1442ecaa7ab88295910191a81a9fe:fitness_coach.py
