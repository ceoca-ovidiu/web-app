package com.webapp.webapp.service;


import com.webapp.webapp.model.Employee;
import com.webapp.webapp.model.Gender;
import com.webapp.webapp.model.TimeTrack;
import com.webapp.webapp.repository.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.convert.MongoConverter;
import org.springframework.stereotype.Service;

import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

@Service
public class EmployeeService {

    @Autowired
    EmployeeRepository employeeRepository;

    @Autowired
    MongoConverter mongoConverter;

    @Autowired
    TimeTrackService timeTrackService;

    String uri = "mongodb+srv://root:root@mongocluster.rxylknq.mongodb.net/?retryWrites=true&w=majority";
    String databaseName = "webapp";
    String collectionName = "employee";

    public List<Employee> getALlEmployees() {
        return employeeRepository.findAll();
    }

    public Employee createEmployee(Employee employee) {
        return employeeRepository.save(employee);
    }


    public List<Employee> searchByField(String field, String value) {
        List<Employee> employeeList = new ArrayList<>();

        switch (field) {
            case "employeeFirstName":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getEmployeeFirstName().equals(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
            case "employeeLastName":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getEmployeeLastName().equals(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
            case "employeeEmail":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getEmployeeEmail().equals(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
            case "employeePlace":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getEmployeePlace().equals(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
            case "id":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getId().equals(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
            case "employeeGender":
                for (Employee employee : getALlEmployees()) {
                    if (employee.getEmployeeGender() == Gender.valueOf(value)) {
                        employeeList.add(employee);
                    }
                }
                break;
        }
        return employeeList;
    }

    public Boolean deleteEmployee(String id) {
        List<Employee> employeeList = searchByField("id", id);
        if (employeeList.isEmpty()) {
            return false;
        } else {
            employeeRepository.deleteById(id);
            return true;
        }
    }

    public String getHourlyRate(String id) {
        List<TimeTrack> timeTrackList = timeTrackService.searchByField("employeeId", id);
        long minutes = 0;
        for (TimeTrack timeTrack : timeTrackList) {
            System.out.println(timeTrack.getCheckInTime() + " " + timeTrack.getCheckOutTime());
            minutes = minutes + ChronoUnit.MINUTES.between(timeTrack.getCheckInTime(), timeTrack.getCheckOutTime());
        }
        return "  WORKED HOURS : " + minutes / 60.0;
    }
}
