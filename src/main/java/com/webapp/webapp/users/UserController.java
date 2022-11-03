package com.webapp.webapp.users;

import com.webapp.webapp.songs.Song;
import com.webapp.webapp.songs.SongService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class UserController {

    @Autowired
    UserService userService;

    @GetMapping("/getUsers")
    public List<User> getUsers() {
        return userService.getALlUsers();
    }

    @PostMapping("/createUser")
    public User createUser(User user) {
        return userService.createUser(user);
    }

}
