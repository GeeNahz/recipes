import axios from "axios"
import auth from "@/lib/auth"

import AuthService from "@/lib/_services/auth-service"

const userConfig = axios.create({
  baseURL: 'http://backend:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
})

userConfig.interceptors.request.use(async (req) => {
  const tokens = await auth.getTokens()
  const accessToken = tokens?.access

  if (accessToken) {
    req.headers['Authorization'] = `Bearer ${accessToken}`
  }
  return req
}, (error) => {
  return Promise.reject(error)
})


let refreshing_token: any = null

userConfig.interceptors.response.use(
  (res) => res,
  async (error) => {
    const originalRequest = error.config

    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const tokens = await auth.getTokens()
        const refreshToken = tokens?.refresh

        refreshing_token = refreshing_token ? refreshing_token : AuthService.refresh({ refresh: refreshToken })
        const response = await refreshing_token
        refreshing_token = null

        const { access, refresh } = response.data

        console.log('NEW ACCESS: ', access)
        console.log('NEW REFRESH: ', refresh)

        const user = await auth.getUser()
        const newSession = {
          user,
          tokens: {
            access,
            refresh,
            token_type: 'Bearer',
          }
        }

        await auth.createSession(newSession)
        userConfig.defaults.headers.common['Authorization'] = `Bearer ${access}`
        return userConfig(originalRequest)
      } catch (err) {
        console.error('TOKEN REFRESH FAILED: ', err)
        await auth.deleteSession()
        window.location.href = '/login'

        return Promise.reject(err)
      }
    }
    return Promise.reject(error)
  }
)

export { userConfig }
