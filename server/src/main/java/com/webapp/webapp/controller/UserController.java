package com.webapp.webapp.controller;

import com.webapp.webapp.model.User;
import com.webapp.webapp.service.UserService;
import com.webapp.webapp.validation.UserValidation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class UserController {

    @Autowired
    UserService userService;

    @Autowired
    UserValidation userValidation;

    @GetMapping("/getUsers")
    public List<User> getUsers() {
        return userService.getALlUsers();
    }

    @PostMapping("/createUser")
    public User createUser(@RequestBody User user) {
        if (userValidation.isFirstNameValid(user.getUserFirstName()) && userValidation.isLastNameValid(user.getUserLastName()) && userValidation.isEmailValid(user.getUserEmail()) && userValidation.isPlaceValid(user.getUserPlace()) && userValidation.isGenderValid(user.getUserGender().toString())) {
            return userService.createUser(user);
        }
        return null;
    }

    @GetMapping("/getUsersByFirstName/{firstName}")
    public List<User> searchByFirstName(@PathVariable String firstName) {
        if (userValidation.isFirstNameValid(firstName)) {
            return userService.searchByField("userFirstName", firstName);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getUsersByEmail/{email}")
    public List<User> searchByEmail(@PathVariable String email) {
        if (userValidation.isEmailValid(email)) {
            return userService.searchByField("userEmail", email);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getUsersByPlace/{place}")
    public List<User> searchByPlace(@PathVariable String place) {
        if (userValidation.isPlaceValid(place)) {
            return userService.searchByField("userPlace", place);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getUsersById/{id}")
    public List<User> searchById(@PathVariable String id) {
        return userService.searchByField("id", id);
    }

    @GetMapping("/getUsersByGender/{gender}")
    public List<User> searchByGender(@PathVariable String gender) {
        if (userValidation.isGenderValid(gender)) {
            return userService.searchByField("userGender", gender);
        }
        return new ArrayList<>();
    }

    @DeleteMapping("/deleteUser/{id}")
    public Boolean deleteUser(@PathVariable String id) {
        return userService.deleteUser(id);
    }
}
