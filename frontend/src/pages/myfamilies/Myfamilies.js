import Myfamiliesstyle from "./Myfamilies.module.css";
import Header from "../../components/Header";
import { Helmet } from 'react-helmet';
import photo1 from "./images/photo1.jpg"

import {React, useState, useEffect }from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import { selectAllFamilies,  getFamiliesStatus, getFamiliesError, fetchFamilies }from '../../reducers/FamilySlice';

<Helmet bodyAttributes={{ style: 'background-color : #fff' }} />

function Myfamilies() {
    const dispatch = useDispatch();    
    const navigate = useNavigate();
    // console.log("process.env.REACT_APP_API_URL :", process.env.REACT_APP_API_URL)
    // --------------------------------------------------------
    const myFamilies = useSelector(selectAllFamilies);
    const familiesStatus = useSelector(getFamiliesStatus);
    const familiesError = useSelector(getFamiliesError);
    useEffect(() => {
        if (familiesStatus === 'idle') {
            dispatch(fetchFamilies())            
        }
        else if (familiesStatus === 'succeeded') {
            console.log("======================")
            console.log("myFamilies:", myFamilies)
            console.log("======================")
        }
    }, [familiesStatus, dispatch])
    // --------------------------------------------------------
    let renderedFamilies;
    if (familiesStatus === 'loading') {
        renderedFamilies = <tr><td>...</td></tr>;
    } else if (familiesStatus === 'succeeded' && Array.isArray(myFamilies)) {
        // renderedFamilies =  <Table myFamilies= {myFamilies.family}/>
        renderedFamilies = myFamilies.map((family, index) => ( 
            <div className={Myfamiliesstyle.images}>
                <div>
                    <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                </div>
                <a href={index == 0 ? '/':'#'} className={Myfamiliesstyle.imagetext}>{family.name}</a>
            </div>
        ))

    } else if (familiesStatus === 'failed') {
        renderedFamilies = {familiesError};
    }
    return (
        <div className={Myfamiliesstyle.myfamcontainer}>
            <Helmet>
                <style>{'body { background-color: #bae0e0; }'}</style>
            </Helmet>
            <Header />
            <div className={Myfamiliesstyle.myfamdiv}>
                <div className={Myfamiliesstyle.myfamdiv2}>
                    <div className={Myfamiliesstyle.myfamdivleft}>
                        <h1 className={Myfamiliesstyle.h1}>All families</h1>
                        <a href="/"className={Myfamiliesstyle.button1}>See my family</a>
                    </div>
                    <div className={Myfamiliesstyle.myfamdivright}>
                        <button className={Myfamiliesstyle.button2}>Add new</button>
                    </div>
                </div>
            </div>
            <div className={Myfamiliesstyle.imagesdiv}>
                {renderedFamilies}
                {/* <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>

                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div> */}
            </div>
        </div>
    )
}

export default Myfamilies;
