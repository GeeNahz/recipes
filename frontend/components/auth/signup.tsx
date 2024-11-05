'use client'

import { useActionState } from "react"

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

import { signup } from '@/lib/actions/auth'
import { useToast } from "@/components/ui/use-toast"
import useEffectAfterMount from "@/hooks/useEffectAfterMount"


export const SignupForm = () => {
  const [state, action, pending] = useActionState(signup, undefined)

  const { toast } = useToast()
  useEffectAfterMount(() => {
    if (state?.status === 400) {
      // show error toast
      toast({
        title: 'Operation failed!',
        description: state.message,
        variant: 'destructive',
      })
    }

    if (state?.status === 200) {
      // show error toast
      toast({
        title: 'Conflict!',
        description: state.message,
        variant: 'destructive',
      })
    }

    if (state?.status === 201) {
      // show success toast
      toast({
        title: 'Account created!',
        description: state.message,
        variant: 'default',
      })
    }
  }, [state])

  return (
    <Card>
      <CardHeader className="w-full text-center">
        <CardTitle>Signup</CardTitle>

        <CardDescription>Enter your details to get started.</CardDescription>
      </CardHeader>

      <form action={action}>
        <CardContent>
          <div className="grid w-full items-center gap-4">
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="first_name">First Name</Label>
              <Input id="first_name" name="first_name" placeholder="John" />

              <div className="h-1 text-xs text-destructive">
                {state?.errors && state.errors.first_name}
              </div>
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="last_name">Last Name</Label>
              <Input id="last_name" name="last_name" placeholder="Doe" />

              <div className="h-1 text-xs text-destructive">
                {state?.errors && state.errors.last_name}
              </div>
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" name="email" placeholder="johndoe@example.com" />

              <div className="h-1 text-xs text-destructive">
                {state?.errors && state.errors.email}
              </div>
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="username">Username</Label>
              <Input id="username" name="username" placeholder="Enter your username" />

              <div className="h-1 text-xs text-destructive">
                {state?.errors && state.errors.username}
              </div>
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="password">Password</Label>
              <Input id="password" name="password" type="password" placeholder="********" />

              <div className="min-h-1 text-xs text-destructive">
                {state?.errors && state.errors.password?.map((error, index) => (
                  <p key={index}>- {error}</p>
                ))}
              </div>
            </div>
          </div>
        </CardContent>

        <CardFooter>
          <Button className="w-full" type="submit" disabled={pending} aria-disabled={pending}>
            {pending ? 'Signing up...' : 'Signup'}
          </Button>
        </CardFooter>
      </form>
    </Card>
  )
}
