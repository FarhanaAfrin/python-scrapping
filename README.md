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


## ChromeDriver Setup

To download the ChromeDriver and set it up for use, follow these steps:

### Download ChromeDriver
1. **Check Your Chrome Version**:
   - Open Google Chrome.
   - Click on the three dots in the top right corner to open the menu.
   - Go to **Help** > **About Google Chrome**. This will display your current Chrome version.

2. **Download ChromeDriver**:
   - Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads).
   - Find the version that matches your Chrome version and download the appropriate driver for your operating system (Windows, Mac, or Linux).

### Setting Up the ChromeDriver Path
1. **Extract the Driver**:
   - After downloading, extract the `chromedriver` executable from the ZIP file.

2. **Set the Path**:
   - **Windows**:
     - Move the `chromedriver.exe` to a location of your choice (e.g., `C:\Program Files\ChromeDriver`).
     - Open the Start Menu and search for "Environment Variables."
     - Click on "Edit the system environment variables."
     - In the System Properties window, click the **Environment Variables** button.
     - In the System Variables section, find the **Path** variable and select it, then click **Edit**.
     - Click **New** and add the path where you placed the `chromedriver.exe` (e.g., `C:\Program Files\ChromeDriver`).
     - Click **OK** to close all dialog boxes.

   - **Mac/Linux**:
     - Move the `chromedriver` executable to `/usr/local/bin/`:
       ```bash
       sudo mv /path/to/chromedriver /usr/local/bin/
       ```
     - Make it executable:
       ```bash
       sudo chmod +x /usr/local/bin/chromedriver
       ```

3. **Verify the Installation**:
   - Open a terminal or command prompt and type:
     ```bash
     chromedriver --version
     ```
   - This should display the version of ChromeDriver you installed, confirming that it is correctly set up.

#### Additional Notes
- Ensure that your version of ChromeDriver matches the version of Google Chrome you have installed to avoid compatibility issues.
- You may need to restart your terminal or command prompt for the changes to take effect.


## wkhtmltopdf Setup

To install and set up wkhtmltopdf, follow these steps:

### Download wkhtmltopdf
1. Go to the [wkhtmltopdf download page](https://wkhtmltopdf.org/downloads.html).
2. Choose the appropriate version for your operating system (Windows, Mac, or Linux) and download the installer.

### Installation Instructions
- **Windows**:
  - Run the downloaded installer and follow the installation prompts.
  - During installation, note the installation directory, as you will need to add it to your system's PATH.

- **Mac**:
  - You can install wkhtmltopdf using Homebrew:
    ```bash
    brew install wkhtmltopdf
    ```

- **Linux**:
  - For Debian/Ubuntu-based systems, you can install it via:
    ```bash
    sudo apt-get install wkhtmltopdf
    ```
  - For RedHat/CentOS-based systems, you can use:
    ```bash
    sudo yum install wkhtmltopdf
    ```

### Set up the Path
- After installation, ensure that the path to the wkhtmltopdf executable is set in your script. If installed correctly, you should be able to run the following command to check the version:
  ```bash
  wkhtmltopdf --version
  ```