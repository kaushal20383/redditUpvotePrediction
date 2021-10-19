# pip install streamlit
import streamlit as st
from model import predict_upvote
from sentiment import cal_polarity
from link_process import extract_features, valid_post
import numpy as np

st. set_page_config(page_title="Predicting the Popularity of Reddit Posts App", page_icon="***", layout ="wide")

with st.form("prediction_form"):
    st.header("Enter the Reddit Post Link: ")
    post_link = st.text_input('Link: ', value='')

    submit_val = st.form_submit_button('Predict Upvote')

if submit_val:    
    attribute = post_link
    if valid_post(post_link):
      
        x_test = extract_features(post_link)
        x_test = [int(x_test[0]), x_test[1], x_test[2]]
        x_test = np.array(x_test).reshape(1,-1)
        value = predict_upvote(attributes = x_test)

        #st.header(f'Link: {attribute}')
        st.header("Result: ")
        st.success(f'The predicted upvote is {int(value)}')
    else:
        st.header("Input valid post link")
        st.success('Wrong post link')
    