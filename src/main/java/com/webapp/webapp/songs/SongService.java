package com.webapp.webapp.songs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SongService {
    @Autowired
    SongRepository songRepository;

    public List<Song> getALlSongs() {
        return songRepository.findAll();
    }

    public Song createSong(Song song) {
        return songRepository.save(song);
    }

}
