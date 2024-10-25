from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver (Chrome)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find the search box using its name attribute (Google's search box has the name 'q')
search_box = driver.find_element("name", "q")

# Type a search query related to tomato crop (e.g., 'tomato crop management')
search_box.send_keys("tomato crop management")

# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to let the results load (optional)
driver.implicitly_wait(5)

# Close the browser
driver.quit()
