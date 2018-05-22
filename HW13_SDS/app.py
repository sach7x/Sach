# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
     # Find data
    mars_info = mongo.db.mars.find_one()

    # return template and data
    return render_template("index.html", mars_info=mars_info)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    mars_info = scrape_mars.scrape()
    print(mars_info)

    #store results in dictionary (stored in scrape_mars.py file)
    
    # Insert Mars info into database
    mongo.db.mars.insert_one(mars_info)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
     app.run(debug=True)
