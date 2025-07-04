interface PageWrapperProps {
  children: React.ReactNode;
}

export default function PageWrapper({ children }: PageWrapperProps) {
  return (
    <div className="bg-gradient-to-r from-black to-zinc-900 bg-opacity-95 backdrop-blur-md text-gray-300 px-6 py-10 min-h-screen w-full font-sans leading-relaxed">
      {children}
    </div>
  );
}
