# About

This project is a simple proxy/relay API Dockerized python flask application. 
It will proxy the GET method calls to GBIF (Global Biodiversity Information Facility) APIs.
For documentation of GBIF APIs please visit https://www.gbif.org/developer/species

### To build Docker: 
docker build -f Dockerfile -t proxy .

### To run docker image at port 8080:
docker run -p 8080:8080 proxy

### The web server will run at 
http://localhost:8080

