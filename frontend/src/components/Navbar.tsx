import { motion } from "framer-motion";
import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();

  return (
    <motion.nav className="sticky top-0 z-50 bg-gradient-to-r from-[rgba(0,0,0,0.5)] to-[rgba(24,24,27,0.5)] backdrop-blur-md text-gray-300 px-6 py-4 shadow-md">
      <motion.div
        initial={{ y: -60, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 1.2, ease: [0.25, 0.8, 0.25, 1] }}
        className="flex gap-6 items-center"
      >
        <Link
          to="/"
          className="text-lg text-gray-300 hover:text-white hover:brightness-125 hover:scale-105 transition-all duration-200"
        >
          {location.pathname === "/" ? "{Home}" : "Home"}
        </Link>
        <Link
          to="/prompt"
          className="text-lg text-gray-300 hover:text-white hover:brightness-125 hover:scale-105 transition-all duration-200"
        >
          {location.pathname === "/prompt" ? "{Prompt Lab}" : "Prompt Lab"}
        </Link>
        <Link
          to="/prompting101"
          className="text-lg text-gray-300 hover:text-white hover:brightness-125 hover:scale-105 transition-all duration-200"
        >
          {location.pathname === "/prompting101" ? "{Prompting 101}" : "Prompting 101"}
        </Link>
        <Link
          to="/login"
          className="text-lg text-gray-300 hover:text-white hover:brightness-125 hover:scale-105 transition-all duration-200 ml-auto"
        >
          {location.pathname === "/login" ? "{Login}" : "Login"}
        </Link>
        <Link
          to="/register"
          className="text-lg text-gray-300 hover:text-white hover:brightness-125 hover:scale-105 transition-all duration-200"
        >
          {location.pathname === "/register" ? "{Register}" : "Register"}
        </Link>
      </motion.div>
    </motion.nav>
  );
}
