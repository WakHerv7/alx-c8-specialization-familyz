import Profilepagestyle from "./Profilepage.module.css";
import Header from "../../components/Header";
import Leftbar from "../../components/leftbar/Leftbar";
import PhotoIcon from '@mui/icons-material/Photo';
import Avatar from '@mui/material/Avatar';
import avatar from "../../components/images/avatar.JPG";
import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import {  selectIndividualById, selectAllIndividuals,  getIndividualsStatus, getIndividualsError, fetchIndividualById }from '../../reducers/IndividualSlice';

function Profilepage() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    // const oneIndividual = useSelector((state) => selectIndividualById(state, Number(2)));
    // --------------------------------------------------------
    const oneIndividual = useSelector(selectAllIndividuals);
    const individualsStatus = useSelector(getIndividualsStatus);
    const individualsError = useSelector(getIndividualsError);
    useEffect(() => {
        if (individualsStatus === 'idle') {
            dispatch(fetchIndividualById({id:4}))            
        }
        else if (individualsStatus === 'succeeded') {
            console.log("======================")
            console.log("myIndividuals:", oneIndividual)
            console.log("======================")
        }
    }, [individualsStatus, dispatch])
    // --------------------------------------------------------
    return (
        <div className={Profilepagestyle.maincontainer}>
            <Header />
            <div className={Profilepagestyle.containerdiv}>
                <div className={Profilepagestyle.leftdiv}>
                    <Leftbar currentUser={oneIndividual}/>
                </div>
                <div className={Profilepagestyle.rightdiv}>
                    <header className={Profilepagestyle.headertext}><h1>My Profile</h1></header>
                    {oneIndividual && <>
                        <div className={Profilepagestyle.rightbottomdiv}>
                        <div className={Profilepagestyle.bottomleftdiv}>
                            {/* <PhotoIcon className={Profilepagestyle.photoicon} /> */}
                            <div>
                                <h1 className={Profilepagestyle.personalh1}>Personal details</h1>
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Full name</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.myName}</h3>
                                </div>
                                {/* <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Last name</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>Brooklin</h3>
                                </div> */}
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Gender</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.myGender}</h3>
                                </div>
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Date of birth</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.birthdate}</h3>
                                </div>
                            </div>
                            {/* <Avatar size={34} className={'ds'} alt="Remy Sharp" src={avatar} /> */}
                            {/* <div className={Profilepagestyle.innerdiv}>
                                <p>{oneIndividual.myName}</p>
                            </div>
                            <div className={Profilepagestyle.innerdiv}>
                                <p className={Profilepagestyle.ptext}>Email</p>
                                <h3 className={Profilepagestyle.h3text}>{oneIndividual.email}</h3>
                            </div>
                            <div className={Profilepagestyle.innerdiv}>
                                <p className={Profilepagestyle.ptext}>Birth date</p>
                                <h3 className={Profilepagestyle.h3text}>{oneIndividual.birthdate}</h3>
                            </div>
                            <div className={Profilepagestyle.innerdiv}>
                                <p className={Profilepagestyle.ptext}>Language</p>
                                <h3 className={Profilepagestyle.h3text}>English</h3>
                            </div>
                            <div className={Profilepagestyle.innerdiv}>
                                <p className={Profilepagestyle.ptext}>Country</p>
                                <h3 className={Profilepagestyle.h3text}>{oneIndividual.country}</h3>
                            </div>
                            <div className={Profilepagestyle.innerdiv}>
                                <p className={Profilepagestyle.ptextbottom}>Life status</p>
                                <h3 className={Profilepagestyle.h3text}>{oneIndividual.myLifeStatus}</h3>
                            </div> */}
                        </div>
                        <div className={Profilepagestyle.bottomcenterdiv}>
                            
                            <div>
                                <h1 className={Profilepagestyle.centerh1}>Contact details</h1>
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Home address</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.adress}</h3>
                                </div>
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Phone number</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.telephone}</h3>
                                </div>
                                <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Email</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>{oneIndividual.email}</h3>
                                </div>
                                {/* <div className={Profilepagestyle.innerdiv}>
                                    <p className={Profilepagestyle.bottominnerdiv}>Date of birth</p>
                                    <h3 className={Profilepagestyle.bottomh3text}>28/02/2023</h3>
                                </div> */}
                            </div>
                        </div>
                        
                    </div>
                    </>}
                    
                </div>
            </div>
        </div>
    )
}

export default Profilepage;