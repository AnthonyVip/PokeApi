# PokeApi
Instructions to run in local:
-In docker create the volume "mongodb_data" there the database data will be stored.
-In the Makefile run the make up, this will generate the 3 images and create the 3 containers of the project.
-In case you want to populate the db with the data of all the pokemon and the evolutions chains you would have to open a console in the web-1 container,
run command poetry shell to start the virtual environment and once started run the script "python populate.py" this will take about 10 minutes to complete.
-Once the containers are started you can call the endpoints which are:
 
 {local_ip}/api/v1/chain/{chain_id}/, this endpoint receives the id of the evolution chain of a pokemon species,
 if the evolution chain is not registered in the database it will make use of the pokeapi api to save the data in the database and proceed to return the information of that pokemon species.
 
 {local_ip}/api/v1/pokemon/{name}/, this endpoint receives the name of the pokemon and returns the data corresponding to that pokemon.
