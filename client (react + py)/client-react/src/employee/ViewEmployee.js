import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

export default function ViewEmployee() {

    const [employee, setEmployees] = useState([]);

    const { id } = useParams();

    useEffect(() => {
        loadEmployee();
        console.log(JSON.stringify(id));
    }, []);

    const loadEmployee = async () => {
        const result = await axios.get(`http://localhost:8080/getEmployeeById/${id}`);
        setEmployees(result.data);
    };

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6 offset-md-3 border rounded p-4 mt-2 shadow">
                    <h2 className="text-center m-4">Employee Details</h2>
                    {employee.map((employee) => (
                        <div className="card">
                            <div className="card-header">
                                Details of employee id : {employee.id}
                                <ul className="list-group list-group-flush">
                                    <li className="list-group-item">
                                        <b>First Name: </b>
                                        {employee.employeeFirstName}
                                    </li>
                                    <li className="list-group-item">
                                        <b>Last Name: </b>
                                        {employee.employeeLastName}
                                    </li>
                                    <li className="list-group-item">
                                        <b>E-mail: </b>
                                        {employee.employeeEmail}
                                    </li>
                                    <li className="list-group-item">
                                        <b>Place: </b>
                                        {employee.employeePlace}
                                    </li>
                                    <li className="list-group-item">
                                        <b>Gender: </b>
                                        {employee.employeeGender}
                                    </li>
                                    <li className="list-group-item">
                                        <b>Worked Hours: </b>
                                        {employee.workedHours}
                                    </li>
                                </ul>
                            </div>
                        </div>
                    ))}
                    <Link className="btn btn-primary my-2" to={"/"}>
                        Back to Home
                    </Link>
                </div>
            </div>
        </div>
    )
}