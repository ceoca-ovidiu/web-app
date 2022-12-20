package com.webapp.webapp.controller;

import com.webapp.webapp.model.Employee;
import com.webapp.webapp.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class EmployeeController {

    @Autowired
    EmployeeService employeeService;

    @GetMapping("/getEmployees")
    public List<Employee> getEmployees() {
        return employeeService.getALlEmployees();
    }

    @PostMapping("/createEmployee")
    public Employee createEmployee(@RequestBody Employee employee) {
        return employeeService.createEmployee(employee);
    }

    @GetMapping("/getEmployeesByFirstName/{firstName}")
    public List<Employee> searchByFirstName(@PathVariable String firstName) {
        return employeeService.searchByField("employeeFirstName", firstName);
    }

    @GetMapping("/getHourlyRateById/{id}")
    public String getHourlyRateById(@PathVariable String id) {
        return employeeService.getHourlyRate(id);
    }

    @GetMapping("/getEmployeesByEmail/{email}")
    public List<Employee> searchByEmail(@PathVariable String email) {
        return employeeService.searchByField("employeeEmail", email);
    }

    @GetMapping("/getEmployeesByPlace/{place}")
    public List<Employee> searchByPlace(@PathVariable String place) {
        return employeeService.searchByField("employeePlace", place);
    }

    @GetMapping("/getEmployeeById/{id}")
    public List<Employee> searchById(@PathVariable String id) {
        return employeeService.searchByField("id", id);
    }

    @GetMapping("/getEmployeesByGender/{gender}")
    public List<Employee> searchByGender(@PathVariable String gender) {
        return employeeService.searchByField("employeeGender", gender);
    }

    @DeleteMapping("/deleteEmployee/{id}")
    public Boolean deleteEmployee(@PathVariable String id) {
        return employeeService.deleteEmployee(id);
    }

    @PutMapping("/updateEmployee/{id}")
    public Employee updateEmployee(@PathVariable String id, @RequestBody Employee employee) {
        return employeeService.updateEmployee(id, employee);
    }
}
