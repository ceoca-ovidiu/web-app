package com.webapp.webapp.service;

import com.webapp.webapp.model.TimeTrack;
import com.webapp.webapp.repository.TimeTrackRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Service
public class TimeTrackService {
    @Autowired
    TimeTrackRepository timeTrackRepository;

    public List<TimeTrack> getALlTimeTracks() {
        return timeTrackRepository.findAll();
    }

    public TimeTrack createTimeTrack(TimeTrack timeTrack) {
        return timeTrackRepository.save(timeTrack);
    }

    public List<TimeTrack> searchByField(String field, String value) {
        List<TimeTrack> timeTrackList = new ArrayList<>();

        switch (field) {
            case "timeTrackId":
                for (TimeTrack timeTrack : getALlTimeTracks()) {
                    if (timeTrack.getTimeTrackId().equals(value)) {
                        timeTrackList.add(timeTrack);
                    }
                }
                break;
            case "checkInTime":
                for (TimeTrack timeTrack : getALlTimeTracks()) {
                    if (timeTrack.getCheckInTime().equals(LocalDateTime.parse(value))) {
                        timeTrackList.add(timeTrack);
                    }
                }
                break;
            case "checkOutTime":
                for (TimeTrack timeTrack : getALlTimeTracks()) {
                    if (timeTrack.getCheckOutTime().equals(LocalDateTime.parse(value))) {
                        timeTrackList.add(timeTrack);
                    }
                }
                break;
            case "employeeId":
                for (TimeTrack timeTrack : getALlTimeTracks()) {
                    if (timeTrack.getEmployeeId().equals(value)) {
                        timeTrackList.add(timeTrack);
                    }
                }
                break;
        }
        return timeTrackList;
    }


    public Boolean deleteTimeTrack(String id) {
        List<TimeTrack> timeTrackList = searchByField("timeTrackId", id);
        if (timeTrackList.isEmpty()) {
            return false;
        } else {
            timeTrackRepository.deleteById(id);
            return true;
        }
    }

    public TimeTrack updateTimeTrack(String id, TimeTrack timeTrack) {
        List<TimeTrack> timeTracks = searchByField("timeTrackId", id);
        TimeTrack timeTrackToBeUpdated = timeTracks.get(0);
        timeTrackToBeUpdated.setCheckInTime(timeTrack.getCheckInTime());
        timeTrackToBeUpdated.setCheckOutTime(timeTrack.getCheckOutTime());
        timeTrackToBeUpdated.setEmployeeId(timeTrack.getEmployeeId());
        timeTrackRepository.save(timeTrackToBeUpdated);
        return timeTrackToBeUpdated;
    }

    public Boolean deleteTimeTrackByEmployeeID(String id) {
        List<TimeTrack> timeTracks = getALlTimeTracks();
        if (timeTracks.isEmpty()) {
            return false;
        } else {
            for (TimeTrack timeTrack : timeTracks) {
                if (timeTrack.getEmployeeId().equals(id)) {
                    timeTrackRepository.deleteById(timeTrack.getTimeTrackId());
                }
            }
            return true;
        }
    }
}
