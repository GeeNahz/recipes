'use server'

import { SignupFormSchema } from "@/lib/_definitions"

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
    return { message: JSON.stringify(payload) }
}