import { Routes, Route, Navigate } from "react-router-dom";

import Home from "./pages/Home";
import Analyze from "./pages/Analyze";
import Results from "./pages/Results";

function App() {
  return (
    <Routes>

      {/* Home page */}
      <Route
        path="/"
        element={<Home />}
      />

      {/* Plant analysis page */}
      <Route
        path="/analyze"
        element={<Analyze />}
      />

      {/* Prediction results page */}
      <Route
        path="/results"
        element={<Results />}
      />

      {/* Unknown routes */}
      <Route
        path="*"
        element={
          <Navigate
            to="/"
            replace
          />
        }
      />

    </Routes>
  );
}

export default App;