package com.webapp.webapp.controller;

import com.webapp.webapp.model.Employee;
import com.webapp.webapp.service.EmployeeService;
import com.webapp.webapp.validation.EmployeeValidation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
public class EmployeeController {

    @Autowired
    EmployeeService employeeService;

    @Autowired
    EmployeeValidation employeeValidation;

    @GetMapping("/getEmployees")
    public List<Employee> getEmployees() {
        return employeeService.getALlEmployees();
    }

    //FIXME: Validarea trebuie sa returneze ceva vizibil altfel se confunda cu null

    @PostMapping("/createEmployee")
    public Employee createEmployee(@RequestBody Employee employee) {
//        if (employeeValidation.isFirstNameValid(employee.getEmployeeFirstName()) && employeeValidation.isLastNameValid(employee.getEmployeeLastName()) && employeeValidation.isEmailValid(employee.getEmployeeEmail()) && employeeValidation.isPlaceValid(employee.getEmployeePlace()) && employeeValidation.isGenderValid(employee.getEmployeeGender().toString())) {
//        }
        return employeeService.createEmployee(employee);
//        return null;
    }

    @GetMapping("/getEmployeesByFirstName/{firstName}")
    public List<Employee> searchByFirstName(@PathVariable String firstName) {
        if (employeeValidation.isFirstNameValid(firstName)) {
            return employeeService.searchByField("employeeFirstName", firstName);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getEmployeesByEmail/{email}")
    public List<Employee> searchByEmail(@PathVariable String email) {
        if (employeeValidation.isEmailValid(email)) {
            return employeeService.searchByField("employeeEmail", email);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getEmployeesByPlace/{place}")
    public List<Employee> searchByPlace(@PathVariable String place) {
        if (employeeValidation.isPlaceValid(place)) {
            return employeeService.searchByField("employeePlace", place);
        }
        return new ArrayList<>();
    }

    @GetMapping("/getEmployeeById/{id}")
    public List<Employee> searchById(@PathVariable String id) {
        return employeeService.searchByField("id", id);
    }

    @GetMapping("/getEmployeesByGender/{gender}")
    public List<Employee> searchByGender(@PathVariable String gender) {
        if (employeeValidation.isGenderValid(gender)) {
            return employeeService.searchByField("employeeGender", gender);
        }
        return new ArrayList<>();
    }

    @DeleteMapping("/deleteEmployee/{id}")
    public Boolean deleteUser(@PathVariable String id) {
        return employeeService.deleteEmployee(id);
    }
}
