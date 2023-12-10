import os
import streamlit as st
from st_aggrid import (GridOptionsBuilder, AgGrid, 
                       GridUpdateMode, ColumnsAutoSizeMode)

def show_data(cursor, db, df, columns, label, table):
    with st.expander("**Show** all Payments"):                    
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
            st.form_submit_button('confirm', on_click=sent_to_db(cursor, db, table, df, new_df))



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
            
            st.form_submit_button('confirm', on_click=sent_to_delete_db(cursor, db, table, selected_rows))

