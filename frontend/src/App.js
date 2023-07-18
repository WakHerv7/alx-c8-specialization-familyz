import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import Listpage from "./pages/listpage/Listpage";
import Profilepage from "./pages/profile-page/Profilepage";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Myfamilies from './pages/myfamilies/Myfamilies';
import FamilyTree from "./pages/family-tree/FamilyTree.js";
import Home from "./pages/home/Home";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route exact path="/login" element={<Login />}/>
          <Route exact path="/signup" element={<Signup />}/>
          <Route exact path="/listpage" element={<Listpage />}/>
          <Route exact path="/profilepage" element={<Profilepage />}/>
          <Route exact path="/myfamilies" element={<Myfamilies />}/>
          <Route exact path="/family-tree" element={<FamilyTree />}/>
        </Routes>
      </Router>
    </>
  );
}

export default App;
