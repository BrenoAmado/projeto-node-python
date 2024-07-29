import axios from "axios";

export const useToken = async () => {
    return localStorage.getItem("token") || "";
};

const env = {
    local: 'http://192.168.0.7:8081',
    dev: 'dev'
};

const baseUrlGlobal = axios.create({
    baseURL: env.local,
});

baseUrlGlobal.interceptors.request.use(
    (config: any) => {
        //const auth = token ? `Bearer ${token}` : ''
        //config.headers.common['Authorization'] = auth

        return config;
    },
    (error) => Promise.reject(error),
);

baseUrlGlobal.interceptors.request.use(
    function (config) {
        config.data = { startTime: new Date().getTime() };
        return config;
    },
    function (error) {
        return Promise.reject(error);
    },
);

baseUrlGlobal.interceptors.response.use(
    function (response) {
        response.config.data = JSON.parse(response.config.data);
        response.config.data.endTime = new Date().getTime();
        response.headers.duration =
            response.config.data.endTime - response.config.data.startTime;
        return response;
    },
    function (error) {
        error.config.endTime = new Date().getTime();
        error.duration = error.config.endTime - error.config.startTime;
        return Promise.reject(error);
    },
);

export default baseUrlGlobal;
export {env}