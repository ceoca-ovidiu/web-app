# Table of Content

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Install MongoDB](#install-mongodb)
- [Errors](#errors)
- [Versions](#versions)

# Description

# Technologies used

- Intellij JetBrains
- Maven
- MongoDB
- Node.js
- React.js

![spring_initializr](media/spring_initializr.png)

# Versions

- Intellij : 2022.2.3 (Ultimate Edition)
- node : v16.16.0
- npm : 8.11.0
- Java : 1.8.0_351
- Java : 19
- Spring Boot : 2.7.5

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

2. > Cannot autogenerate id of type java.lang.Integer for entity of type com.webapp.webapp.songs.Song!

Change ID from whatever type to String type

See
here: [link](https://stackoverflow.com/questions/71351310/cannot-autogenerate-id-of-type-java-lang-long-for-entity-of-type-entity-mongod)