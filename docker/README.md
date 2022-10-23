### Project overview

The main idea is to write docker-compose file and additional files that will deploy a set of 3 related services.

---

### Service description

##### Service-1: The database

The container for data storage. What kind of database will be used - no matter, you can use the image from [Docker Hub](https://hub.docker.com/).

Requirements:
+ to store the data necessary for the web application to work. Two columns represent the data:
    + *name* (string)
    + *age* (integer)

##### Service-2: The script for filling the database

The container for filling the database. The service starts, connects to the database over the network and fills it with a set of data.

Notes:
+ you can write scripts in any language, we advise Python or Bash
+ write Dockerfile to build an image for the Service-2 container

Requirements:
+ the dataset is represented by a ``data.csv`` file with two columns and header
+ Service-2 starts after the Service-1
+ Service-2 stops after filling of the database
+ Service-2 displays the database content after it has been populated in ``stdout`` (validation of filling out)
