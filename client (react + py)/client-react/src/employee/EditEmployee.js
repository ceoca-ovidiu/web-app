import axios from "axios";
import React, { useState, useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

export default function EditEmployee() {

    let navigate = useNavigate();

    const [employee, setEmployees] = useState([]);
    
    const { id } = useParams();

    useEffect(() => {
        loadEmployee();
    }, []);


    const onSubmit = async (e) => {
        e.preventDefault();
        await axios.put(`http://localhost:8080/updateEmployee/${id}`, employee);
        navigate("/");
    };

    const loadEmployee = async () => {
        const result = await axios.get(`http://localhost:8080/getEmployeeById/${id}`);
        setEmployees(result.data);
    };

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6 offset-md-3 border rounded p-4 mt-2 shadow">
                    <h2 className="text-center m-4">Edit Employee</h2>
                    <form onSubmit={(e) => onSubmit(e)}>
                        <div className="mb-3">
                            <label htmlFor="firstName" className="form-label">
                                First Name
                            </label>
                            <input
                                type={"text"}
                                className="form-control"
                                placeholder="Enter employee first name"
                                name="firstName"
                                value={employee.employeeFirstName}
                                onChange={(e) => setEmployees({ ...employee, employeeFirstName: e.target.value })}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="lastName" className="form-label">
                                Last Name
                            </label>
                            <input
                                type={"text"}
                                className="form-control"
                                placeholder="Enter employee last name"
                                name="lastName"
                                value={employee.employeeLastName}
                                onChange={(e) => setEmployees({ ...employee, employeeLastName: e.target.value })}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="email" className="form-label">
                                E-mail
                            </label>
                            <input
                                type={"text"}
                                className="form-control"
                                placeholder="Enter employee e-mail"
                                name="email"
                                value={employee.employeeEmail}
                                onChange={(e) => setEmployees({ ...employee, employeeEmail: e.target.value })}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="place" className="form-label">
                                Place
                            </label>
                            <input
                                type={"text"}
                                className="form-control"
                                placeholder="Enter employee place"
                                name="place"
                                value={employee.employeePlace}
                                onChange={(e) => setEmployees({ ...employee, employeePlace: e.target.value })}
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="gender" className="form-label">
                                Gender
                            </label>
                            <input
                                type={"text"}
                                className="form-control"
                                placeholder="Enter employee gender (MALE/FEMALE)"
                                name="gender"
                                value={employee.employeeGender}
                                onChange={(e) => setEmployees({ ...employee, employeeGender: e.target.value })}
                            />
                        </div>
                        <button type="submit" className="btn btn-success">Update</button>
                        <Link className="btn btn-danger mx-2" to="/">Cancel</Link>
                    </form>
                </div>
            </div>
        </div>
    );
}
