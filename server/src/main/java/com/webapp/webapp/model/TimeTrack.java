package com.webapp.webapp.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "timetrack")
public class TimeTrack {

    @Id
    private String timeTrackId;
    private LocalDateTime checkInTime;
    private LocalDateTime checkOutTime;
    private String employeeId;
}
