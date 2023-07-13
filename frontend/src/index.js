import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import Listpage from "./pages/listpage/Listpage";
import Profilepage from "./pages/profile-page/Profilepage";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Myfamilies from './pages/myfamilies/Myfamilies';


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/signup",
    element: <Signup />,
  },
  {
    path: "/listpage",
    element: <Listpage />,
  },
  {
    path: "/profilepage",
    element: <Profilepage />,
  },
  {
    path: "/myfamilies",
    element: <Myfamilies />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);


