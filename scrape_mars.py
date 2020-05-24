#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import time
import requests

def scrape_info():

    browser = Browser("chrome")
    mars = {}
    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    result = soup.find_all('div',class_='content_title')
    title = result[1].a.text

    result2 = soup.find('div',class_='article_teaser_body')
    paragraph = result2.text

    mars['news_title'] = title
    mars['news_p'] = paragraph


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    clickimage=browser.find_by_id('full_image').click()
    clicklink=browser.find_link_by_partial_text('more info').click()
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find('figure',class_='lede')
    result.a.img['src']
    featured_image = 'https://www.jpl.nasa.gov'+ result.a.img['src']
    mars['featured_image_url']=featured_image
    mars


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)
    hemisphere_image_url = []
    findlink = browser.find_by_css('a.product-item h3')
    findlink
    for x in range(len(findlink)):
        hemisphere = {}
        browser.find_by_css('a.product-item h3')[x].click()
        firstelement = browser.find_link_by_text('Sample').first
        hemisphere['img_url']=firstelement['href']
        hemisphere['title']=browser.find_by_css('h2.title').text
        hemisphere_image_url.append(hemisphere)
        browser.back()


    mars["hemisphere"]=hemisphere_image_url


    url="https://space-facts.com/mars/"
    tables=pd.read_html(url)
    df=tables[0]
    df.columns=['atributes', 'values']
    tables_html=df.to_html()
    tables_html=tables_html.replace('\n','')
    mars['facts']=tables_html


    #url="https://twitter.com/marswxreport?lang=en"
    #browser.visit(url)
    #time.sleep(2)
    #html = browser.html
    #soup = BeautifulSoup(html, "html.parser")
    #result = soup.find_all('span',class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    #result

    return mars

if __name__ == "__main__":
    print(scrape_info())


