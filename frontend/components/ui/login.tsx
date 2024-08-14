import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { SubmitButton } from "@/components/ui/submit-button"

export const LoginForm = () => {
    return (
        <Card>
            <CardHeader>
                <CardTitle>Login</CardTitle>

                <CardDescription>Enter your login credentials</CardDescription>
            </CardHeader>

            <form>
                <CardContent>
                    <div className="grid w-full items-center gap-4">
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
                    <SubmitButton value="Login" loadingValue="Logging in..." />
                </CardFooter>
            </form>
        </Card>
    )
}