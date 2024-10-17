import axios from "axios"
import { BASE_URL } from "@/lib/_constants"

const authConfig = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
})

export { authConfig }
