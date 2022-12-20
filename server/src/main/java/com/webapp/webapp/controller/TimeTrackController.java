package com.webapp.webapp.controller;

import com.webapp.webapp.model.TimeTrack;
import com.webapp.webapp.service.TimeTrackService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TimeTrackController {

    @Autowired
    TimeTrackService timeTrackService;

    @GetMapping("/getAllTimeTracks")
    public List<TimeTrack> getTimeTracks() {
        return timeTrackService.getALlTimeTracks();
    }

    @PostMapping("/createTimeTrack")
    public TimeTrack createTimeTrack(@RequestBody TimeTrack timeTrack) {
        return timeTrackService.createTimeTrack(timeTrack);
    }

    @GetMapping("/getTimeTrackById/{timeTrackId}")
    public List<TimeTrack> searchTimeTrackById(@PathVariable String timeTrackId) {
        return timeTrackService.searchByField("timeTrackId", timeTrackId);
    }

    @GetMapping("/getTimeTrackByEmployeeId/{employeeId}")
    public List<TimeTrack> searchTimeTrackByEmployeeId(@PathVariable String employeeId) {
        return timeTrackService.searchByField("employeeId", employeeId);
    }

    @DeleteMapping("/deleteTimeTrack/{id}")
    public Boolean deleteTimeTrack(@PathVariable String id) {
        return timeTrackService.deleteTimeTrack(id);
    }

    @PutMapping("/updateTimeTrack/{id}")
    public TimeTrack updateTimeTrack(@PathVariable String id, @RequestBody TimeTrack timeTrack) {
        return timeTrackService.updateTimeTrack(id, timeTrack);
    }
}
