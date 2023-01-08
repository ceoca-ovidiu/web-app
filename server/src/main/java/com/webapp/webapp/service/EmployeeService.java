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

    private void updateWorkedHours() {
        List<Employee> employeeList = employeeRepository.findAll();
        if (!employeeList.isEmpty()) {
            for (Employee employee : employeeList) {
                employee.setWorkedHours(getHourlyRate(employee.getId()));
                employeeRepository.save(employee);
            }
        }
    }

    public List<Employee> getALlEmployees() {
        updateWorkedHours();
        return employeeRepository.findAll();
    }

    public Employee createEmployee(Employee employee) {
        updateWorkedHours();
        employee.setWorkedHours("0");
        return employeeRepository.save(employee);
    }

    public List<Employee> searchByField(String field, String value) {
        updateWorkedHours();
        List<Employee> returnedEmployeeList = new ArrayList<>();
        List<Employee> employeeList = getALlEmployees();
        if (employeeList.isEmpty()) {
            return returnedEmployeeList;
        } else {
            switch (field) {
                case "employeeFirstName" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getEmployeeFirstName().equals(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
                case "employeeLastName" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getEmployeeLastName().equals(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
                case "employeeEmail" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getEmployeeEmail().equals(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
                case "employeePlace" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getEmployeePlace().equals(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
                case "id" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getId().equals(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
                case "employeeGender" -> {
                    for (Employee employee : employeeList) {
                        if (employee.getEmployeeGender() == Gender.valueOf(value)) {
                            returnedEmployeeList.add(employee);
                        }
                    }
                }
            }
            return returnedEmployeeList;
        }
    }

    public Boolean deleteEmployee(String id) {
        updateWorkedHours();
        List<Employee> employeeList = searchByField("id", id);
        if (employeeList.isEmpty()) {
            return false;
        } else {
            employeeRepository.deleteById(id);
            timeTrackService.deleteTimeTrackByEmployeeID(id);
            return true;
        }
    }

    public String getHourlyRate(String id) {
        List<TimeTrack> timeTrackList = timeTrackService.searchByField("employeeId", id);
        if (timeTrackList.isEmpty()) {
            return "";
        } else {
            long minutes = 0;
            for (TimeTrack timeTrack : timeTrackList) {
                minutes = minutes + ChronoUnit.MINUTES.between(timeTrack.getCheckInTime(), timeTrack.getCheckOutTime());
            }
            return "" + minutes / 60.0;
        }
    }

    public Boolean updateEmployee(String id, Employee employee) {
        List<Employee> employeeList = searchByField("id", id);
        if (employeeList.isEmpty()) {
            return false;
        } else {
            Employee employeeToBeUpdated = employeeList.get(0);
            employeeToBeUpdated.setEmployeeFirstName(employee.getEmployeeFirstName());
            employeeToBeUpdated.setEmployeeLastName(employee.getEmployeeLastName());
            employeeToBeUpdated.setEmployeePlace(employee.getEmployeePlace());
            employeeToBeUpdated.setEmployeeEmail(employee.getEmployeeEmail());
            employeeToBeUpdated.setEmployeeGender(employee.getEmployeeGender());
            employeeRepository.save(employeeToBeUpdated);
            updateWorkedHours();
            return true;
        }
    }
}
