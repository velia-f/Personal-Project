import re
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome options with headless mode enabled
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

CACHE_FILE = "analyzed_links.txt"

def load_cache():
    """Load previously analyzed links from the cache file."""
    try:
        with open(CACHE_FILE, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def save_to_cache(link):
    """Save a link to the cache file."""
    with open(CACHE_FILE, "a") as file:
        file.write(link + "\n")

def get_similar_links(base_url):
    """Extract all links that start with 'https://www.vinted.it/items/' from the base URL."""
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load completely

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith("https://www.vinted.it/items/"):
            links.append(href)

    return list(set(links))  # Remove duplicates

def extract_shipping_price(link):
    """Visit the link and extract the shipping price."""
    driver.get(link)
    time.sleep(2)  # Wait for the product page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    shipping_price = None
    shipping_price_tag = soup.find('h3', {'data-testid': 'item-shipping-banner-price'})
    
    if shipping_price_tag:
        price_text = shipping_price_tag.text.strip()
        match = re.search(r"([0-9]+,[0-9]+)", price_text)

        if match:
            shipping_price = float(match.group(1).replace(",", "."))
            print(f"Shipping from: {shipping_price}")
        else:
            print("No shipping cost found.")
    return shipping_price

def main():
    base_url_template = ("https://www.vinted.it/catalog?search_text=braccialetto&search_id=19549334615"
                         "&order=newest_first&time=1735069126&price_to=15&currency=EUR&page={page}"
                         "&status_ids[]=4&status_ids[]=3&status_ids[]=2&status_ids[]=6&status_ids[]=1")

    print("Loading cache...")
    analyzed_links = load_cache()

    valid_links = []
    max_shipping_price = 2.99  # Max price for shipping that we are interested in
    link_counter = 1  # Initialize the link counter

    # Loop through the first 5 pages
    for page in range(1, 6):
        base_url = base_url_template.format(page=page)
        print(f"\nExtracting links from page {page}...")
        similar_links = get_similar_links(base_url)

        print(f"Found {len(similar_links)} similar links on page {page}.")

        for link in similar_links:
            print(f"\n{link_counter}) Analyzing link: {link}")

            if link in analyzed_links:
                print("\nAlready analyzed.")
                link_counter += 1
                continue

            shipping_price = extract_shipping_price(link)
            if shipping_price is not None:
                if shipping_price <= max_shipping_price:
                    valid_links.append(link)
                    print(f"Valid (<= {max_shipping_price}) shipping price found: {shipping_price}")
                    webbrowser.open(link)
            else:
                print("No valid shipping price found.")

            save_to_cache(link)
            analyzed_links.add(link)  # Avoid duplicates in the same run
            link_counter += 1

    print("\nLinks with shipping price less or equal than {:.2f}:".format(max_shipping_price))
    for valid_link in valid_links:
        print(valid_link)

if __name__ == "__main__":
    main()

driver.quit()
