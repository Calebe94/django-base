#!/bin/sh

curl -s -X POST -d 'title=Titanic' -d 'description=A romantic movie' http://localhost:8000/api/movies/ | jq
curl -s -X POST -d 'title=Avatar' -d 'description=sci-fi movie' http://localhost:8000/api/movies/ | jq
curl -s -X POST -d 'title=Titanic to remove' -d 'description=A romantic movie' http://localhost:8000/api/movies/ | jq

curl -s -X PUT -d 'title=Avatar' -d 'description=sci-fi movie with blue guys and whatever' http://localhost:8000/api/movies/2/ | jq

curl -s -X DELETE -d 'title=Titanic to remove' -d 'description=A romantic movie' http://localhost:8000/api/movies/3/ | jq

curl -s -X POST -d 'stars=3' -d 'movie=1' -d 'user=1' http://localhost:8000/api/ratings/ | jq
curl -s -X PUT -d 'stars=4' -d 'movie=1' -d 'user=1' http://localhost:8000/api/ratings/1/ | jq

# Should return errors
curl -s -X POST -d 'stars=10' -d 'movie=2' -d 'user=1' http://localhost:8000/api/ratings/ | jq
curl -s -X POST -d 'stars=0' -d 'movie=2' -d 'user=1' http://localhost:8000/api/ratings/ | jq
