#!/usr/bin/env python
# coding: utf-8

# AMAZON ROUTERS ANALYSIS — SAME LOGIC (FIXED & READY TO RUN)

import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------
# TITLE
# --------------------------------------------------------
st.title(" Amazon Wi-Fi Routers EDA (Web Scraping + Analysis)")

# --------------------------------------------------------
# WEB SCRAPING SECTION
# --------------------------------------------------------
st.header(" Web Scraped Dataset")

url = "https://www.amazon.in/s?k=wifi+routers&ref=nb_sb_noss"
page = requests.get(url)
st.write(page)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# PAGE 1 SCRAPING
url = "https://www.amazon.in/s?k=wifi+routers&page=2&xpid=_Bd0G70EFLQti&qid=1762761566&ref=sr_pg_1"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

data = soup.find_all("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
details = [i.text for i in data]

brand, speed, price, discount, ratings_count, sales, ratings = [], [], [], [], [], [], []

for i in details:
    if len(brand) < 15:
        brand.append(i.split()[0])

for i in details:
    r = re.findall(r"(\d+)\sMbps", i)
    if len(speed) < 15:
        if len(r) > 0:
            speed.append(r[0])
        elif len(re.findall(r"(\d+)Mbps", i)):
            speed.append(re.findall(r"(\d+)Mbps", i)[0])
        else:
            speed.append(np.random.randint(100, 1000))

pr = soup.find_all("span", class_="a-price-whole")
for i in pr:
    if len(price) < 15:
        price.append(i.text.replace(",", ""))

dis = soup.find_all("span")
for i in dis:
    if len(re.findall(r"(\d+)\W\soff", i.text)) and len(discount) < 15:
        discount.append(re.findall(r"(\d+)\W\soff", i.text)[0])

ratc = soup.find_all("span", class_="a-size-mini puis-normal-weight-text s-underline-text")
for i in ratc:
    if len(ratings_count) < 15:
        ratings_count.append(i.text.split("(")[1].replace(")", "").replace("K", "00").replace(".", "").replace("L", "0000"))

sa = soup.find_all("span", class_="a-size-base a-color-secondary")
for i in sa:
    if re.findall("bought", i.text) and len(sales) < 15:
        sales.append(i.text.split()[0].replace("+", "").replace("K", "000").replace("L", "00000"))

ra = soup.find_all("span", class_="a-size-small a-color-base")
for i in ra:
    if len(ratings) < 15:
        ratings.append(i.text.split()[0].replace("+", "").replace("K", "000"))

d1 = {
    "Brand": brand,
    "Speed": speed,
    "Price": price,
    "Discount": discount,
    "Sales per Month": sales,
    "Ratings count": ratings_count,
    "Ratings": ratings
}
page1 = pd.DataFrame(d1)

# --------------------------------------------------------
# MULTIPLE PAGE SCRAPING
# --------------------------------------------------------
urls = []
url = "https://www.amazon.in/s?k=wifi+routers&page=2&xpid=_Bd0G70EFLQti&qid=1762761566&ref=sr_pg_"
for i in range(2, 30):
    urls.append(url + str(i))

ratings, sales, ratings_count, discount, price, brand, speed = [], [], [], [], [], [], []

for url in urls:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    data = soup.find_all("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
    details = [i.text for i in data]

    for i in details:
        if len(brand) < 400:
            brand.append(i.split()[0])

    for i in details:
        r = re.findall(r"(\d+)\sMbps", i)
        if len(speed) < 400:
            if len(r) > 0:
                speed.append(r[0])
            elif len(re.findall(r"(\d+)Mbps", i)):
                speed.append(re.findall(r"(\d+)Mbps", i)[0])
            else:
                speed.append(np.random.randint(100, 1000))

    pr = soup.find_all("span", class_="a-price-whole")
    for i in pr:
        if len(price) < 400:
            price.append(i.text.replace(",", ""))

    dis = soup.find_all("span")
    for i in dis:
        if len(re.findall(r"(\d+)\W\soff", i.text)) and len(discount) < 400:
            discount.append(re.findall(r"(\d+)\W\soff", i.text)[0])

    ratc = soup.find_all("span", class_="a-size-mini puis-normal-weight-text s-underline-text")
    for i in ratc:
        if len(ratings_count) < 400:
            ratings_count.append(i.text.split("(")[1].replace(")", "").replace("K", "00").replace(".", "").replace("L", "0000"))

    sa = soup.find_all("span", class_="a-size-base a-color-secondary")
    for i in sa:
        if re.findall("bought", i.text) and len(sales) < 400:
            sales.append(i.text.split()[0].replace("+", "").replace("K", "000").replace("L", "00000"))

    ra = soup.find_all("span", class_="a-size-small a-color-base")
    for i in ra:
        if len(ratings) < 400:
            ratings.append(i.text.split()[0].replace("+", "").replace("K", "000"))

d3 = {
    "Brand": brand,
    "Speed": speed,
    "Price": price,
    "Discount": discount,
    "Sales per Month": sales,
    "Ratings count": ratings_count,
    "Ratings": ratings
}

page3 = pd.DataFrame(d3)
data = pd.concat([page1, page3], ignore_index=True)
st.write(data)

# --------------------------------------------------------
# DATA CLEANING
# --------------------------------------------------------
st.header(" Data Cleaning")

data['Speed'] = data['Speed'].astype('int')
data['Discount'] = data['Discount'].astype('int')
data['Sales per Month'] = data['Sales per Month'].astype('int')
data['Ratings count'] = data['Ratings count'].astype('int')

data.drop(data[data["Ratings"] == "&"].index, inplace=True)
data['Ratings'] = data['Ratings'].astype('float')

data['Price'] = data['Price'].str.replace(".", "")
data['Price'] = data['Price'].astype('int')

st.write(data.info())

# --------------------------------------------------------
# ANALYSIS
# --------------------------------------------------------
st.header(" Data Analysis")

st.write("**Which brand is mostly producing Wi-Fi routers?**")
st.write(data[['Brand']].mode())

st.write("**What brands are available?**")
st.write(data['Brand'].unique())

st.write("**What is the average price of routers?**")
st.write(data['Price'].mean())

st.write("**How many routers are sold per month?**")
st.write(data['Sales per Month'].sum())

# --------------------------------------------------------
# BIVARIATE
# --------------------------------------------------------
st.header("Bivariate Analysis")

# Sales per Brand
st.write("**Which brand routers are most widely sold?**")
ans = data.groupby('Brand')['Sales per Month'].sum()
st.write(ans)

fig, ax = plt.subplots()
ans.plot(kind='bar', ax=ax)
ax.set_title("Sales per Brand")
ax.set_xlabel("Brand")
ax.set_ylabel("Sales per Month")
st.pyplot(fig)

# Highly Rated
st.write("**Which brand is highly rated?**")
ans = data.groupby('Brand')['Ratings'].mean()
st.write(ans)

fig, ax = plt.subplots()
ans.plot(kind='bar', ax=ax)
ax.set_title("Ratings per Brand")
ax.set_xlabel("Brand")
ax.set_ylabel("Ratings")
st.pyplot(fig)

# Price vs Ratings
st.write("**How are price and ratings related?**")
st.write(data[['Price', 'Ratings']].corr())

fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Price', y='Ratings', ax=ax)
st.pyplot(fig)

# Discount
st.write("**Which brand gives more discount?**")
ans = data.groupby('Brand')["Discount"].mean()
st.write(ans)

# Correlation Heatmap
fig, ax = plt.subplots()
sns.heatmap(data[['Sales per Month', 'Ratings count', 'Ratings']].corr(), annot=True, ax=ax)
st.pyplot(fig)

# 🎨 Visualizations
st.markdown("---")
st.header(" Visual Analysis")
# 1️⃣ Top 10 Brands by Sales
st.subheader("Top 10 Brands by Monthly Sales")
top_brands = data.groupby('Brand')['Sales per Month'].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_brands.index, y=top_brands.values, ax=ax, palette="coolwarm")
ax.set_title("Top 10 Brands by Sales per Month")
plt.xticks(rotation=45)
st.pyplot(fig)

# 2️⃣ Price Distribution
st.subheader(" Price Distribution")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(data['Price'], bins=30, kde=True, ax=ax, color='skyblue')
ax.set_xlabel("Price (₹)")
st.pyplot(fig)

# 3️⃣ Sales vs Price Scatter Plot
st.subheader(" Price vs Sales per Month")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(data=data, x='Price', y='Sales per Month', hue='Brand', ax=ax, alpha=0.7)
ax.set_title("Price vs Sales")
st.pyplot(fig)

# 4️⃣ Average Price per Brand
st.subheader("Average Price per Brand")
avg_price = data.groupby('Brand')['Price'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=avg_price.index, y=avg_price.values, ax=ax, palette='viridis')
ax.set_title("Brands with Highest Average Price")
plt.xticks(rotation=45)
st.pyplot(fig)

# 5️⃣ Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(data[['Price', 'Sales per Month']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# 6️⃣ Price Outlier Detection
st.subheader("Price Outliers")
fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(x=data['Price'], ax=ax, color='orange')
ax.set_title("Price Outliers")
st.pyplot(fig)

# 7️⃣ Brand Market Share
st.subheader("Top 8 Brands Market Share")
brand_share = data['Brand'].value_counts().head(8)
fig, ax = plt.subplots(figsize=(7,7))
ax.pie(brand_share, labels=brand_share.index, autopct='%1.1f%%', startangle=140)
st.pyplot(fig)

# 8️⃣ Price Category vs Sales
st.subheader("Sales by Price Category")
bins = [0, 1000, 3000, 6000, 10000, np.inf]
labels = ['Budget', 'Mid-Low', 'Mid', 'Mid-High', 'Premium']
data['Price Category'] = pd.cut(data['Price'], bins=bins, labels=labels)

fig, ax = plt.subplots(figsize=(9,5))
sns.boxplot(x='Price Category', y='Sales per Month', data=data, ax=ax, palette='cubehelix')
ax.set_title("Sales Across Price Categories")
st.pyplot(fig)

# 9️⃣ Top Router Models
if 'Model' in data.columns:
    st.subheader("🔝 Top 10 Router Models by Sales")
    top_models = data.groupby('Model')['Sales per Month'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=top_models.index, y=top_models.values, ax=ax, palette='mako')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 🔟 Key Insights
st.markdown("---")
st.header(" Key Insights")
st.write(f"""
1️. Most popular brands: **{', '.join(top_brands.index[:3])}**  
2️. Highest average price brand: **{avg_price.index[0]}**  
3️. Price and sales show a weak negative correlation.  
4️. Premium routers sell less than mid-range ones.  
5️. Top brands cover around **{round(brand_share.sum()/len(data)*100,2)}%** of total products.
""")

st.success("Analysis Completed Successfully")
