# 🖼️ Web Image Scraper

A powerful Python-based tool for extracting and downloading images from various web sources. This project is specifically designed for creating datasets for machine learning applications, particularly for visual recognition tasks.

## 📊 Dataset Created

This project was used to create the **[Visual Plastic Type Recognition Dataset](https://www.kaggle.com/datasets/harshitkandoi7850/dataset-for-visual-plastic-type-recognition)** on Kaggle.

### 🎯 Dataset Uses
The collected images are specifically curated for:
- **Computer Vision Models**: Training deep learning models for plastic type classification
- **Environmental AI**: Developing AI systems for waste sorting and recycling
- **Research Applications**: Academic studies on plastic waste recognition
- **Industry Solutions**: Automated sorting systems for recycling facilities
- **Educational Purposes**: Teaching computer vision and environmental awareness

## 🚀 Features

### 🔧 Core Functionality
- **Multi-source scraping**: Extract images from any URL with infinite scroll
- **Pexels API integration**: High-quality stock images via official API
- **Resume capability**: Continues from last downloaded image (no overwrites)
- **Smart pagination**: Automatically navigates through multiple pages
- **Duplicate prevention**: Avoids downloading the same image twice

### 📁 Project Structure
```
web-image-scrapper/
├── main.py              # General image extractor (Selenium-based)
├── extra.py             # Pexels API image downloader
├── images/              # Downloaded images from main script
├── pexels_images/       # Downloaded images from Pexels API
├── pyproject.toml       # Project dependencies
├── uv.lock              # Lock file for dependencies
└── README.md           # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Chrome browser (for Selenium)
- Pexels API key (for `extra.py`)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/web-image-scrapper.git
cd web-image-scrapper
```

2. **Install dependencies**
```bash
pip install -e .
```

3. **Run the image scrapers**

#### For general web scraping:
```bash
python main.py
```

#### For Pexels API scraping:
```bash
python extra.py
```

## 📋 Configuration

### Main Script (`main.py`)
- **Target URL**: Currently set to Unsplash plastic trash images
- **Image Limit**: 50 images (configurable)
- **Save Directory**: `images/`

### Pexels Script (`extra.py`)
- **Search Term**: "nature" (configurable)
- **Image Limit**: 25 images (configurable)
- **Pages**: 3 pages (configurable)
- **Save Directory**: `pexels_images/`

### Environment Variables
Create a `.env` file for Pexels API:
```ini
PEXELS_API_KEY=your_api_key_here
```

## 🔧 Customization

### Changing Target URLs
Edit `main.py` line 75:
```python
driver.get("https://unsplash.com/s/photos/plastic-trash")  # Your target URL
```

### Modifying Search Terms
Edit `extra.py` line 8:
```python
SEARCH_TERM = "your_search_term"
```

### Adjusting Image Limits
- `main.py`: Change `IMAGE_LIMIT = 50`
- `extra.py`: Change `IMAGE_LIMIT = 25`

## ⚠️ Important Notes

### Rate Limiting
- Built-in delays prevent overwhelming servers
- Respect website terms of service
- Consider using proxies for large-scale scraping

### Legal Considerations
- Only scrape publicly available images
- Respect robots.txt files
- Use responsibly and ethically

## 🎯 Use Cases

### Machine Learning Datasets
- **Computer Vision**: Training image classification models
- **Object Detection**: Creating bounding box datasets
- **Image Segmentation**: Preparing pixel-level annotation data

### Research Applications
- **Environmental Studies**: Plastic waste analysis
- **Material Science**: Visual material classification
- **Recycling Technology**: Automated sorting systems

### Industry Solutions
- **Waste Management**: Smart recycling bins
- **Manufacturing**: Quality control systems
- **Retail**: Product recognition systems

## 📊 Dataset Statistics

The created dataset includes:
- **Multiple plastic types**: PET, HDPE, PVC, LDPE, PP, PS
- **Various conditions**: Clean, dirty, crushed, intact
- **Different backgrounds**: Real-world scenarios
- **High-quality images**: Suitable for ML training

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Kaggle Dataset**: [Visual Plastic Type Recognition Dataset](https://www.kaggle.com/datasets/harshitkandoi7850/dataset-for-visual-plastic-type-recognition)
- **Pexels API**: [Get your API key](https://www.pexels.com/api/)
- **ChromeDriver**: Automatically managed by webdriver-manager

---

⭐ **Star this repository if it helped you create your dataset!**