import streamlit as st
from scrape import scrape_website , split_dom_content , clean_body_content , extract_body_content
st.title("AI web scraper")
url = st.text_input("Enter a website Url")

if st.button("Scrape site"):
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_conent = cleaned_content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content , height=300)
    
    if "dom_content" in st.session_state:
        parse_description = st.text_area("Descripe")

        if st.button("parse"):
            if parse_description:
                st.write("parsing")

                dom_chunks = split_dom_content(st.session_state.dom_content)
                