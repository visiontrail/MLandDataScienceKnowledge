import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Install necessary libraries (if needed)
# !mamba install bs4==4.10.0 -y
# !mamba install html5lib==1.1 -y 
# !pip install lxml==4.6.4

# URL for Netflix data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# Step 1: Send an HTTP request to the web page
data = requests.get(url).text

# Step 2: Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

# Step 3: Identify the HTML tags and create an empty DataFrame
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Step 4: Use BeautifulSoup methods to extract data
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Append the data of each row to the DataFrame
    netflix_data = pd.concat([netflix_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

# Step 5: Print the extracted data
print(netflix_data.head())

# Extracting data using `pandas` library
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head())

# Exercise: use webscraping to extract stock data
# URL for Amazon data
url_amazon = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data_amazon = requests.get(url_amazon).text
print(data_amazon)

# Parse the html data using BeautifulSoup
soup_amazon = BeautifulSoup(data_amazon, 'html.parser')
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Extract data and build the DataFrame
for row in soup_amazon.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

# Print the first five rows of the `amazon_data` DataFrame
print(amazon_data.head())