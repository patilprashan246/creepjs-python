import json
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from fpdf import FPDF

# Define the log file path
log_file_path = 'scrape_log.txt'

def log(message):
    """
    Function to append logs to a file.
    :param message: The message to log.
    """
    timestamp = datetime.now().isoformat()
    with open(log_file_path, 'a') as file:
        file.write(f"{timestamp} - {message}\n")

def log_error(error, iteration):
    """
    Function to log errors with a specific iteration context.
    :param error: The error object.
    :param iteration: The iteration number during which the error occurred.
    """
    log(f"Error in iteration {iteration}: {str(error)}")

def scrape_api_data(iteration):
    """
    Makes a POST request to the specified API with given payload and headers.
    """
    url = "https://creepjs-api.web.app/fp"

    payload = json.dumps([
        "KANg440lYwnldNxxD90co6yGygzvOelD4g3mB7mRquyvKL/FTXtiY6jp32B1zATKySTVTJ4k4KDUtzX6fS/Y3bbh0UZ5nG+H3Mp95C/TP8asRP7VMMI54W9pHKbYfeMd9pyndpQucm52jFyYN0eGj8CvF1n2Jy5WnQT+0UmIMY5cqfKDB3cAxHMtIaniHbDcTJI79qaKBx2kKxv1eP94yDAaThW7A9qTOLptgz+KF88hH0zm7os9ZfI6NBwMB6l342vQwNsio++njba/8MFK4wc48ZB4KAEVyTnQdJWh0tRTZwX9/8dByqGSydphk8v5XPL2BEdrw/8aNiRCqIdBSv4mJJzOR5ucnyLzu94iFcXx15vDF6xz+q1NzrxQ4Wq5RJAvkXbXESho+73FYzb9zkJhFFXF3MLQ4vH24fzZBFmqT5Od6phqp7ysaDSZFwVpnk0Rk5Xl86ZrbhIIii6abD+Zxgt3X7rLOVUsJbrrk9hOfx03FaudOzPNBJYl6jH50v6uAs+/eSjh4+KJysjAgKT7BFcXN0N1vK7+sJ/lZT4neDnMKlhc9OYs1qAXbVpRO7flZbEy5AKJu5s0TP7YZgmXjotyEKAAVqVgg1/W7CmS9oGmc/Q94Ki4KrXzsNzPE7Xl4BusqTRpGpClyOeBO2ptLJRY8zaA/VfOkOQLdf1US6//r2jrY9hslNothaRzERSToftiAZ1CcVEddbzDL31C4RPe/3G/stqmMiYKm/apcY+k2dBO2s50Y0lPTnDRuSfZnJ3ik8APCV0=",
        "PNVSeBn1OwYN6aCB",
        "hLxp01uh2mabENxp3hFuYgQW9ZTH2hKvI_hoN9ODj6c"
    ])
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '853',
        'Content-Type': 'application/json',
        'Origin': 'https://abrahamjuliot.github.io',
        'Referer': 'https://abrahamjuliot.github.io/',
        'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    log(f"API request for iteration {iteration} completed.")

    # Extract specific fields from the response
    data_to_save = {
        'trustScore': response.json().get('score'),
        'lies': response.json().get('hasLied'),
        'bot': response.json().get('bot'),
        'fingerprint': response.json().get('fingerprint')
    }

    # Save the extracted data as JSON
    with open(f'data_{iteration}.json', 'w') as file:
        json.dump(data_to_save, file)
    log(f"Selected API data for iteration {iteration} saved as JSON.")

def generate_screenshot_and_pdf(iteration):
    """
    Takes a screenshot of a webpage and generates a PDF.
    :param iteration: The current iteration number.
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    service = Service('chromedriver.exe')  # Specify the correct path to chromedriver
    browser = webdriver.Chrome(service=service, options=options)

    try:
        log(f"Iteration {iteration} started.")

        # Navigate to the target page
        browser.get('https://abrahamjuliot.github.io/creepjs/')
        time.sleep(2)
        screenshot_path = f"screenshot_{iteration}.png"
        browser.save_screenshot(screenshot_path)
        log(f"Screenshot for iteration {iteration} saved.")

        # Convert page to PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = "Screenshot for Iteration: " + str(iteration), ln = True, align = 'C')
        pdf.image(screenshot_path, x = 10, y = 20, w = 180)
        pdf.output(f"page_{iteration}.pdf")
        log(f"PDF for iteration {iteration} created.")

    except Exception as e:
        log_error(e, iteration)
    finally:
        browser.quit()

def main():
    """
    Main function to control the flow of iterations and make an API request.
    """
    for i in range(1, 4):
        scrape_api_data(i)
        generate_screenshot_and_pdf(i)

if __name__ == "__main__":
    main()
