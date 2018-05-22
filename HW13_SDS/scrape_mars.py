
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import time


# In[2]:


# SECTION INVALIDATED DUE TO FRONT END OF WEBSITE BEING CHANGED
# URL of page to be scraped
#url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[3]:


# Retrieve page with the requests module
#response = requests.get(url)


# In[4]:


# Create BeautifulSoup object
#soup = bs(response.text, 'html.parser')


# In[5]:


# Examine the results, then determine element that contains sought info
#print(soup.prettify())


# In[6]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text. 
#Assign the text to variables that you can reference later.
#results = soup.find_all('li', class_='slide')
#print(results)


# In[7]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text. 
#Assign the text to variables that you can reference later.
#for result in results:
#    try:
#        news_title = result.find('a', target_="self")
#        news_p = result.find('div', class_="article_teaser_body")

#        if (news_title and news_p):
#                print('-------------')
#                print(news_title)
#                print(news_p)

#    except AttributeError as e:
#            print(e)


# In[8]:


#Visit the url for JPL's Featured Space Image here.
#Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
#Make sure to find the image url to the full size .jpg image.
#Make sure to save a complete url string for this image.
def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # # In[9]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # # In[10]:


    html = browser.html
    soup = bs(html, 'html.parser')
    browser.click_link_by_partial_text('FULL IMAGE')


    # # In[11]:


    # #needs a pause or else code runs too fast
    time.sleep(2)
    browser.click_link_by_partial_text('more info')


    # # In[12]:


    html2 = browser.html
    soup2 = bs(html2, 'html.parser')
    image = soup2.find('img', class_='main_image')


    url = image.get('src')

    featured_image_url = 'https://www.jpl.nasa.gov' + url
    # #print(featured_image_url)
    time.sleep(2)
    browser.quit()


    # # In[13]:


    # #Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    # #print(soup.prettify())


    # # In[14]:


    results = soup.find_all('div', class_='js-tweet-text-container')
    # #print(results)


    # # In[15]:


    mars_tweet= results[0].text
    # #print(mars_tweet)


    # # In[16]:


    # #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # #Use Pandas to convert the data to a HTML table string.
    mars_facts_url = 'https://space-facts.com/mars/'


    # # In[17]:


    tables = pd.read_html(url)
    tables


    # # In[18]:


    df = tables[0]
    df.head()


    # # In[19]:


    df.set_index(0, inplace=True)
    clean_df = df
    clean_df


    # # In[20]:


    html_table = clean_df.to_html()
    html_table


    # # In[21]:


    html_table.replace('\n', '')


    # # In[22]:


    df.to_html('mars_table.html')


    # # In[23]:


    # #Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # #You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # #Save both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # #Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # # In[24]:


    # #opening browser
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # # In[25]:


    # #clicking into Cerberbus Hemisphere Enhanced page
    # #this needs to be modified to click into new hyperlink each time (store hyperlinks in a list to access?)
    hemisphere_info = []
    hyperlinks = ['Cerberus Hemisphere Enhanced', 'Schiaparelli Hemisphere Enhanced', 'Syrtis Major Hemisphere Enhanced', 'Valles Marineris Hemisphere Enhanced']

    for hyperlink in hyperlinks:
        browser.click_link_by_partial_text(hyperlink)
        html = browser.html
        soup = bs(html, 'html.parser')
        image = soup.find('img', class_='wide-image')
        url = image.get('src')
        image_url = 'https://astrogeology.usgs.gov' + url
        results = soup.find('h2', class_="title").text
        hemisphere_info.append({'title':results, 'img_url': image_url})
        time.sleep(1)
        browser.back()



    # # In[26]:


    # #print(hemisphere_info)


    # # In[ ]:


    browser.quit()
    mars_info = {
        "image_URL": featured_image_url,
        "Mars_weather": mars_tweet,
        "Mars_table": mars_table(),
       # 'mars_facts': 'foo bar baz', 
        "Hemisphere_info": hemisphere_info
    }
    return mars_info



def mars_table():
    tables = pd.read_html(mars_facts_url)
    tables
    df = tables[0]
    df.head()
    df.set_index(0, inplace=True)
    clean_df = df
    clean_df
    html_table = clean_df.to_html()
    html_table
    html_table.replace('\n', '')
    return df.to_html('mars_table.html')