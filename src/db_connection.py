import yaml
import streamlit as st
import mysql.connector as mysql


with open('credintials.yml', 'r') as f:
    credintials = yaml.load(f, Loader=yaml.FullLoader)
    db_credintials = credintials['db']
    system_pass = credintials['system_pass']['admin']
    email_sender = credintials['email_sender']


@st.cache
def get_database_connection():
    db = mysql.connect(host = db_credintials['host'],
                      user = db_credintials['user'],
                      passwd = db_credintials['passwd'],
                      database = db_credintials['database'],
                      auth_plugin= db_credintials['auth_plugin'])
    
    cursor = db.cursor()

    return cursor, db




def get_all_members(db, cursor):
	pass

def get_single_member(db, cursor):
	pass