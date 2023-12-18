import json
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import base64

def login(func):
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    # hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
    # st.write(hashed_passwords)

    authenticator.login('Sign-In', 'main')

    if st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    if st.session_state["authentication_status"]:
        with st.sidebar:
            authenticator.logout('Sign Out', 'main', key='unique_key')
            st.write(f'Welcome *{st.session_state["name"]}* 🤗')

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute
    

def load_expenses(filename):
    try:
        with open(filename, 'r') as infile:
            return json.load(infile)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        print("Error decoding JSON from file")
        return []



def save_expenses(expenses, filename):
    with open(filename, 'w') as outfile:
        json.dump(expenses, outfile, indent=4)


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

