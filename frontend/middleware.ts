import { NextRequest, NextResponse } from "next/server";

export async function middleware(request: NextRequest) {
  const nextUrl = request.nextUrl
  const user = false;

  if (!user) {
    const response = NextResponse.redirect(new URL('/login', nextUrl))
    return response
  }

  return NextResponse.next()
}

// export const config = {
//   matcher: []
// }
