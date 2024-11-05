import axios from "axios"
import { BASE_URL } from "@/lib/_constants"

const authConfig = axios.create({
  baseURL: `${BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
})

export { authConfig }
