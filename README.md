# python-scrapping
Scrape the contents from the content section of the base URL and all sub-URLs into separate PDF files

# PDF Generator using Selenium and BeautifulSoup

This Python script utilizes Selenium WebDriver to scrape web content and generate PDF documents using the `pdfkit` library. The application is designed to run in headless mode for efficiency.

## Features

- Web scraping using Selenium and BeautifulSoup.
- PDF generation using `pdfkit`.
- Headless browser support for scraping without a GUI.

## Requirements

- Python 3.x
- Chrome WebDriver
- wkhtmltopdf

## Installation

1. **Clone the repository** or download the script.
2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt

3. **Set up ChromeDriver**:

- Download the appropriate version of ChromeDriver from ChromeDriver based on your installed version of Chrome.
- Place the chromedriver executable in a directory included in your system's PATH or specify its path in the script.

4. **Install wkhtmltopdf**:

- Download and install wkhtmltopdf from wkhtmltopdf.
- Make sure to set the path to the wkhtmltopdf executable in the script.

5. To run the script, execute the following command:
    ```
    python3 scarpes.py
    ```