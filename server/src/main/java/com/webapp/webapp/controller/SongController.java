package com.webapp.webapp.controller;

import com.webapp.webapp.model.Song;
import com.webapp.webapp.model.User;
import com.webapp.webapp.service.SongService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
public class SongController {

    @Autowired
    SongService songService;

    @GetMapping("/getSongs")
    public List<Song> getSongs() {
        return songService.getALlSongs();
    }

    @PostMapping("/createSong")
    public Song createSong(@RequestBody Song song) {
        return songService.createSong(song);
    }

    @GetMapping("/getSongsById/{songId}")
    public List<Song> searchById(@PathVariable String songId) {
        return songService.searchByField("songId", songId);
    }

    @GetMapping("/getSongsByName/{songName}")
    public List<Song> searchByName(@PathVariable String songName) {
        return songService.searchByField("songName", songName);
    }

    @GetMapping("/getSongsByDuration/{duration}")
    public List<Song> searchByDuration(@PathVariable float duration) {
        return songService.searchByField("duration", String.valueOf(duration));
    }

    @GetMapping("/getSongsByArtist/{artistName}")
    public List<Song> searchByArtist(@PathVariable String artistName) {
        return songService.searchByField("artist", artistName);
    }

    @GetMapping("/getSongsByURL/{URL}")
    public List<Song> searchByURL(@PathVariable String URL) {
        return songService.searchByField("songURL", URL);
    }

    @DeleteMapping("/deleteSong/{id}")
    public Boolean deleteSong(@PathVariable String id) {
        return songService.deleteSong(id);
    }
}
