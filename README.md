# Table of Content

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Versions](#versions)
- [Install MongoDB](#install-mongodb)
- [MongoDB commands](#mongodb-commands)
- [React](#react)
- [Errors](#errors)


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
- node : v18.12.1
- npm : 8.19.2
- Java : 1.8.0_351
- Java : 19.0.1
- Spring Boot : 2.7.5
- MongoDB : 6.0.1
- Swagger UI : 2.9.2 [[link]](https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui/2.9.2)
- Swagger2 : 2.9.2 [[link]](https://mvnrepository.com/artifact/io.springfox/springfox-swagger2/2.9.2)

# Install MongoDB (MacOS Ventura 13.0.1)

1. First you need to install **Homebrew** by opening a terminal and inserting the following command

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. You need to configure the Homebrew in order to work properly.

3. After installing Homebrew, it is time to install **MongoDB** so run this command in a terminal

```
brew tap mongodb/brew
```

4. Now install the actual MongoDB

```
brew install mongodb-community
```

MongoDB stores data as **BSON** which is the binary format for a JSON file.
There are **Documents** which are translated into rows for SQL and **Collections** which are the actual tables

# MongoDB commands

1. Start the server 
```
brew services start mongodb-community
```
2. Stop the server
```
brew services stop mongodb-community
```
3. If you want to have MongoDB running in background use 
```
mongod --config /opt/homebrew/etc/mongod.conf --fork
```
4. Enter MongoDB shell
```
mongosh
```
5. List databases
```
show dbs
```

# React

1. Start the server 
```
npm start
```

2. If you get the error *sh:react-scripts: command not found*
```
npm install
npm start
```
> See [here](https://stackoverflow.com/questions/40546231/sh-react-scripts-command-not-found-after-running-npm-start)


# Errors

1. > Web server failed to start. Port 8080 was already in use.

Change the port the app is running on with this command:

```
server.port=8081
```

Paste it into **application.properties** file from *resources* folder.

2. > Cannot autogenerate id of type java.lang.Integer for entity of type com.webapp.webapp.model.Song!

Change ID from whatever type to String type

See
here: [link](https://stackoverflow.com/questions/71351310/cannot-autogenerate-id-of-type-java-lang-long-for-entity-of-type-entity-mongod)