This project sets up a NySQL datastore with docker, 
generates and ingests data, 
and visualizes it using python and plotly

First you'll need to start MySQL in docker so in a command window
input: docker-compose up-d
then make sure to pip install everything in the requirements file
with: pip install -r requirements.txt

then to run the ingestion file type : python data_ingest.py
then run: python visualization.py
