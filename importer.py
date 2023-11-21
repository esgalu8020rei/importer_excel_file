import streamlit as st
import pandas as pd
import zipfile

st.title("Importer")

file_zip = st.file_uploader("Choose a file")

if file_zip is not None:

    file = zipfile.ZipFile(file_zip)
    list_files = file.namelist()

    df = {}

    for file_name in list_files:
        df[file_name] = pd.read_excel(file.open(file_name).read())
        df[file_name]["FILE_NAME"] = file_name

    df = pd.concat(df.values())

    st.write(f"Cantidad de registros {len(df)}")

    st.write("Ejemplo del archivo")
    st.write(df.head())
