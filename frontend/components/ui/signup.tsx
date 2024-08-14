'use client'

import { useFormState, useFormStatus } from "react-dom"

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"

import { signup } from '@/lib/actions/signup'
import { SubmitButton } from "@/components/ui/submit-button"

export const SignupForm = () => {
    const [state, action] = useFormState(signup, undefined)

    return (
        <Card>
            <CardHeader>
                <CardTitle>Signup</CardTitle>

                <CardDescription>Enter your details</CardDescription>
            </CardHeader>

            <form action={action}>
                <CardContent>
                    <div className="grid w-full items-center gap-4">
                        <div className="flex flex-col space-y-1.5">
                            <Label htmlFor="first_name">First Name</Label>
                            <Input id="first_name" name="first_name" placeholder="John" />
                        </div>
                        <div className="flex flex-col space-y-1.5">
                            <Label htmlFor="last_name">Last Name</Label>
                            <Input id="last_name" name="last_name" placeholder="Doe" />
                        </div>
                        <div className="flex flex-col space-y-1.5">
                            <Label htmlFor="email">Email</Label>
                            <Input id="email" type="email" name="email" placeholder="johndoe@example.com" />
                        </div>
                        <div className="flex flex-col space-y-1.5">
                            <Label htmlFor="username">Username</Label>
                            <Input id="username" name="username" placeholder="Enter your username" />
                        </div>
                        <div className="flex flex-col space-y-1.5">
                            <Label htmlFor="password">Password</Label>
                            <Input id="password" type="password" placeholder="********" />
                        </div>
                    </div>
                </CardContent>

                <CardFooter>
                    <SubmitButton
                        value="Sign Up"
                        loadingValue="Signing Up..."
                    />
                </CardFooter>
            </form>
        </Card>
    )
}
