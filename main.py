import streamlit as st
from parse import parse_ai
from scrape import scrape,extract_body,clean_body,split_dom

st.title("Ai WebScraper")
url = st.text_input("Enter a website Url")

if st.button("Scrape site"):
    result = scrape(url)
    body_content = extract_body(result)
    cleaned_content = clean_body(body_content)
    st.session_state.dom_content = cleaned_content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content , height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe content to parse")
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            dom_chunk = split_dom(st.session_state.dom_content)
            parsed_result = parse_ai(dom_chunk, parse_description)
            st.write(parsed_result)