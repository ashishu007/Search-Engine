# Search-Engine

Document search using different ranking algorithms

## Algorithms supported 
This is the list of algorithms currently supported for document ranking. 
* TF
* TF-IDF
* ~BM25~
* ~BERT~

## Docker Image

* Pull the image from `docker-hub`:

    ```docker pull ashishu007/rgu-soc-se:latest```

* Run the image:

    ```docker run -d -p 5000:5000 ashishu007/rgu-soc-se:latest```

* The Flask app will be running on `http://localhost:5000`

## Heroku

Assuming you have `docker` installed and an app created on `heroku`.

0. Suppose the app created on heroku is: `rgu-soc-search-eng`

1. Clone the repo:

    `git clone https://github.com/ashishu007/Search-Engine.git`

2. Build the docker-container:

    `docker build -t search-eng:latest .`

3. Tag the docker-container:

    `docker tag search-eng registry.heroku.com/rgu-soc-search-eng/web`

4. Push the tagged container to the heroku-registry:

    `docker push registry.heroku.com/rgu-soc-search-eng/web`

5. Release the container on heroku:

    `heroku container:release -a rgu-soc-search-eng web`

6. Goto the browser, and type: [rgu-soc-search-eng.herokuapp.com](https://rgu-soc-search-eng.herokuapp.com/)

