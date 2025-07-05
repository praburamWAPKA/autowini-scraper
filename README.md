**🛡️ Disclaimer**
This project is for educational and research purposes only.

The developer is not affiliated with Autowini.com.

The developer is not responsible for any misuse, abuse, or violation of terms of service.

The code is provided as-is without warranty of any kind.

You are solely responsible for using this tool ethically and legally.


# 🚗 Autowini Scraper

A fast and reliable Python-based scraper that extracts used vehicle listings from [Autowini.com](https://www.autowini.com) using `curl` and JSON parsing. Listings are saved to a clean CSV file for further use or analysis.

---

## 🔧 Features

- ✅ Downloads thousands of vehicle listings
- ✅ Uses `curl` for network reliability
- ✅ Parses JSON responses from Autowini API
- ✅ Writes structured CSV output
- ✅ Auto-retries pages with missing or failed data
- ✅ Automatically deletes temp files after processing

---

## ⚙️ Requirements

- Python 3.6+
- curl (preinstalled on most Linux/macOS systems)

**Install Python dependencies:**

pip install beautifulsoup4


**🚀 Usage**
**1. Clone the repository:**

git clone https://github.com/your-username/autowini-scraper.git
cd autowini-scraper

**2. Run the scraper:**

python3 auto.py


**3. Optional: Change scraping range in auto.py:**

START_PAGE = 1
END_PAGE = 5398

This allows you to control how many pages the scraper will crawl from Autowini.

**📂 Output**

autowini_data.csv – Contains all extracted car listings

autowini_json/ – Temp directory for raw JSON files (auto-deleted after each page)


------------------------------------------------------------
✅ Saved 30 listings from page 57
📦 Downloading page 58
🔍 Preview of page 58 JSON:
{"result":"SUCCESS","data":{"totalCount":161937,"hidden":false,"items":[{"code":"CI202506270003942114","listingId":"IC4137575","status":"FOR_SALE","condition":"Used","detailUrl":"/items/IC4137575","itemName":"2016 Hyundai Avante AD O*KM(17R+S*KEY+FULLAUTO+ANDROI","content":"IC4137575 · Gasoline · 1,591cc · AT · LHD · 5seats · Front 2WD · S.Korea · 163,503km (Actual)","make":"Hyundai","subModel":"Avante","modelYear":2016,"steeringType":"LHD","steering":"LHD","fuelType":"Gasoline","drivetrainType"
------------------------------------------------------------


