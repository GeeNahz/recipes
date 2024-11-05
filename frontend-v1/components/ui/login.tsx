'use client'

import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

import { useToast } from "@/components/ui/use-toast"
import useEffectAfterMount from "@/hooks/useEffectAfterMount"

import { login } from "@/lib/actions/login"
import { useActionState } from "react"

export const LoginForm = () => {
  const [state, action, pending] = useActionState(login, undefined)

  const { toast } = useToast()
  useEffectAfterMount(() => {
    if (state?.status === 400) {
      // show error toast
      toast({
        title: 'Login failed!',
        description: state.message,
        variant: 'destructive',
      })
    }

    if (state?.status === 200) {
      // show success toast
      toast({
        title: 'Login successful',
        description: state.message,
      })
    }
  }, [state])
  return (
    <Card>
      <CardHeader className="w-full text-center">
        <CardTitle>Login</CardTitle>

        <CardDescription>Enter your login credentials</CardDescription>
      </CardHeader>

      <form action={action}>
        <CardContent>
          <div className="grid w-full items-center gap-4">
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

              <div className="h-1 text-xs text-destructive">
                {state?.errors && state.errors.password}
              </div>
            </div>
          </div>
        </CardContent>

        <CardFooter>
          <Button className="w-full" type="submit" disabled={pending} aria-disabled={pending}>
            {pending ? 'Logging in...' : 'Login'}
          </Button>
        </CardFooter>
      </form>
    </Card>
  )
}
