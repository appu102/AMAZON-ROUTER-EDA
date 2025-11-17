<h1>Amazon Wi-Fi Routers Analysis</h1>
<h3>Web Scraping | Python | EDA | Visualization | Streamlit</h3>

<p>
This project focuses on scraping Wi-Fi router listings from <strong>Amazon India</strong>, cleaning the extracted data,
and performing a complete <strong>Exploratory Data Analysis (EDA)</strong> to uncover pricing patterns,
brand popularity, and market trends.
</p>

<hr>

<h2>Project Overview</h2>
<p>
I scraped multiple pages of Amazon India for Wi-Fi Router data using <strong>BeautifulSoup</strong> and analyzed the dataset
using <strong>Python, Pandas, NumPy, Seaborn, and Matplotlib</strong>.
A <strong>Streamlit dashboard</strong> was also built to make the insights interactive and easy to understand.
</p>

<hr>

<h2>Dataset Features</h2>
<ul>
  <li>Product Name</li>
  <li>Brand</li>
  <li>Price</li>
  <li>Old Price</li>
  <li>Discount</li>
  <li>Ratings</li>
  <li>Reviews Count</li>
  <li>Deal/Offer Information</li>
  <li>Product Link</li>
</ul>

<hr>

<h2>Key Insights</h2>

<h3>1. Most Popular Brands</h3>
<p>TP-Link, D-Link, and Tenda dominate the market.</p>

<h3>2. Highest Average Price Brand</h3>
<p>GEONIX has the highest average price among all brands.</p>

<h3>3. Price vs Sales Relationship</h3>
<p>
There is a weak negative correlation – higher-priced routers tend to sell slightly less.
</p>

<h3>4. Premium vs Budget Market</h3>
<p>Premium routers have lower sales volume; mid-range models sell more.</p>

<h3>5. Brand Market Share</h3>
<p>Top brands cover approximately 78% of total products.</p>

<hr>

<h2>Visualizations Included</h2>
<ul>
  <li>Brand-wise product count</li>
  <li>Price distribution</li>
  <li>Correlation heatmap</li>
  <li>Brand market share</li>
  <li>Scatterplots (Price vs Ratings, Price vs Reviews)</li>
  <li>Interactive Streamlit dashboard</li>
</ul>

<hr>

<h2>Tools and Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>BeautifulSoup</li>
  <li>Requests</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>Streamlit</li>
</ul>

<hr>

<h2>Steps in the Project</h2>
<ol>
  <li>Scraped data using BeautifulSoup</li>
  <li>Cleaned and pre-processed the dataset</li>
  <li>Performed EDA (univariate, bivariate, multivariate)</li>
  <li>Created visualizations and insights</li>
  <li>Developed an interactive Streamlit dashboard</li>
</ol>

<hr>

<h2>Project Structure</h2>

<pre>
Amazon-Routers-Analysis/
│
├── data/
│     ├── routers_raw.csv
│     └── routers_cleaned.csv
│
├── notebooks/
│     └── amazon_router_eda.ipynb
│
├── images/        (Screenshots go here)
│     ├── price_distribution.png
│     ├── brand_sales.png
│     ├── heatmap.png
│     └── dashboard.png
│
├── app.py         (Streamlit App)
├── scraper.py     (Web Scraper)
└── README.html
</pre>

<hr>

<h2>Screenshots</h2>
<p>Add your images to the <code>images/</code> folder and reference them like this:</p>

<pre>
<img src="images/dashboard.png" width="600">
</pre>

<hr>

<h2>How to Run</h2>

<p><strong>1. Clone the Repository</strong></p>
<pre>git clone https://github.com/yourusername/Amazon-Routers-Analysis</pre>

<p><strong>2. Install Dependencies</strong></p>
<pre>pip install -r requirements.txt</pre>

<p><strong>3. Run the Streamlit App</strong></p>
<pre>streamlit run app.py</pre>
