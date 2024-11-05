export default function AuthLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className="font-geist-mono w-full min-h-screen flex flex-col items-center justify-center">
      <div className="max-w-md w-full container mx-auto">
        {children}
      </div>
    </div>
  );
}
