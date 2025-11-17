Amazon Wi-Fi Routers Analysis
Web Scraping | Python | EDA | Visualization | Streamlit
This project involves scraping Wi-Fi router listings from Amazon India, cleaning the dataset, and performing Exploratory Data Analysis (EDA) to understand pricing patterns, brand popularity, and market trends.
An interactive Streamlit dashboard is included for easy exploration.

Project Overview


Scraped multiple Amazon India pages using BeautifulSoup


Cleaned and processed the collected data


Conducted EDA using Pandas, NumPy, Matplotlib, and Seaborn


Built a Streamlit web app to present insights visually



Dataset Features
The dataset contains:


Product Name


Brand


Price


Old Price


Discount


Ratings


Reviews Count


Deal/Offer Information


Product Link



Key Insights
1. Most Popular Brands
TP-Link, D-Link, and Tenda lead in the number of listed products.
2. Highest Average Price Brand
GEONIX has the highest average router price.
3. Price vs Sales
A weak negative correlation indicates that higher-priced routers tend to sell slightly less.
4. Premium vs Budget Market
Premium routers have lower visibility and sales compared to mid-range models.
5. Market Share
Top brands account for approximately 78% of all listed routers.

Visualizations Included


Brand-wise product count


Price distribution


Correlation heatmap


Brand market share


Scatterplots for price vs ratings


Streamlit interactive dashboard



Tools and Technologies Used


Python


Pandas


NumPy


BeautifulSoup


Requests


Matplotlib


Seaborn


Streamlit



Steps in the Project


Web scraping using BeautifulSoup


Cleaning and preprocessing the dataset


Performing EDA


Creating plots and visual insights


Developing the Streamlit dashboard



Project Structure
Amazon-Routers-Analysis/
│
├── data/
│     ├── routers_raw.csv
│     └── routers_cleaned.csv
│
├── notebooks/
│     └── amazon_router_eda.ipynb
│
├── images/                 (Screenshots go here)
│     ├── price_distribution.png
│     ├── brand_sales.png
│     ├── heatmap.png
│     └── dashboard.png
│
├── app.py                  (Streamlit App)
├── scraper.py              (Web Scraper)
└── README.md


Screenshots
Add images to the images/ folder and reference them like this:
![Dashboard](images/dashboard.png)


How to Run
1. Clone the repository
git clone https://github.com/yourusername/Amazon-Routers-Analysis

2. Install the required packages
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py


