package com.webapp.webapp.songs;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.net.URL;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "song")
public class Song {

    @Id
    private Integer songId;
    private String songName;
    private float duration;
    private String artist;
    private URL songURL;

}
