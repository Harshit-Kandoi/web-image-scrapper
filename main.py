import os
import time
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

SAVE_DIR = "images"
IMAGE_LIMIT = 50  # Total number of images you want to download

# Ensure the folder exists
os.makedirs(SAVE_DIR, exist_ok=True)

# Get all existing images
def get_existing_images():
    return set(os.listdir(SAVE_DIR))

# Get max index to continue from last image
def get_start_index(existing_images):
    max_index = -1
    pattern = re.compile(r"image_(\d+)\.jpg")
    for name in existing_images:
        match = pattern.match(name)
        if match:
            idx = int(match.group(1))
            if idx > max_index:
                max_index = idx
    return max_index + 1

# Extract image URLs from current page
def get_image_urls(driver):
    time.sleep(2)  # Let the page load images
    urls = set()

    # Re-fetch elements and extract their src in the same loop to avoid stale references
    images = driver.find_elements(By.TAG_NAME, "img")
    for i in range(len(images)):
        try:
            # Fetch the image again by index
            images = driver.find_elements(By.TAG_NAME, "img")
            src = images[i].get_attribute("src")
            if src and src.startswith("http"):
                urls.add(src)
        except Exception as e:
            print(f"Error fetching image {i}: {e}")
            continue

    print(f"Found {len(urls)} image URLs on the page.")
    return list(urls)


# Download images, continuing from last index
def download_images(image_urls, existing_images, start_index, limit=IMAGE_LIMIT):
    count = 0
    image_index = start_index
    for url in image_urls:
        if count >= limit:
            break
        img_name = f"image_{image_index}.jpg"
        if img_name not in existing_images:
            try:
                img_data = requests.get(url).content
                with open(os.path.join(SAVE_DIR, img_name), 'wb') as f:
                    f.write(img_data)
                print(f"Downloaded {img_name}")
                existing_images.add(img_name)
                image_index += 1
                count += 1
                time.sleep(0.3)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

# Setup Selenium
options = Options()
options.add_argument("--headless")  # Optional: Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://unsplash.com/s/photos/plastic-trash")  # Replace with your actual target URL

# Initialization
existing_images = get_existing_images()
start_index = get_start_index(existing_images)
total_downloaded = len(existing_images)
page_number = 1

# Main loop for scraping
while total_downloaded < IMAGE_LIMIT:
    print(f"Scraping Page {page_number}...")
    image_urls = get_image_urls(driver)
    before_download = len(existing_images)
    download_images(image_urls, existing_images, start_index, limit=IMAGE_LIMIT - total_downloaded)
    after_download = len(existing_images)
    total_downloaded = after_download
    start_index = get_start_index(existing_images)

    # Try to click next
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a[rel="next"], button[aria-label="Next"]')
        print("Clicking next page...")
        next_button.click()
        time.sleep(2)
        page_number += 1
    except (NoSuchElementException, ElementNotInteractableException):
        print("No more pages or can't click next. Exiting...")
        break

print(f"Reached image limit of {IMAGE_LIMIT} images.")
driver.quit()
