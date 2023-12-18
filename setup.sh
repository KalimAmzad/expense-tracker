#!/bin/bash
mkdir -p ~/.streamlit/

echo "
[server]
headless = true
port = 8582
enableCORS = false
" > ~/.streamlit/config.toml

cd ~/expense-tracker;
source ./env/bin/activate;
streamlit run app.py;