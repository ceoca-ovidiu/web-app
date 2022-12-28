import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useParams } from "react-router-dom";

export default function Home() {

    const [employees, setEmployees] = useState([]);

    const { id } = useParams();

    useEffect(() => {
        loadEmployees();
    }, []);

    const loadEmployees = async () => {
        const result = await axios.get("http://localhost:8080/getEmployees");
        console.log(result.data)
        setEmployees(result.data);
    };

    const deleteEmployee = async (id) => {
        await axios.delete(`http://localhost:8080/deleteEmployee/${id}`);
        loadEmployees();
    };

    return (
        <div className='container'>
            <div className='py-4'>
                <table className="table shadow border">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">ID</th>
                            <th scope="col">First Name</th>
                            <th scope="col">Last Name</th>
                            <th scope="col">Email</th>
                            <th scope="col">Place</th>
                            <th scope="col">Gender</th>
                            <th scope="col">Worked Hours</th>
                            <th scope="col">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {employees.map((employee, index) => (
                            <tr>
                                <th scope="row" key={index}>
                                    {index + 1}
                                </th>
                                <td>{employee.id}</td>
                                <td>{employee.employeeFirstName}</td>
                                <td>{employee.employeeLastName}</td>
                                <td>{employee.employeeEmail}</td>
                                <td>{employee.employeePlace}</td>
                                <td>{employee.employeeGender}</td>
                                <td>3</td>
                                <td>
                                    <div className="btn-group" role="group" aria-label="Basic mixed styles example">
                                        <Link type="button" className="btn btn-success" to={`/viewemployee/${id}`}>View</Link>
                                        <Link className="btn btn-warning" to={`/editemployee/${employee.id}`}>Edit</Link>
                                        <button type="button" className="btn btn-danger" onClick={(e) => deleteEmployee(employee.id)}>Delete</button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}