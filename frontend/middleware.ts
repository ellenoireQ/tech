import { NextRequest, NextResponse } from "next/server";
import { jwtVerify } from "jose";

const SECRET_KEY = new TextEncoder().encode(process.env.SECRET_KEY ?? "");

export async function middleware(req: NextRequest) {
  const token =
    req.cookies.get("token")?.value

  const redirectUrl = new URL("/", req.url);

  if (!token) {
    return NextResponse.redirect(redirectUrl);
  }

  try {
    await jwtVerify(token, SECRET_KEY);
    return NextResponse.next();
  } catch {
    return NextResponse.redirect(redirectUrl);
  }
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
