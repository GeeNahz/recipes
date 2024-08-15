import { z } from 'zod'

export const SignupFormSchema = z.object({
  first_name: z
    .string()
    .min(2, { message: 'First name must be at least 2 characters long.' })
    .trim(),
  last_name: z
    .string()
    .min(2, { message: 'Last name must be at least 2 characters long.' })
    .trim(),
  email: z.string().email({ message: 'Please enter a valid email.' }).trim(),
  username: z
    .string()
    .min(3, { message: 'Username must be at least 3 characters long.' })
    .trim(),
  password: z
    .string()
    .min(8, { message: 'Be at least 8 characters long' })
    .regex(/[a-zA-Z]/, { message: 'Contain at least one letter.' })
    .regex(/[0-9]/, { message: 'Contain at least one number.' })
    .trim(),
});

// .regex(/[^a-zA-Z0-9]/, {
//   message: 'Contain at least one special character.',
// })

export type TSignupFormPayload = z.infer<typeof SignupFormSchema>

export const LoginFormSchema = z.object({
  username: z.string(),
  password: z.string().min(1, { message: 'Password field must not be empty.' }),
});

export type TLoginFormPayload = z.infer<typeof LoginFormSchema>

export type FormState =
  | {
    errors?: {
      first_name?: string[];
      last_name?: string[];
      username?: string[];
      email?: string[];
      password?: string[];
    };
    message?: string;
  }
  | undefined;

export type SessionPayload = {
  userId: string | number;
  expiresAt: Date;
};
