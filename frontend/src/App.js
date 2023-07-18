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
// import Header from "./components/Header";
import Layout from "./pages/Layout";
function App() {
  return (
    <>
      <Router forceRefresh={true}>
        <Routes>
          {/* <Route path="/" element={<Home key="1" />}>            
          </Route> */}
          <Route path="/login" element={<Login key="2" />}>              
          </Route>
          <Route path="/signup" element={<Signup key="3" />}>              
          </Route>
          <Route exact path="/" element={<Layout/>}>
            <Route exact path="" element={<Home key="1" />}>            
            </Route>
            <Route exact path="listpage" element={<Listpage key="4" />}>              
            </Route>
            <Route exact path="profilepage" element={<Profilepage key="5" />}>              
            </Route>
            <Route exact path="myfamilies" element={<Myfamilies key="6" />}>              
            </Route>
            <Route exact path="family-tree" element={<FamilyTree key="7" />}>              
            </Route>
          </Route>
          
        </Routes>
      </Router>
    </>
  );
}

export default App;

