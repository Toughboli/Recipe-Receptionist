import streamlit as st
import os
import subprocess
from backend import file_in,url_in,ask_question

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'output_question_list' not in st.session_state:
    st.session_state['output_question_list'] = []
if 'text_input_question' not in st.session_state:
    st.session_state['text_input_question'] = ""
if 'text_url_value' not in st.session_state:
    st.session_state['text_url_value'] = ""

def clear_uploads():
    for root, dirs, files in os.walk("uploads"):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
                
def process_input_question(input_text):
    print("asking question.")
    processed_text = ask_question(input_text)
    return processed_text


def process_file(uploaded_file):
    clear_uploads()
    try:
        save_directory = "uploads"
        file_extension = "." + uploaded_file.name.split(".")[-1]
        file_Name = "tempVideo" + file_extension
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        file_path = os.path.join(save_directory, file_Name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        file_in(file_path)
        st.session_state['video_processed'] = True
        
        return f"File processed:\nName: {uploaded_file.name}\nType: {uploaded_file.type}\nSize: {uploaded_file.size} bytes"

    except Exception as e:
        return f"An error occurred during file saving: {e}"

def process_url(text):
    clear_uploads()
    print("url submitted")
    url_in(text, "uploads", "tempVideo")
    st.session_state['video_processed'] = True
    
def update_answer_list():
    if st.session_state['output_question_list']:
        for processed_item in st.session_state['output_question_list']:
            st.write(f"- {processed_item}")


def reset_video_processed():
    st.session_state['video_processed'] = False
    
st.title("Recipe Receptionist")

input_option = st.radio(
    "Select Input Method:", 
    ("URL", "File Upload"), 
    key="input_method", 
    on_change=reset_video_processed
    )

if input_option == "File Upload":
    upload = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"], key="file_uploader") # Unique key
    if upload is not None:
        file_processing_result = process_file(upload)
        st.success(file_processing_result)

elif input_option == "URL":
    url = st.text_input(
        "Enter URL:",
        key="url_input",
        value=st.session_state['text_url_value']
    )
    if st.button("Submit URL", key="submit_url"):
        if url:
            process_url(url)
            st.session_state['text_url_value'] = ""
            
if 'video_processed' in st.session_state and st.session_state['video_processed']:
    user_input = st.text_input(
            "Enter Question:",
            key="question_input",
            value=st.session_state['text_input_question']
        )
    ask_button = st.button("Ask", key="ask_button")
    st.write("---")
    st.write("Processed Inputs:")
    
    if ask_button:
        if user_input:
            processed_text = process_input_question(user_input)
            st.session_state['output_question_list'].append(processed_text)
            st.success(f"Processed Text: {processed_text}")
            st.session_state['text_input_question'] = ""
            update_answer_list()
        else:
            st.warning("Please enter a question.")
            