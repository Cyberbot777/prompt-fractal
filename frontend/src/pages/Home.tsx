import PageWrapper from "../components/PageWrapper";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <PageWrapper>
      <motion.div
        initial={{ y: -60, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 1.2, ease: [0.25, 0.8, 0.25, 1] }}
        className="flex flex-col items-center justify-center text-center min-h-[80vh]"
      >
        <h1 className="text-4xl md:text-5xl font-extrabold text-white tracking-tight mb-2 animate-pulse">
          PromptPilot
        </h1>

        <p className="text-lg text-gray-400 max-w-xl mb-5">
          Your path to AI integration and customization awaits...
        </p>

        <Link
          to="/prompt"
          className="bg-white/10 text-gray-200 px-5 py-2 text-sm rounded-full backdrop-blur-md hover:scale-105 hover:brightness-125 transition-all duration-200"
        >
          ↵ Enter
        </Link>
      </motion.div>
    </PageWrapper>
  );
}
