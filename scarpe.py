import hashlib
from sqlalchemy.orm import Session
from models import Task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pdfkit
import os
import logging
from datetime import datetime
from config import CHROME_DRIVER_PATH

class PDFGenerator:
    def __init__(self):
        self.driver = None
        os.makedirs("pdfs", exist_ok=True)

    def __enter__(self):
        """Initialize the Chrome WebDriver with headless options."""
        self.driver = self._init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure WebDriver is closed on exit."""
        if self.driver:
            self.driver.quit()

    def _init_driver(self):
        """Private method to initialize WebDriver with options."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        service = Service(executable_path=CHROME_DRIVER_PATH)
        return webdriver.Chrome(service=service, options=chrome_options)

    def generate_pdf(self, content, title):
        """Generates a PDF from HTML content."""
        pdf_path = f"pdfs/{title}.pdf"
        pdfkit.from_string(content, pdf_path, options={"quiet": "", "enable-local-file-access": ""})
        return pdf_path

    def extract_content_and_generate_pdf(self, task: Task, db: Session):
        """Fetches content from the URL, checks for changes, and generates a PDF if updated."""
        try:
            self.driver.get(task.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            # Extract content and calculate hash
            content_div = soup.find('div', class_='col-xs-12 col-md-12 content-col')
            content = content_div.get_text(strip=True) if content_div else ""
            current_hash = hashlib.md5(content.encode('utf-8')).hexdigest()

            # Check if content has changed by comparing hashes
            if task.content_hash == current_hash:
                logging.info("No updates detected.")
                return  # Exit if content hasn't changed

            # Content has changed, generate a new PDF
            title = soup.title.string.strip() if soup.title else "untitled"
            pdf_path = self.generate_pdf(content, title)
            task.result_path = pdf_path
            task.content_hash = current_hash
            task.updated_at = datetime.utcnow()
            task.status = "completed"
            logging.info("Content updated, new PDF saved at %s", pdf_path)

        except Exception as e:
            task.status = "failed"
            print(f"Error processing {task.url}: {e}")
        finally:
            db.commit()
