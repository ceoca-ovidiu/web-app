package com.webapp.webapp.songs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class SongController {

    @Autowired
    SongService songService;

    @GetMapping("/getSongs")
    public List<Song> getSongs() {
        List<Song> songList = songService.getALlSongs();
        if (songList.size() > 0) {
            return songList;
        } else {
            return null;
        }
    }

    @PostMapping("/createSong")
    public Song createSong(@RequestBody Song song) {
        return songService.createSong(song);
    }


}
