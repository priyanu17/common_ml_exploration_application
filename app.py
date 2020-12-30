import os
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use("Agg")


def main():
    st.title("Dataset Explorer in Machine Learning with Streamlit")
    st.header("Perform exploratory data analysis on any dataset")
    st.write("  ***** ")

    html_temp = """ 
    <div style="background-color:orange;">
    <p style="color:white; font-size:50px;">
    Streamlit content from html</p>
    </div>
    """

    html_temp_2 = """
    
        <body style="background-color:green;">
        <p style = "color:white; font-size:30px">
        Text in white over a green background </p>
        </body>

    """
    #st.markdown(html_temp_2, unsafe_allow_html=True)

    def file_selector(folder_path="datasets"):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a file", filenames)
        return os.path.join(folder_path, selected_filename)
    # Select dataset and display dataset path
    selected_file = file_selector()
    st.info("You have selected : " + f" '{selected_file}' ")

    # Read Data
    df = pd.read_csv(selected_file)

    # Show Dataset
    if st.checkbox("Display Dataset : "):
        number = st.number_input("Enter number of rows to view", 1, 25)
        if number >= 1 and number <= 25:
            st.write("Displaying dataframe : ")
            st.dataframe(df.head(number))

    # Display columns
    if st.checkbox("View Column Names : "):
        st.write("Displaying column names : ")
        st.write(df.columns)

    # Show shape
    if st.checkbox("Display dataset shape : "):
        st.write(f"Shape of dataset is : {df.shape}")
        data_dim = st.radio("Select data dimension ", ("Rows", "Columns"))
        st.write(f"Number of rows is : {df.shape[0]}")
        st.write(f"Number of columns is : {df.shape[1]}")


if __name__ == "__main__":
    main()
