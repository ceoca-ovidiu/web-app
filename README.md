# Table of Content

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Versions](#versions)
- [Block Diagram](#block-diagram)
- [Activity Diagram](#activity-diagram)
- [User Guide](#user-guide)
- [Encountered Errors](#encountered-errors)

# Description

This is a project that mimic an employee time tracking in a company. The server side is written in *Java* with the help
of **Spring Boot** framework. All the data is stored in a **MongoDB** database using *JSON*. The GUI is a window
application made using *Python* language and **Tkinter** library.

# Technologies used

- Intellij JetBrains
- PyCharm JetBrains
- Visual Studio Code
- Maven
- MongoDB
- Python
- Java
- Postman

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
    - tkinter
- Client (**React**)
    - node : 18.12.1
    - npm : 8.19.2

# Block Diagram

![block_diagram](media/block_diagram.svg)

# Activity Diagram

![activity_diagram](media/activity_diagram.svg)

# User Guide

# Encountered Errors

## Server

1. > Web server failed to start. Port 8080 was already in use. (Server)

Change the port the app is running on with this command:

```
server.port=8081
```

Paste it into **application.properties** file from *resources* folder.

2. > Cannot autogenerate id of type java.lang.Integer for entity of type com.webapp.webapp.model.Employee! (Server)

Change ID from whatever type to String type

See
here: [link](https://stackoverflow.com/questions/71351310/cannot-autogenerate-id-of-type-java-lang-long-for-entity-of-type-entity-mongod)

## UI

3. > Python requests - No connection adapters were found for ... (UI)

You need to include *http://* part before the request call.

See here: [link](https://stackoverflow.com/questions/15115328/python-requests-no-connection-adapters)

4. > Tkinter button automatically call the function on runtime (UI)

You need to call the function using *lambda* expression.

See here: [link](https://stackoverflow.com/questions/3704568/tkinter-button-command-activates-upon-running-program)

5. > Expecting value: line 1 column 1 (char 0)

The request returns nothing which cannot be converted to json.

See here: [link](https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0)