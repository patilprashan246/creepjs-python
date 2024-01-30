# Web Scraping (https://abrahamjuliot.github.io/creepjs/)

This project consists of a Python script that performs web scraping using an API request and takes a screenshot of a web page using Selenium. It then generates a PDF of the webpage and saves the scraped data in JSON format.

## Installation

Before running the script, ensure you have Python installed on your system. Then, install the required packages using the following command:
pip install -r requirements.txt


## Usage

To run the script, use the following command:

python script.py


## The script performs the following actions:

1. Makes a POST request to a specified API to scrape data.
2. Extracts specific fields (`trustScore`, `lies`, `bot`, `fingerprint`) from the API response.
3. Saves the extracted data as JSON.
4. Takes a screenshot of the webpage 'https://abrahamjuliot.github.io/creepjs/'.
5. Generates a PDF of the webpage.
6. Repeats the process three times, generating three sets of JSON and PDF files.

## Output

The script generates the following files in its directory:

- `data_1.json`, `data_2.json`, `data_3.json`: JSON files containing scraped data.
- `screenshot_1.png`, `screenshot_2.png`, `screenshot_3.png`: Screenshots of the webpage.
- `page_1.pdf`, `page_2.pdf`, `page_3.pdf`: PDFs of the webpage screenshots.

## Notes

- Ensure that the Chrome WebDriver is installed and the path is correctly set in the script.
- The script logs its process in `scrape_log.txt`.

## Troubleshooting

If you encounter any issues, check the following:

- Ensure all requirements are correctly installed.
- Verify the path to Chrome WebDriver is correct.
- Check `scrape_log.txt` for any error messages logged by the script.

## Author

Prashant P


