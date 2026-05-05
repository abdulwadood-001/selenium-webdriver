from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome in headless mode (important for Jenkins)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open a simple website
    driver.get("https://example.com")

    # Check page title
    assert "Example Domain" in driver.title

    print("Received!")

finally:
    driver.quit()
