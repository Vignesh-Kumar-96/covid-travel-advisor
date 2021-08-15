from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
origin = "VOBL"
destination = "OTHH"
url = "https://flightaware.com/live/findflight?origin=" + origin + "&destination=" + destination
driver.get(url)

flights = []
try:
    results_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Results"]')))
    rows = results_table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 0:
            flight = []
            for col in cols:
                flight.append(col.text)
            flights.append(flight)
except Exception as e:
    print(e)
    print("Unable to get results")

print(flights)
driver.close()
