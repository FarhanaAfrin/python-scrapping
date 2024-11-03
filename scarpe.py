import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pdfkit
from urllib.parse import urlparse, urlunparse


class PDFGenerator:
    def __init__(self, chrome_driver_path, wkhtmltopdf_path):
        self.chrome_driver_path = chrome_driver_path
        self.wkhtmltopdf_path = wkhtmltopdf_path
        self.driver = self._init_driver()

    def _init_driver(self):
        """Initialize the Chrome WebDriver with headless options."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--window-size=1920x1080")  # Set window size
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")  # Set a user agent

        service = Service(executable_path=self.chrome_driver_path)
        return webdriver.Chrome(service=service, options=chrome_options)

    def extract_content_and_generate_pdf(self, current_url):
        """Fetches content and sub-URLs, generating PDFs accordingly."""
        self.driver.get(current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))  # wait for the main title
        )

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        # Extracting the title
        title = soup.title.string.strip()

        # Extracting the main content from the appropriate div
        content_div = soup.find('div', class_='col-xs-12 col-md-12 content-col')
        if content_div is None:
            print(f"No content found at {current_url}.")
            return []

        # Getting the text content
        content = content_div.get_text(strip=True)

        # Saving the main content PDF
        pdfkit.from_string(content, f'{title}.pdf', options={'quiet': '', 'enable-local-file-access': ''})

        # Check for sub-URLs in the table of contents
        sub_urls = self._get_sub_urls(soup, current_url)

        return sub_urls

    def _get_sub_urls(self, soup, current_url):
        """Extracts sub-URLs based on the current URL."""
        sub_urls = []
        parsed_url = urlparse(current_url)
        url_without_query = urlunparse(parsed_url._replace(query=''))

        for item in soup.select('.ecfr-table-of-contents .table-of-contents a'):
            link = "https://www.ecfr.gov" + item['href']
            if link.startswith(url_without_query):
                sub_urls.append(link)

        return sub_urls

    def extract_and_generate_pdf(self, base_url):
        """Processes the base URL and all its sub-URLs."""
        queue = [base_url]
        processed_urls = set()

        while queue:
            current_url = queue.pop(0)
            if current_url in processed_urls:
                continue

            processed_urls.add(current_url)

            # Extract content and get sub-URLs
            sub_urls = self.extract_content_and_generate_pdf(current_url)

            # Adding sub-URLs to the queue
            queue.extend(sub_urls)

        print("All URLs have been processed and PDFs generated.")

    def close_driver(self):
        """Closes the WebDriver."""
        self.driver.quit()


if __name__ == "__main__":
    chrome_driver_path = '/usr/bin/chromedriver'
    wkhtmltopdf_path = '/usr/bin/wkhtmltopdf'

    pdf_generator = PDFGenerator(chrome_driver_path, wkhtmltopdf_path)
    try:
        pdf_generator.extract_and_generate_pdf("https://www.ecfr.gov/current/title-12/chapter-I/part-2?toc=1")
    finally:
        pdf_generator.close_driver()
