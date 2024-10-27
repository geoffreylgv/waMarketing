# WhatsApp Message Automation Script

This Python script automates sending messages to WhatsApp contacts using data from an Excel file. It uses Selenium to open and control WhatsApp Web in a browser and pandas to read the Excel file containing contact details.

## Prerequisites
* Python 3.6+ is required.
* Chrome Browser (or another browser compatible with Selenium).
* ChromeDriver (or corresponding WebDriver for the browser used).
* Setup and Installation
* Clone the Repository (or download the script):

## Setup and installation
1. Clone the repository

```bash
git clone https://github.com/geoffreylgv/wa.git
cd waMarketing
```

2. Install the Required Python Libraries:

To install all necessary dependencies, run:

```bash
pip install -r requirements.txt
```

3. Download WebDriver:

* **Chrome Users:** Download the latest version of ChromeDriver from ChromeDriver - WebDriver for Chrome and add it to your system PATH or specify its location in the script.
* **Other Browsers:** Refer to Selenium’s WebDriver documentation to download the appropriate driver for your browser.

## Usage
1. Prepare Your Excel File:

* Ensure your Excel file is formatted with the columns ```Name```, ```Message```, and ```Number``` (the international format is preferred for numbers).
* Save your file as ```clients.xlsx``` in the same directory as the script or specify the file path in the code.

2. Run the Script:

```bash
python waMarketing.py
```
* The script will open WhatsApp Web in a browser window.
* You will need to scan the QR code on WhatsApp Web to log in (the script will wait for some seconds).
* Once logged in and you have your chat interface, hit enter (keyboard Enter)
* Message box will prompt and you'll need to click on send button to send the message, all this loaded from the specified Excel file.

## File Structure

```bash
waMarketing/
├── requirements.txt
├── clients.xlsx       # Excel file with contact information (example)
└── waMarketing.py  # Main script
```

## Example Excel File
|name	|message	|number|
|:-------|:-------|:-------|
|Alice	|Hello Alice, this is a message!	|233593888888|
|Geoffrey	|Hi, sorry another message!	|22898776682|

## Troubleshooting
* Login Timeout: If you need more time to log in, adjust the time.sleep() duration in the script after opening WhatsApp Web.
* WebDriver Issues: Ensure that the WebDriver version matches your browser version. If issues persist, try updating both your browser and WebDriver.

## Requirements
* pandas
* selenium
* openpyxl
* xlrd

## License
> [!NOTE] 
> This project is open source and freely available under the GNU GPL V3. <br> Help giving a star to the project and get your hands dirty by contributing to it, having the send feature automatically without clicking on any button. Feel free to submit a pull request or start a discussion to share your ideas.
