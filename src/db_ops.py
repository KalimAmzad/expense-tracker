import os
import streamlit as st
from st_aggrid import (GridOptionsBuilder, AgGrid, 
                       GridUpdateMode, ColumnsAutoSizeMode)
import pandas as pd
from utility import show_pdf


def show_data(df, columns):
    with st.expander("**Show** all Expenses"):                    
        gb = GridOptionsBuilder.from_dataframe(df[columns])
        # configure selection
        gb.configure_selection(selection_mode="single", use_checkbox=False)
        gb.configure_side_bar()
        gridOptions = gb.build()
        data = AgGrid(df,
                    gridOptions=gridOptions,
                    # enable_enterprise_modules=True,
                    allow_unsafe_jscode=True,
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)

        selected_rows = data["selected_rows"]

        if len(selected_rows) != 0:
            # col1, col2, col3, col4 = st.columns(4)
            documents_urls = selected_rows[0]['documents']
            # st.write(documents_urls)
            documents_urls = documents_urls.strip('[]').split(', ')
            doc_text = False
            for document in documents_urls:
                # file_path += document
                if document:
                    if not doc_text:
                        st.title("Referenced Documents")
                        doc_text = True
                    file_extension = os.path.splitext(document)[1].replace("'", '')
                    if file_extension in [".png", ".jpg", ".jpeg"]:
                        # Display the image file
                        url=os.path.join(os.getcwd(), document.strip("'.//"))
                        st.image(url, width=None)
                    elif file_extension == ".pdf":
                        # Display a link to the pdf file
                        url=os.path.join(os.getcwd(), document.strip("'.//"))
                        show_pdf(url)
                        # st.markdown("[Open the PDF file]({})".format(url))
                    else:
                        # Display the contents of the text file
                        url=os.path.join(os.getcwd(), document.strip("'.//"))
                        with open(url, "r") as f:
                            st.text(f.read())
                else:
                    st.error("Reference File does not exist.")


def edit_data(cursor, db, df, columns, label, table):
    with st.expander(label):
        with st.form(f'edit_{table}'):
            # select the columns you want the users to see
            gb = GridOptionsBuilder.from_dataframe(df[columns])
            gb.configure_default_column(editable=True)

            # configure selection
            # gb.configure_selection(selection_mode="single", use_checkbox=False)
            gb.configure_side_bar()
            gridOptions = gb.build()

            data = AgGrid(df,
                        editable=True,
                        gridOptions=gridOptions,
                        allow_unsafe_jscode=True,
                        # enable_enterprise_modules=True,
                        # update_mode=GridUpdateMode.SELECTION_CHANGED,
                        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)
            
            # grid_return = AgGrid(editable_df, editable=True, theme='streamlit')
            # st.write(data)
            new_df = data['data']
            st.form_submit_button('confirm', 
                                  on_click=sent_to_db(cursor, db, table, df, new_df))
            # st.rerun()




def delete_data(cursor, db, df, columns, label, table):
    with st.expander(label):
        with st.form(f'delete_{table}'):
            # select the columns you want the users to see
            gb = GridOptionsBuilder.from_dataframe(df[columns])
            # configure selection
            gb.configure_selection(selection_mode="single", use_checkbox=False)
            gb.configure_side_bar()
            gridOptions = gb.build()

            data = AgGrid(df,
                        gridOptions=gridOptions,
                        # enable_enterprise_modules=True,
                        allow_unsafe_jscode=True,
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)

            selected_rows = data["selected_rows"]
            # st.write(selected_rows)
            
            st.form_submit_button('Confirm', on_click=sent_to_delete_db(cursor, db, table, selected_rows))
            # st.rerun()



def sent_to_db(cursor, db, primary_table, df_ref, new_df):
    df_changes = df_ref.compare(new_df)
    # st.write(new_df)

    for row_index, col_name in df_changes.iterrows():
        # st.write(row_index, col_name.index.tolist())
        for col in col_name.index.tolist()[1::2]:
            # st.write(col)
            # st.write(col_name[col])
            if not pd.isna(col_name[col]):
                # st.write("Sure to udpate?") 
                data_id = new_df.iloc[row_index]['id']

                if col[0] not in ['bank', 'concern', 'payto', 'payfor']:
                    # st.write("Are you sure to update?")
                    if isinstance(col_name[col], str):
                        update_query = "UPDATE {} SET {}='{}' WHERE id={}".format(primary_table, col[0], col_name[col], data_id)
                    else:
                        update_query = "UPDATE {} SET {}={} WHERE id={}".format(primary_table, col[0], col_name[col], data_id)
                    # st.write(update_query)
                    cursor.execute(update_query)
                    db.commit()
                    st.success(f'ID: {data_id}, {col[0]} = {col_name[col]}   Edited Successfully!')
                    st.balloons()




def sent_to_delete_db(cursor, db, table_name, selected_rows):
    if len(selected_rows):
        # st.write("Are you sure to delete?")
        row_id = selected_rows[0]["id"]
        # st.write(selected_rows[0]["id"])
        delete_query = "DELETE from {} WHERE id={}".format(table_name, row_id)
        # st.write(delete_query)
        cursor.execute(delete_query)
        db.commit()
        st.success(f'ID: {row_id} Deleted Successfully!')
        st.balloons()
