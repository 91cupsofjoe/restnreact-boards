import {useState} from "react";
import {Routes, Route, Link} from "react-router-dom";
import ThreadsPage from "./pages/ThreadsPage";
import ThreadDetailPage from "./pages/ThreadDetailPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";

function App() {
  const [selectedThread, setSelectedThread] = useState(null);

  /*
   * This acts as a view controller:
   *  if selectedThread === null, show ThreadList
   *  else, show ThreadDetailPage
   */
  return (
    <div>
      <nav>
        <Link to="/">Threads</Link>{" | "}
        <Link to="/login">Login</Link> {" | "}
        <Link to="/register">Register</Link>
      </nav>

      <Routes>
        <Route path="/" element={<ThreadsPage />} />
        <Route path="/threads/:threadId" element={<ThreadDetailPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />}/>
      </Routes>
    </div>
  );
}

export default App;