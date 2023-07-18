import React, {useState} from 'react';
import { Outlet } from "react-router-dom";
import Header from '../components/Header';

function Layout(props) {
    const [sidebarOpen, setSidebarOpen] = useState(false);
    return (
        <div>
            <Header/>
            <Outlet/>
        </div>
    );
}

export default Layout;