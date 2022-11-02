# Table of Content

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Install MongoDB](#install-mongodb)

# Description

# Technologies used

- Java : 1.8.0_351
- Java : 19
- Spring Boot : 2.7.5
- Intellij JetBrains
- Maven
- MongoDB

![spring_initializr](media/spring_initializr.png)

# Install MongoDB

MongoDB stores data as **BSON** which is the binary format for a JSON file.
There are **Documents** which are translated into rows for SQL and **Collections** which are the actual tables

# Errors
1. > Web server failed to start. Port 8080 was already in use.

Change the port the app is running on with this command: 
```
server.port=8081
```
Paste it into **application.properties** file from *resources* folder.