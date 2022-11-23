package com.webapp.webapp.service;

import com.webapp.webapp.model.Song;
import com.webapp.webapp.model.User;
import com.webapp.webapp.repository.SongRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
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

    public List<Song> searchByField(String field, String value) {
        List<Song> songList = new ArrayList<>();

        switch (field) {
            case "songId":
                for (Song song : getALlSongs()) {
                    if (song.getSongId().equals(value)) {
                        songList.add(song);
                    }
                }
                break;
            case "songName":
                for (Song song : getALlSongs()) {
                    if (song.getSongName().equals(value)) {
                        songList.add(song);
                    }
                }
                break;
            case "duration":
                for (Song song : getALlSongs()) {
                    if (song.getDuration() == Integer.parseInt(value)) {
                        songList.add(song);
                    }
                }
                break;
            case "artist":
                for (Song song : getALlSongs()) {
                    if (song.getArtist().equals(value)) {
                        songList.add(song);
                    }
                }
                break;
            case "songURL":
                for (Song song : getALlSongs()) {
                    if (song.getSongURL().equals(value)) {
                        songList.add(song);
                    }
                }
                break;
        }
        return songList;
    }


    public Boolean deleteSong(String id) {
        List<Song> songList = searchByField("songId", id);
        if (songList.isEmpty()) {
            return false;
        } else {
            songRepository.deleteById(id);
            return true;
        }
    }
}
