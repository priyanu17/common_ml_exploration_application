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
    st.markdown(html_temp_2, unsafe_allow_html=True)

    def file_selector(folder_path="./datasets"):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a file", filenames)

    file_selector()
if __name__ == "__main__":
    main()
