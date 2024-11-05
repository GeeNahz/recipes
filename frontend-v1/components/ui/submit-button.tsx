'use client'

import { useFormStatus } from "react-dom"
import { Button } from "@/components/ui/button"


type Props = {
    value: string;
    loadingValue?: string;
}
export const SubmitButton = ({ value, loadingValue }: Props) => {
    const { pending } = useFormStatus()

    return <Button className="w-full" type="submit" disabled={pending} aria-disabled={pending}>
        {
            pending
                ? (loadingValue ? loadingValue : value)
                : value
        }
    </Button>
}
