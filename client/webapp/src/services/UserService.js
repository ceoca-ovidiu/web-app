import axios from 'axios'

const GET_ALL_USERS_URL = 'http://localhost:8080/getUsers';


class UserService {

    getUsers() {
        return axios.get(GET_ALL_USERS_URL);
    }
}

export default new UserService();