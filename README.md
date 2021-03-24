# web-scraping-challenge

In this assignment we first used a created a jupyter notebook and used beautifulsoup, pandas and requests/splinter to scrape mars data from the internet.

We scraped the following:
  Mars News
  Mars Space Images-Featured Image 
  Mars Facts 
  Mars Hemsipheres ( used a python dictionary to store data images)
  
Once we had the jupyter notebook working we created an HTML page that displayed all the information we collected from our jupyter notebook.
  Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

Store the return value in Mongo as a Python dictionary.

Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
  
  
