# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

#Import Depedencies 
import requests 
from splinter import Browser
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

mars_data = {}
 
def scrape_all():
    browser = init_browser()

    

    mars_news(browser)
    featured_image(browser)
    mars_facts()
    hemispheres(browser)

    browser.quit()

    return mars_data
    # Setup splinter
    
def mars_news(browser):

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html =browser.html
    soup = BeautifulSoup(html,'html.parser')

    title_results =soup.find_all('div', class_='content_title')

    # retrieve the the title of the first news article
    news_title = title_results[1].text
    #print(news_title)

    # retrieve the paragraph of the first news article
    p_news = soup.find_all('div',class_='article_teaser_body')

    news_p = p_news[0].text
    #print(news_p)
    # Dictionary entry from MARS NEWS
    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p
    # Close the test browser
    return mars_data


    # Next part pulling image from website
def featured_image(browser):

    # url for image page 
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url)

    #XPATH slector
    xpath = "/html/body/div[1]/div/a/button"

    img_results = browser.find_by_xpath(xpath)
    img = img_results[0]
    img.click()

    ## Scrape the browser into soup and use soup to find the full resolution image of mars
    html = browser.html
    soup = bs(html, 'html.parser')



    img_url = soup.find("img", class_="fancybox-image")["src"]

    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + img_url
    featured_image_url

    mars_data['featured_image_url'] = featured_image_url
    return mars_data

 
    # Mars Facts 
def mars_facts():
    #define URL
    url = "https://space-facts.com/mars/"

    # use read_html to scrape tables
    tables = pd.read_html(url)
    tables

    #save file

    mars_facts = tables[0].to_html()
    mars_facts

    mars_info['mars_facts'] = mars_facts

    return mars_data
    


    # Mars Hemispheres

def hemispheres(browser):   
    ## URL of page to be scraped
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    ## Opens test Chrome browser
    browser.visit(url)

    hemisphere_image_urls = []
    link = browser.find_by_css("a.product-item h3")

    for x in range (len(link)):
        hemis = {}
        
        browser.find_by_css("a.product-item h3")[x].click()
        
        html = browser.html
        hemi_soup = bs(html,"html.parser")
        
        hemis['title'] = hemi_soup.find("h2", class_="title").get_text()
        hemis['img_url'] = hemi_soup.find("a", text="Sample").get("href")

        hemisphere_image_urls.append(hemis)

        browser.back()
    
    hemisphere_image_urls

    mars_data["hemispheres"] = hemisphere_image_urls


    
    
    return mars_data


# if __name__ == "__main__":
#     print()