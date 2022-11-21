package com.webapp.webapp.validation;

import org.jetbrains.annotations.NotNull;
import org.springframework.stereotype.Component;

@Component
public class UserValidation {

    public Boolean isGenderValid(@NotNull String value) {
        if(value.toUpperCase().equals("MALE") || value.toUpperCase().equals("FEMALE")){
            return true;
        }
        return false;
    }

    public Boolean isFirstNameValid(@NotNull String value) {
        if(value.matches("[a-zA-Z]+") && !value.isEmpty()){
            return true;
        }
        return false;
    }

    public Boolean isLastNameValid(@NotNull String value) {
        if(value.matches("[a-zA-Z]+") && !value.isEmpty()){
            return true;
        }
        return false;
    }

    public Boolean isEmailValid(@NotNull String value) {
        return value.matches("^(?=.{1,64}@)[A-Za-z0-9_-]+(\\\\.[A-Za-z0-9_-]+)*@[^-][A-Za-z0-9-]+(\\\\.[A-Za-z0-9-]+)*(\\\\.[A-Za-z]{2,})$\n" + "\n");
    }

    public Boolean isPlaceValid(@NotNull String value) {
        if(value.matches("[a-zA-Z]+") && !value.isEmpty()){
            return true;
        }
        return false;
    }
}
