'use server'

import { SignupFormSchema } from "@/lib/_definitions"
import AuthService from '@/lib/_services/auth-service'

export async function signup(_prevState: unknown, formData: FormData) {
  let payload = Object.fromEntries(formData)
  const validationResult = SignupFormSchema.safeParse({
    ...payload,
  })
  if (!validationResult.success) {
    return {
      errors: validationResult.error.flatten().fieldErrors,
    }
  }

  try {
    const res = await AuthService.signupUser(validationResult.data)
    return { message: res.data?.message, status: res.status }
  } catch (err: any) {
    return { message: 'Unable to register user. Please try again', status: 400 }
  }
}
