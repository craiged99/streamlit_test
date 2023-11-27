import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Specify a fixed Chrome browser version
chrome_version = "94.0.4606.61"  # You can update this to the appropriate version

@st.experimental_singleton
def get_driver():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    # Specify the Chrome browser version when creating the driver
    driver_path = ChromeDriverManager(chrome_version=chrome_version).install()
    return webdriver.Chrome(service=Service(driver_path), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get('http://example.com')

st.code(driver.page_source)

driver.quit()  # Make sure to quit the driver when done
