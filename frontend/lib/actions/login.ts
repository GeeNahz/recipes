'use server'

import { LoginFormSchema } from "@/lib/_definitions"
import AuthService from '@/lib/_services/auth-service'
import { redirect } from "next/navigation"

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
  console.log('LOGIN DATA: ', validationResult.data)

  try {
    const res = await AuthService.loginUser(validationResult.data)
    console.log('LOGIN USER: ', res.data)
    // create session for user
    // return { message: res.data?.message, status: res.status }
  } catch (err: any) {
    return { message: 'Username or password is incorrect.', status: 400 }
  }

  redirect('/dashboard')
}

