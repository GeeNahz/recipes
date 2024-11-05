'use server'

import { SignupFormSchema, LoginFormSchema } from "@/lib/_definitions"
import AuthService from '@/lib/_services/auth-service'
import { redirect } from "next/navigation"
import auth from "@/lib/auth"


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

export async function login(_prevState: unknown, formData: FormData) {
  let payload = Object.fromEntries(formData)
  const validationResult = LoginFormSchema.safeParse({
    ...payload,
  })
  if (!validationResult.success) {
    return {
      errors: validationResult.error.flatten().fieldErrors,
    }
  }

  try {
    const res = await AuthService.loginUser(validationResult.data)
    // create session for user
    let data = {
      tokens: {
        access: res.data.access,
        refresh: res.data.refresh,
        token_type: res.data.token_type,
      },
      user: res.data.user,
    }
    await auth.createSession(data)
  } catch (err: any) {
    return { message: 'Username or password is incorrect.', status: 400 }
  }

  redirect('/dashboard')
}
