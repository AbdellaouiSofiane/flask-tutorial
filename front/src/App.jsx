import { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchMessage = async () => {
      const response = await fetch("/api/hello");
      const data = await response.json();
      setMessage(data.message);
    };
    fetchMessage();
  }, []);

  return <h1>{message}</h1>;
}

export default App;
