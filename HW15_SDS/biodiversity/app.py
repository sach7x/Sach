#import libraries/dependencies
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

#flask setup
app = Flask(__name__)

#database setup
engine=create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")

session=Session(bind=engine)

Base = automap_base()

Base.prepare(engine, reflect=True)

sample_names = Base.classes.samples
OTU = Base.classes.otu
Metadata = Base.classes.samples_metadata

# create all relevant routes as defined in instructions
#return index page
@app.route("/")
def home():
    return render_template("index.html")

#return list of sample names
@app.route('/names')
def names():
    samples_query = session.query(sample_names)
    samples = pd.read_sql(samples_query.statement, samples_query.session.bind)
    names=list()
    for i in samples.to_dict().keys():
        names.append(i)
    names=names[1:]
    return(jsonify(names)) 

#return list of OTU descriptions
@app.route('/otu')
def otu():
    otu_query = session.query(OTU)
    otu = pd.read_sql(otu_query.statement, otu_query.session.bind)
    taxonomy=otu.lowest_taxonomic_unit_found
    return(jsonify(taxonomy.to_dict()))  

#return metadata of samples
@app.route("/metadata/<sample>")
def metadata(sample):
    sample_ID=int(sample.split("_")[1])
    metadata_query = session.query(Metadata).filter(Metadata.SAMPLEID==sample_ID)
    metadata = pd.read_sql(metadata_query.statement, metadata_query.session.bind)
    return(jsonify(metadata.to_dict()))  

#return weekly washing frequency as a number
@app.route("/wfreq/<sample>")
def wfreq(sample):
    sample_ID=int(sample.split("_")[1])
    wfreq_query = session.query(Metadata).filter(Metadata.SAMPLEID==sample_ID)
    wfreq = int(pd.read_sql(wfreq_query.statement, wfreq_query.session.bind)['WFREQ'])
    return(jsonify(wfreq))

#return OTU IDs and Sample values for given sample
@app.route("/samples/<sample>") 
def sampleData(sample):
    sort_values= session.query(sample_names.otu_id,sample).order_by(sample+" desc").limit(100).all()
    sampleData_result = [{"otu_id" : [c[0] for c in sort_values],
          "sample_values" : [c[1] for c in sort_values]}]
    return jsonify(sampleData_result)

if __name__ == '__main__':
    app.run(debug=True)