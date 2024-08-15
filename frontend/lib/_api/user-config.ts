import axios from "axios"

const userConfig = axios.create({
  baseURL: 'http://backend:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
})

export { userConfig }
