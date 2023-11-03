import axios from 'axios';

class ApiService {
    LoadVOD() {
        return axios.get("/vod/gettest");
    }
}
export default new ApiService();