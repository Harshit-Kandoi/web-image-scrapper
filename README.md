# 🖼️ Image Extractor

This project is a Python-based tool to extract and download images from:

1. **Any URL with infinite scroll/image-based content** (like Google Images, Pinterest, etc.)
2. **Pexels.com** using their developer-friendly API (via `extra.py`)

---

## 📁 Project Structure
image-extracter/
├── .venv/ # Python virtual environment

├── images/ # Downloaded images from main script

├── pexels_images/ # Downloaded images from Pexels API

├── extra.py # Pexels image downloader

├── main.py # General image extractor (uses Selenium)

├── pyproject.toml # Project dependencies

├── README.md # You're reading it!

└── uv.lock # Lock file for dependencies


---

## 🚀 Features

### `main.py`
- Extracts images from dynamically loaded pages using Selenium.
- Automatically continues from the last downloaded image (doesn't overwrite).
- Can scroll and click through pages (if pagination exists).
- Works on most websites with image elements.

### `extra.py`
- Uses the **Pexels API** to fetch high-quality stock images.
- Requires a valid [Pexels API key](https://www.pexels.com/api/).
- Images are saved in a separate `pexels_images/` folder.

---

## 🛠️ Setup Instructions

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/image-extracter.git
cd image-extracter
```

2. **Create and activate a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the image extractors**

### 'For general image scraping:'
```bash
python main.py
```

### 'For Pexels scraping:'

```bash
python extra.py
```

---

## ⚠️ Proxy Support (Optional but Recommended)
If you're scraping a high volume of images or running the script frequently, some websites may block your IP address. In such cases, it's highly recommended to use rotating proxies.

### 'When to use a proxy:'
- Getting blocked, captchas, or 403 errors
- Running the script continuously
- Scraping from websites like Google Images, Pinterest, etc.

### 'How to enable proxy (planned):'
Proxy support can be added using selenium-wire or by configuring ChromeOptions to use a proxy server.

Let me know if you’d like proxy integration added!

---

## 🔑 Pexels API Key
For extra.py, create a .env file and store your API key like this:
```ini
PEXELS_API_KEY=your_api_key_here
```

---

## 📸 Example Output
### 'Images are saved in respective folders:'
- General scrape: images/
- Pexels API: pexels_images/

---

📃 License
MIT License — Feel free to use and modify.