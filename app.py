# --------------------------------------------------------------------
#  waMarketing : IndabaX Togo automation tool to send bulk WhatsApp message
# --------------------------------------------------------------------

import pandas as pd
from time import sleep
from urllib.parse import quote
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Load data from Excel
data = pd.read_excel('clients.xlsx', sheet_name='Sheet0')
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
input("Press ENTER after logging into WhatsApp Web and when your chats are visible.\n\n\n")

# Loop through the contacts in the Excel file
for index, row in data.iterrows():
    name = row.get("Name")
    message = row.get("Message")
    number = row.get("Number")
    
    # Check if number and message exist
    if pd.isna(number) or pd.isna(message):
        print(f"Skipping row {index + 1}: Missing number or message.")
        continue
    
    # URL encode the message for safe URL usage
    encoded_message = quote(str(message))
    url = f'https://web.whatsapp.com/send?phone={str(number)}&text={encoded_message}'
    
    try:
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the message box to load
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='conversation-compose-box-input']"))
        )
        
        js_executor = driver.execute_script("return arguments[0]", message_box)

        # Simulate Enter key press using JavaScript
        js_executor.send_keys(Keys.ENTER)

        print(f'Message sent to: {number}\n')
        
        sleep(5)
    
    except Exception as e:
        print(f"Failed to send message to {number}\n")

# Close WebDriver after sending all messages
driver.quit()
print("The script executed successfully.\n")
