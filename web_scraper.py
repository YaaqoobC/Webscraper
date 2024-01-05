import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import csv

# def get_product_price(url):
# #takes URL input --> feches HTML content and extracts product
# #price using BeautifulSoup
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
#     #mimicing a request from a windows chrom browser. This is for possibly abvoiding Detecton and blocking
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Update the HTML structure based on the specific website you're scraping
#     price_element = soup.find('span', {'class': 'a-price-whole'})
    

#     # Find all anchor elements containing book titles
#     ##title_elements = soup.find_all('a', {'title': True})

#     # Extract and print the text content of each title element
#     # titles = []
#     # for title_element in title_elements:
#     #     title = title_element.get_text(strip=True)
#     #     titles.append(title)
#     # if len(titles) > 0:
#     #     return titles 

#     if price_element:
#         return price_element.text.strip()
#     return 'Price not found'
        
# def write_to_textfile(text,current_date):
#     # Write the data to a text file
#     text_file_path = 'scraped_data_text.txt'
#     with open(text_file_path, 'a', encoding='utf-8') as textfile:
#     # Write the quote and scrape date to the text file
#             textfile.write(
#                  '================================================================'
#                  f'\nScrape Date: \n{current_date}\n'
#                  '----------------------------------------------------------------'
#                  f'\nScraped TEXT: \n{text}\n' 
#             )
#     print(f'Data written to: {text_file_path}')

# def write_to_CSVfile(text,current_date):
#     csv_file_path = 'scraped_data_csv.csv'
#     with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Scrape Date (Y/M/D)','Quote']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Check if the file is empty, and write header if needed
#         if csvfile.tell() == 0:
#             writer.writeheader()

#     # Write the quote and scrape date to the CSV file
#         writer.writerow({'Scrape Date (Y/M/D)': current_date,'Quote': text})
     

# current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# #fixes file directory to create in same folder
# script_directory = os.path.dirname(os.path.realpath(__file__))
# os.chdir(script_directory) 

# # url = 'http://books.toscrape.com/'
# url = 'https://www.amazon.ca/dp/B08H75RTZ8?ref_=Oct_DLandingS_D_128a425f_NA&th=1'
# print(get_product_price(url),current_date)

# def purchase_nike_shoe():
#     shoe_name = 'attack-white-and-yellow-ochre' 
#     size = '7'
#     html = load_nike_site(shoe_name)
#     select_size(html,size)
#     buy(html)

#     print(html)


# def load_nike_site(shoe_name):
#     url = f'https://www.nike.com/ca/launch/t/{shoe_name}'
#     # response = requests.get(url) 
#     # soup = BeautifulSoup(response.text, 'html.parser')
#     # main_container = soup.find('div', {'class': 'pdp-container-inner' })
#     # sections = main_container.findChildren('section', recursive=False)
#     # first_section = sections[0]
#     # buttons = first_section.find_all('aside')[0].find_all('button')

#     # print(len(buttons))
#     # for button in buttons:
#     #     print(button.text)
#     # print("heree==============================================================================r \n")
#     # #print(buy_button)
#     # #return buy_button


#     chrome_options = Options()
#     chrome_options.add_argument('--headless')  # Run the browser in headless mode (without GUI)
#     driver = webdriver.Chrome('./chromedriver', options=chrome_options)


#     try:
#         driver.get(url)
#         page_source = driver.page_source
#     finally:
#         driver.quit()

#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Update the HTML structure based on the specific website you're scraping
#     price_element = soup.find('span', {'class': 'price'})  # Replace with the actual HTML element and class

#     if price_element:
#         return price_element.text.strip()
#     else:
#         return 'Price not found'


def select_size(html,size):
    pass
def buy(html):
    pass

#purchase_nike_shoe()
def load_nike_site(shoe_name):
    url = f'https://www.nike.com/ca/launch/t/{shoe_name}'

    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run the browser in headless mode (without GUI)
    driver = webdriver.Chrome('./chromedriver', options=chrome_options.options)



    try:
        driver.get(url)
        page_source = driver.page_source
    finally:
        driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

def purchase_nike_shoe():
    shoe_name = 'attack-white-and-yellow-ochre' 
    soup = load_nike_site(shoe_name)

    # Now you can continue with scraping or interacting with the page using BeautifulSoup
    # For example, find the price element:
    price_element = soup.find('button', {'class': 'ncss-btn-primary-dark btn-lg  buying-tools-cta-button '})
    
    if price_element:
        print(f'Price: {price_element.text.strip()}')
    else:
        print('Price not found')

purchase_nike_shoe()


