import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- Settings ---
SEARCH_TERM = "nature"
SAVE_DIR = "pexels_images"
NUM_SCROLLS = 5  # Number of times to scroll down to load more images
IMAGE_LIMIT = 25  # Limit to how many images you want to download
NUM_PAGES = 3  # Number of pages to scrape

# --- Create Save Directory ---
os.makedirs(SAVE_DIR, exist_ok=True)

# --- Function to Check Already Downloaded Images ---
def get_existing_images():
    existing_images = set()
    for file_name in os.listdir(SAVE_DIR):
        if file_name.endswith('.jpg'):
            existing_images.add(file_name)
    return existing_images

# --- Setup Chrome ---
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
options.add_argument('--start-maximized')  # Open in maximized window

# Use headless mode if needed
# options.add_argument('--headless')  # Uncomment to make it invisible

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- Function to Scrape Images from Current Page ---
def scrape_images():
    image_elements = driver.find_elements(By.TAG_NAME, 'img')
    image_urls = set()
    for img in image_elements:
        src = img.get_attribute('src')
        if src and "images.pexels.com" in src:
            image_urls.add(src)
    return image_urls

# --- Download Images Function ---
def download_images(image_urls, existing_images, limit=IMAGE_LIMIT):
    count = 0
    for idx, url in enumerate(image_urls):
        if count >= limit:
            break
        # Construct image filename
        img_name = f"image_{len(existing_images) + count}.jpg"
        if img_name not in existing_images:
            try:
                img_data = requests.get(url).content
                with open(os.path.join(SAVE_DIR, img_name), 'wb') as f:
                    f.write(img_data)
                print(f"Downloaded {img_name}")
                count += 1
                existing_images.add(img_name)  # Add to existing images to avoid duplicates
                time.sleep(0.3)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

# --- Open Pexels Search Page ---
driver.get(f"https://www.pexels.com/search/{SEARCH_TERM}/")
time.sleep(3)

# --- Get Already Existing Images ---
existing_images = get_existing_images()
downloaded = len(existing_images)  # Set the initial downloaded count

# --- Loop to Scrape Images from Multiple Pages ---
for page in range(1, NUM_PAGES + 1):
    print(f"Scraping Page {page}...")
    image_urls = scrape_images()
    download_images(image_urls, existing_images, limit=IMAGE_LIMIT - downloaded)
    
    # Update downloaded count
    downloaded = len(existing_images)
    
    # Stop if we've reached the image limit
    if downloaded >= IMAGE_LIMIT:
        print(f"Reached image limit of {IMAGE_LIMIT} images.")
        break

    # Scroll before clicking the Next button to ensure visibility
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Wait for the "Next" button to be clickable and then click it
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@rel='next']"))  # Update this XPath if needed
        )
        driver.execute_script("arguments[0].scrollIntoView();", next_button)  # Scroll to the "Next" button
        next_button.click()
        time.sleep(3)
    except Exception as e:
        print(f"Failed to click next page: {e}")
        break

# --- Cleanup ---
driver.quit()
print("Scraping completed.")