package com.webapp.webapp.users;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.ZonedDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "user")
public class User {
    @Id
    private int id;
    private String userFirstName;
    private String userLastName;
    private String userEmail;
    private Gender userGender;
    private ZonedDateTime userCreatedTime;

}
