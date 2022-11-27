# Table of Content

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Versions](#versions)
- [Install MongoDB](#install-mongodb)
- [MongoDB commands](#mongodb-commands)
- [React](#react)
- [Errors](#errors)


# Description

This is a project that mimic an employee time tracking in a company. The server side is written in *Java* with the help of **Spring Boot** framework. All the data is stored in a **MongoDB** database using *JSON*. The GUI is a window application made using *Python* language and **Tkinter** library.

# Technologies used

- Intellij JetBrains
- PyCharm JetBrains
- Visual Studio Code
- Maven
- MongoDB
- Python
- Java
- Postman 

![spring_initializr](media/spring_initializr.png)

# Versions

- IDEs
  - Intellij : 2022.2.3 (Ultimate Edition)
  - Visual Studio Code : 1.73.1 (Universal)
  - PyCharm : 2022.2.3 (Ultimate Edition)
- Server (**Spring**)
  - Java : 1.8.0_351
  - Java : 19.0.1
  - Spring Boot : 2.7.5
  - Swagger UI : 2.9.2 [[link]](https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui/2.9.2)
  - Swagger2 : 2.9.2 [[link]](https://mvnrepository.com/artifact/io.springfox/springfox-swagger2/2.9.2)
- Database
  - MongoDB : 6.0.1
- Client (**Python**)
  - pip : v22.3.1
  - requests : 2.28.1
  - python : 3.11
  
# Install MongoDB (MacOS Ventura 13.0.1)


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