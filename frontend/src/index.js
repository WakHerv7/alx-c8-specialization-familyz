import React from 'react';
import ReactDOM from 'react-dom/client';
import {Store} from './store/Store.js';
import {Provider} from 'react-redux';
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
import FamilyTree from "./pages/family-tree/FamilyTree.js";


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
  {
    path: "/family-tree",
    element: <FamilyTree />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={Store}>
      <RouterProvider router={router} />
    </Provider>
  </React.StrictMode>
);


