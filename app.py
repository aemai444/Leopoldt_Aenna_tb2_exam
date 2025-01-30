import streamlit as st
from page_definitions2 import main_page
from page_definitions2 import contact_page
from page_definitions2 import AI_page
from page_definitions2 import checkbox_page
from page_definitions2 import information_page
from page_definitions2 import faq_page

# set up the page
st.set_page_config(page_title="SupportCircle")

options = ["Mainpage", "Contacts", "Checkbox", "Information", "Your AI assistant", "FAQ"]
page_selection = st.sidebar.selectbox("Menu", options)


if page_selection == "Mainpage":
    main_page()
elif page_selection == "Contacts":
    contact_page()
elif page_selection == "Checkbox":
    checkbox_page()
elif page_selection == "Information":
    information_page()
elif page_selection == "Your AI assistant":
    AI_page()
elif page_selection == "FAQ":
    faq_page()


