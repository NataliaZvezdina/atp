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