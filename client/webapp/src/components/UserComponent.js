import React, { Component } from 'react'
import UserService from '../services/UserService'

class UserComponent extends Component {

    constructor(props) {
        super(props)

        this.state = {
            users: []
        }
    }

    componentDidMount() {
        UserService.getUsers().then((response) => {
            this.setState({ users: response.data })
        });
    }

    render() {
        return (
            <div>
                <h1 className="text-center">User List</h1>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <td> ID </td>
                            <td> First Name </td>
                            <td> Last Name </td>
                            <td> Email </td>
                            <td> Place </td>
                            <td> Gender </td>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.users.map(
                                user =>
                                    <tr key={user.id}>
                                        <td> {user.id} </td>
                                        <td> {user.userFirstName} </td>
                                        <td> {user.userLastName}</td>
                                        <td> {user.userEmail}</td>
                                        <td> {user.userPlace}</td>
                                        <td> {user.userGender} </td>
                                    </tr>
                            )
                        }
                    </tbody>
                </table>
            </div>
        )
    }
}

export default UserComponent;