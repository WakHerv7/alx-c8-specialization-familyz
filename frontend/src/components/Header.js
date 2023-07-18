import Headerstyle from "./Header.module.css";
import Leftbarstyle from "./leftbar/Leftbar.module.css";
import family from "./images/family.png";
import avatar from "./images/avatar.JPG";
import SearchIcon from '@mui/icons-material/Search';
import Avatar from '@mui/material/Avatar';

import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import {  selectIndividualById, fetchIndividuals, selectAllIndividuals,  getIndividualsStatus, getIndividualsError, fetchIndividualById }from '../reducers/IndividualSlice';


function Header({currentUser}) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [user, setUser] = useState();
    // --------------------------------------------------------
    const oneIndividual = useSelector(selectAllIndividuals);
    const individualsStatus = useSelector(getIndividualsStatus);
    const individualsError = useSelector(getIndividualsError);
    useEffect(() => {
        if (currentUser) {
            setUser(currentUser)
            console.log("======================")
            console.log("currentUser:", currentUser)
            console.log("======================")
        } else {
            if (individualsStatus === 'idle') {
                dispatch(fetchIndividualById({id:4}))            
            }
            else if (individualsStatus === 'succeeded') {
                setUser(oneIndividual)
                console.log("======================")
                console.log("myIndividuals:", oneIndividual)
                console.log("======================")
            }
        }
        
    }, [currentUser, individualsStatus, dispatch])
    // --------------------------------------------------------
    return (
        <header className={Headerstyle.headercontainer}>
            <div className={Headerstyle.headerleft}>
                <img className={Headerstyle.headerimage} src={family} alt="logo"></img>
                <span className={Headerstyle.logotext}>Familyz</span>
            </div>
            <div className={Headerstyle.headercenter}>
                <div className={Headerstyle.searchbar}>
                    <SearchIcon className={Headerstyle.searchicon}  />
                    <input className={Headerstyle.searchinput} placeholder="Search..." />
                </div>
            </div>
            <div className={Headerstyle.headerright}>
                {/* <Avatar className={Headerstyle.profilepic} alt="Remy Sharp" src={avatar} /> */}
                <div className={Headerstyle.headerright}>
                    <div className={Leftbarstyle.leftbaravatar}>
                        <Avatar className={Leftbarstyle.profile} alt="Remy Sharp" src={avatar} />
                    </div>
                        <div className={Leftbarstyle.leftbarnames}>
                            <h3 className={Leftbarstyle.leftbarnamesh3}>{user?.myName}</h3>
                            <p className={Leftbarstyle.leftbarnamesP} >@_{user?.email?.split('@')[0]}</p>
                        </div>
                </div>
            </div>
        </header>
    );
}

export default Header;