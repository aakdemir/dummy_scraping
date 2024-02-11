<!--Installations -->
install python
pip install scrapy,psycopg2

<!--Docker pulls -->
install docker desktop
docker pull
    -postgresql, mongodb
    -pgAdmin, mongo-express

<!-- run the commands at terminal -->
docker-compose up
<!-- to check docker -->
docker ps
scrapy crawl json_spider 

<!-- I created a dummy json file s03 which is same format with s01 and s02 -->
<!-- This python app is using spider to parses json file and saves into a Postgresql Db -->
<!-- Finally, after saving the data to db, this app is selecting all the data from db and writing into a json file -->

<!-- To dockerize -->
docker build -t json_spider .
docker run --name scrapy-container json_spider