import { authConfig } from "@/lib/_api/auth-config"
import { TSignupFormPayload, TLoginFormPayload } from "@/lib/_definitions"

export default {
  async signupUser(payload: TSignupFormPayload) {
    return await authConfig.post('/auth/register', payload)
  },
  async loginUser(payload: TLoginFormPayload) {
    return await authConfig.post('/auth/pair', payload)
  },
  async refresh(payload: { refresh: string }) {
    return await authConfig.post('/auth/refresh', payload)
  },
  async logout(payload: { refresh: string }) {
    return await authConfig.post('/auth/blacklist', payload)
  },
}
