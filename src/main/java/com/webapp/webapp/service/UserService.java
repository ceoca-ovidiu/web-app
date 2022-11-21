package com.webapp.webapp.service;


import com.webapp.webapp.model.Gender;
import com.webapp.webapp.model.User;
import com.webapp.webapp.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.convert.MongoConverter;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    MongoConverter mongoConverter;

    String uri = "mongodb+srv://root:root@mongocluster.rxylknq.mongodb.net/?retryWrites=true&w=majority";
    String databaseName = "webapp";
    String collectionName = "users";

    public List<User> getALlUsers() {
        return userRepository.findAll();
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }


    public List<User> searchByField(String field, String value) {
        List<User> userList = new ArrayList<>();

        switch (field) {
            case "userFirstName":
                for (User user : getALlUsers()) {
                    if (user.getUserFirstName().equals(value)) {
                        userList.add(user);
                    }
                }
                break;
            case "userLastName":
                for (User user : getALlUsers()) {
                    if (user.getUserLastName().equals(value)) {
                        userList.add(user);
                    }
                }
                break;
            case "userEmail":
                for (User user : getALlUsers()) {
                    if (user.getUserEmail().equals(value)) {
                        userList.add(user);
                    }
                }
                break;
            case "userPlace":
                for (User user : getALlUsers()) {
                    if (user.getUserPlace().equals(value)) {
                        userList.add(user);
                    }
                }
                break;
            case "id":
                for (User user : getALlUsers()) {
                    if (user.getId().equals(value)) {
                        userList.add(user);
                    }
                }
                break;
            case "userGender":
                for (User user : getALlUsers()) {
                    if (user.getUserGender() == Gender.valueOf(value)) {
                        userList.add(user);
                    }
                }
                break;
        }
        return userList;
    }

    public Boolean deleteUser(String id) {
        List<User> userList = searchByField("id", id);
        if (userList.isEmpty()) {
            return false;
        } else {
            userRepository.deleteById(id);
            return true;
        }
    }
}
