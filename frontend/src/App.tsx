import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Prompt from "./pages/Prompt";
import Prompting101 from "./pages/Prompting101";
import Navbar from "./components/Navbar";


export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/prompt" element={<Prompt />} />
        <Route path="/prompting101" element={<Prompting101 />} />
      </Routes>
    </Router>
  );
}
