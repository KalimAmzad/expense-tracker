# Project Features
- User Authentication: Secure login system for personal use.
- Expense Management: Ability to add, view, edit, and delete expenses.
- Data Persistence: Save and retrieve expense data using files and databases.
- Categorization: Organize expenses into categories.
- Reporting: Visualize expenses with charts and summaries.
- Interactive GUI: A user-friendly web interface using Streamlit.
- Cloud Deployment: Deploy the application to the cloud using DigitalOcean.


# Project Setup
- create virtual environment
`virtualenv env`
- activate virtual environment
`source env/bin/activate`
- Install all required dependent libraries
`pip install -r requirements.txt`
- Check app is up and running
`streamlit run app.py`


### Setup DB
---
Store your db connection in `config.yaml`
Create a db name `expense` and run following command

`
python src/db_create.py
`



