package com.webapp.webapp.users;

import com.webapp.webapp.songs.Song;
import com.webapp.webapp.songs.SongService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class UserController {

    @Autowired
    UserService userService;

    @GetMapping("/getUsers")
    public List<User> getUsers() {
        List<User> usersList = userService.getALlUsers();
        if (usersList.size() > 0) {
            return userService.getALlUsers();
        } else {
            return null;
        }
    }

    @PostMapping("/createUser")
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }

    //TODO

}
