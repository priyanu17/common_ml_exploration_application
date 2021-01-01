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

    st.subheader("")
    # Show Dataset
    if st.checkbox("Display Dataset : "):
        number = st.number_input("Enter number of rows to view", 1, 25)
        if number >= 1 and number <= 25:
            st.write("Displaying dataframe : ")
            st.dataframe(df.head(number))

    # Display columns
    if st.checkbox("View column names : "):
        st.text("Displaying column names : ")
        st.write(df.columns)

    # Show shape
    if st.checkbox("Display dataset shape : "):
        st.text(f"Shape of dataset is : {df.shape}")
        # data_dim = st.radio("Select data dimension ", ("Rows", "Columns"))
        st.write(f"Number of rows is : {df.shape[0]}")
        st.write(f"Number of columns is : {df.shape[1]}")

    # Show specified columns
    if st.checkbox("Display selected columns : "):
        selected_columns = st.multiselect(
            "Select columns to display", df.columns.tolist())
        st.dataframe(df[selected_columns].head())

    # Show value counts
    if st.checkbox("Show Target value counts : "):
        st.text(
            f"Target :'{df.columns.tolist()[-1]}' value counts are as follows :")
        st.write(df.iloc[:, -1].value_counts())

    # Show datatypes
    if st.checkbox("Display data types : "):
        st.text("Data types of various columns")
        data_types = df.dtypes
        st.write(data_types)

    # describe dataset
    if st.checkbox("Display dataset summary : "):
        st.text("Dataset summary is as follows ")
        st.write(df.describe().transpose())

    # Plots and Visualizations
    st.subheader("Data Visualization (Customizable Plot)")

    # Pie Chart
    if st.checkbox("Pie Chart"):
        all_column_names = df.columns.tolist()
        selected_one_column = st.selectbox(
            "(Select columns to plot pie chart)", all_column_names)
        if st.button("Generate Pie Chart"):
            st.text("Generating Pie chart for selected fields")
            st.write(df[selected_one_column].value_counts().plot.pie(
                autopct="%1.1f%%"))

            st.pyplot()

    all_column_names = df.columns.tolist()

    st.subheader("More types of plots")
    type_of_plot = st.selectbox("Select type of plot", [
                                "area", "bar", "line", "hist", "box", "kde"])

    selected_columns_names = st.multiselect(
        "Select Columns To plot", all_column_names)

    if st.button("Click to generate plot"):
        st.success(
            f"Generate  '{type_of_plot}' plot for  {selected_columns_names}")

        if type_of_plot == "area":
            custom_data = df[selected_columns_names]
            st.area_chart(custom_data)

        elif type_of_plot == "bar":
            custom_data = df[selected_columns_names]
            st.bar_chart(custom_data)

        elif type_of_plot == "line":
            custom_data = df[selected_columns_names]
            st.line_chart(custom_data)

        # more custom plots
        else:
            custom_data_plot = df[selected_columns_names].plot(
                kind=type_of_plot)
            st.write(custom_data_plot)
            # st.pypolt()


if __name__ == "__main__":
    main()
