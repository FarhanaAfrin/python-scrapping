# python-scrapping

A FastAPI application that scrapes content from a base URL and its sub-URLs into PDF files, only downloading new content when updates are detected. This project utilizes Selenium WebDriver, BeautifulSoup, and pdfkit, with PostgreSQL as the database.

## Features

- **Web Scraping**: Uses Selenium and BeautifulSoup to scrape the main content section of a web page.
- **PDF Generation**: Converts scraped HTML content into PDF format with `pdfkit`.
- **Update Checking**: Only downloads new content if an update is detected, using a content hash for efficient change tracking.
- **Background Processing**: Runs scraping as a background task with FastAPI, with optional support for scheduling checks.
- **PostgreSQL Database**: Stores task information, including status, PDF paths, content hash, and timestamps.

## Requirements

- Python 3.x
- FastAPI
- PostgreSQL
- Chrome WebDriver
- wkhtmltopdf

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/python-scrapping
   cd python-scrapping
   ```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:

Create a config file in the root directory:

```
DATABASE_URL=postgresql://username:password@localhost/dbname
CHROME_DRIVER_PATH=/path/to/chromedriver
WKHTMLTOPDF_PATH=/path/to/wkhtmltopdf
```
Replace username, password, localhost, and dbname with your PostgreSQL details.

5. **Set up ChromeDriver**:

Download the appropriate version of ChromeDriver from ChromeDriver based on your installed version of Chrome.
Place the chromedriver executable in a directory included in your system's PATH or specify its path in the .env file.
Run Redis (optional):


6. **Running the Application**:
Start the FastAPI server:
Run the following command to start the server:

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```