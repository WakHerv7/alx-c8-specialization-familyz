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
import Welcome from "./pages/welcome/Welcome";
import Layout from "./pages/Layout";
function App() {
  return (
    <>
      <Router basename={process.env.PUBLIC_URL}>
        <Routes>
          <Route path="/welcome" element={<Welcome/>}>            
          </Route>
          <Route path="/login" element={<Login/>}>              
          </Route>
          <Route path="/signup" element={<Signup/>}>              
          </Route>
          <Route exact path="/" element={<Layout/>}>
            <Route exact path="" element={<Home/>}>            
            </Route>
            <Route exact path="listpage" element={<Listpage/>}>              
            </Route>
            <Route exact path="profilepage" element={<Profilepage/>}>              
            </Route>
            <Route exact path="myfamilies" element={<Myfamilies/>}>              
            </Route>
            <Route exact path="family-tree" element={<FamilyTree/>}>              
            </Route>
          </Route>
          
        </Routes>
      </Router>
    </>
  );
}

export default App;

