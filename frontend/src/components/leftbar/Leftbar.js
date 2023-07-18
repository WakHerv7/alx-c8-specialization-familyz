import Leftbarstyle from "./Leftbar.module.css";
import Avatar from '@mui/material/Avatar';
import HomeIcon from '@mui/icons-material/Home';
import FamilyRestroomIcon from '@mui/icons-material/FamilyRestroom';
import PhotoLibraryIcon from '@mui/icons-material/PhotoLibrary';
import FolderIcon from '@mui/icons-material/Folder';
import LinkIcon from '@mui/icons-material/Link';
import PeopleIcon from '@mui/icons-material/People';
import PersonIcon from '@mui/icons-material/Person';
import avatar from "../../images/photo1.jpg";
import { Link } from "react-router-dom";

import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import {  selectFamilyById, fetchFamilies, selectAllFamilies,  getFamiliesStatus, getFamiliesError, fetchFamilyById }from '../../reducers/FamilySlice';

function Leftbar(props) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    // --------------------------------------------------------
    const oneFamily = useSelector(selectAllFamilies);
    const familiesStatus = useSelector(getFamiliesStatus);
    const familiesError = useSelector(getFamiliesError);
    useEffect(() => {
        if (familiesStatus === 'idle') {
            dispatch(fetchFamilyById({id:1}))            
        }
        else if (familiesStatus === 'succeeded') {
            console.log("======================")
            console.log("myFamilies:", oneFamily)
            console.log("======================")
        }
    }, [familiesStatus, dispatch])
    // --------------------------------------------------------
    return (
        <div className={Leftbarstyle.leftbar}>
            <div className={Leftbarstyle.leftbarwrapper}>
                <div className={Leftbarstyle.leftbaravatar}>
                    <Avatar className={Leftbarstyle.profile} alt="Remy Sharp" src={avatar} />
                </div>
                <div className={Leftbarstyle.leftbarnames}>
                    <h3 className={Leftbarstyle.leftbarnamesh3}>{oneFamily && oneFamily.name}</h3>
                    {/* <p className={Leftbarstyle.leftbarnamesP} >@_{props.currentUser?.email?.split('@')[0]}</p> */}
                </div>
            </div>
            <div className={Leftbarstyle.leftbarbottomwrapper}>
                <ul className={Leftbarstyle.leftbarlist}>
                    <Link to="/" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><HomeIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Home</span></li></Link>
                    <Link to="/listpage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PeopleIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>My family members</span></li></Link>
                    <Link to="/profilepage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PersonIcon className={Leftbarstyle.leftbaricon} /><span className={Leftbarstyle.leftbarspantext}>My profile</span></li></Link>
                    <Link to="/myfamilies" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PhotoLibraryIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>All families</span></li></Link>
                    <Link to="/family-tree" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><FamilyRestroomIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Family Tree</span></li></Link>

                    {/* <a href="/" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><HomeIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Home</span></li></a>
                    <a href="/listpage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PeopleIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>My family members</span></li></a>
                    <a href="/profilepage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PersonIcon className={Leftbarstyle.leftbaricon} /><span className={Leftbarstyle.leftbarspantext}>My profile</span></li></a>
                    <a href="/myfamilies" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PhotoLibraryIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>All families</span></li></a>
                    <a href="/family-tree" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><FamilyRestroomIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Family Tree</span></li></a> */}
                    
                    {/* <li className={Leftbarstyle.leftbarlistitems}><FamilyRestroomIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Family Tree</span></li> */}
                </ul>
            </div>
        </div>
    )
}

export default Leftbar;