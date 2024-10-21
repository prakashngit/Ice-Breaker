from dotenv import load_dotenv
load_dotenv()
from linkedin_dataprocessing_outputparser import ice_beak_with

import streamlit as st
import requests


st.title("Profile Finder")

name = st.text_input("Enter Name of person to lookup")

if st.button("Loop Up!"):
    if name:
        res, photo_url = ice_beak_with(name)
        res_dict = res.to_dict()
        summary = res_dict["summary"]
        facts = res_dict["facts"]
        
        if photo_url:
            try:
                response = requests.get(photo_url)
                if response.status_code == 200:
                    st.image(response.content)
                else:
                    st.warning("Unable to fectch profile photo")
            except Exception as e:
                st.error("Error fetching photo {}".format(e))
        else:
            st.info("No profile photo available")
        
        st.header("Summary")
        st.write(summary)

        st.header("Interesting Facts")
        st.write("1. " + facts[0])
        st.write("2. " + facts[1])
    else:
        st.write("Please enter name First")    
