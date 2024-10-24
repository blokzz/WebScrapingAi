import streamlit as st
from scrape import scrape_website
st.title("AI web scraper")
url = st.text_input("Enter a website Url")

if st.button("Scrape site"):
    result = scrape_website(url)
    print(result)
