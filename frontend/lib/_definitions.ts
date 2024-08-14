import { z } from 'zod'

export const SignupFormSchema = z.object({
    first_name: z.string().min(3).trim(),
    last_name: z.string().min(3).trim(),
    username: z.string().min(3).trim(),
    password: z.string().min(8).trim(),
    email: z.string().email().trim(),
})