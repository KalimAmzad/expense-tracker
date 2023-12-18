import os
import streamlit as st
import pandas as pd

from src.db_ops import show_data, edit_data, delete_data


def save_expense(cursor, db):
    st.header('💸 Expense Entry')
    # st.write(st.session_state)
    if 'flag' not in st.session_state:
        st.session_state.flag = 0

    with st.form(key='expense_submit_form', clear_on_submit=False, border=True):
        expense_category = ['Shopping', 'Snacks', 'Mobile Recharge', 
                            'Online Course', 'Subscription', 'Others']

        expense_date = st.date_input('Expense Date*')
        category = st.selectbox('Expense Category*', expense_category)
        amount = st.text_input('Amount*')
        notes = st.text_area('Notes')
        document_upload = st.file_uploader('Upload Document', 
                                           type=['txt','pdf', 
                                                 'jpg', 'png', 'jpeg'], 
                                            accept_multiple_files=True)
        if st.form_submit_button(label='Submit'):
            if not(expense_date and category and amount):
                st.error('Please fill all the * fields')
            else:
                st.session_state.flag = 1
                # st.success('Data Submitted Successfully')


    if st.session_state.flag:
        # st.write(final_parameter_calculation)

        with st.form(key='final', clear_on_submit=True, border=True):
             # st.write(final_parameter_calculation)

            if st.form_submit_button('Are you Sure?'):
                # st.write(final_parameter_calculation)
                st.session_state.flag = 0
                # insert data into expense table
                
                # st.write(document_upload.read())
                # st.write(document_upload.name)
                # st.write(document_upload.getvalue())
                # file = open(document_upload.read(),'rb')
                all_documents = []
                for file in document_upload:
                    st.write(file.name)
                    # st.write(file.getvalue())
                    # st.write(file.read())
                    if file is not None:
                        # Get the file name and extract the extension
                        file_name = file.name
                        # st.write(file_name)
                        file_extension = os.path.splitext(file_name)[1]
                        dir_name = "./documents/expenses"
                        if not os.path.isdir(dir_name):
                            os.makedirs(dir_name)

                        file_url = dir_name + '/' + file_name
                        # file_url = dir_name + file_name
                        all_documents.append(file_url)

                        # Save the file in its original format
                        with open(file_url, "wb") as f:
                            f.write(file.read())
                        st.success("File has been successfully saved.")


                query = '''Insert into expense (expense_date, category, amount, 
                                                notes, documents) 
                        VALUES (%s, %s, %s, %s, %s)
                        '''
                values = (expense_date, category, amount, notes, str(all_documents))
                # st.write(query, values)
                cursor.execute(query, values)
                db.commit()
                st.success("Expense Record Inserted Successfully!")
                st.balloons()

            else:
                st.write("Click above button If you are Sure")
    else:
        st.warning("Please fill up above form")

    df = pd.read_sql('''SELECT id, expense_date, category, amount, notes, documents FROM expense''', con=db)
    
    # st.dataframe(df)

    # select the columns you want the users to see
    columns = [
               'expense_date',
                'category',
                'amount',
                'notes']   
    # st.dataframe(df[columns])
    show_data(df, columns)
    edit_data(cursor, db, df, columns, 'Edit Expenses', 'expense')
    delete_data(cursor, db, df, columns, 'Delete Expenses', 'expense')


