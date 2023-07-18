import {React, useState, useEffect }from 'react';
import Header from "../../components/Header";
import Listpagestyle from  "./Listpage.module.css";
import Table from "../../components/table/Table";
import Leftbar from "../../components/leftbar/Leftbar";
import AddIcon from '@mui/icons-material/Add';
import { Link, useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import { selectAllIndividuals,  getIndividualsStatus, getIndividualsError, fetchIndividuals }from '../../reducers/IndividualSlice';

function Listpage() {
    const dispatch = useDispatch();    
    const navigate = useNavigate();
    // console.log("process.env.REACT_APP_API_URL :", process.env.REACT_APP_API_URL)
    // --------------------------------------------------------
    const myIndividuals = useSelector(selectAllIndividuals);
    const individualsStatus = useSelector(getIndividualsStatus);
    const individualsError = useSelector(getIndividualsError);
    useEffect(() => {
        if (individualsStatus === 'idle') {
            dispatch(fetchIndividuals())            
        }
        else if (individualsStatus === 'succeeded') {
            console.log("======================")
            console.log("myIndividuals:", myIndividuals)
            console.log("======================")
        }
    }, [individualsStatus, dispatch])
    // --------------------------------------------------------


    let renderedIndividuals;
    if (individualsStatus === 'loading') {
        renderedIndividuals = <tr><td>...</td></tr>;
    } else if (individualsStatus === 'succeeded' && Array.isArray(myIndividuals.family)) {
        renderedIndividuals =  <Table myIndividuals= {myIndividuals.family}/>
        // renderedIndividuals = myIndividuals.map((individual, index) => (            
        // <tr key={index} onClick={()=>handleModalOpen(individual.id)} className="table_row_w cursor-pointer">
        //     <td className="text-gray-900  cursor-pointer font-light px-6 py-4 whitespace-nowrap">
        //         {individual.createdAt.split("T")[0]}
        //     </td>
        //     {/* <td className="text-gray-900 font-light px-6 py-4 whitespace-nowrap">
        //         {individual.transaction_type}
        //     </td> */}
        //     <td className="text-gray-900 font-light px-6 py-4 whitespace-nowrap">
        //         {individual.to_account_name}
        //     </td>
        //     <td className="text-gray-900 font-light px-6 py-4 whitespace-nowrap">
        //         {individual.individualors_names}
        //     </td>
        //     <td className="text-gray-900 font-light px-6 py-4 whitespace-nowrap">
        //         {individual.total_amount ?? 0}
        //     </td>                           
        // </tr>
    // ))
    } else if (individualsStatus === 'failed') {
        renderedIndividuals = {individualsError};
    }

    return (
        <>        
        {Array.isArray(myIndividuals.family) && <Header currentUser={myIndividuals.family[3]}/>}
        <div className={Listpagestyle.profilecontainer}>
            <h1 className={Listpagestyle.familymembers}>Family Members</h1>
            
               
            
            <div className={Listpagestyle.renderedcontainer}>
                <div className={Listpagestyle.renderedtop}>
                    <Leftbar currentUser={Array.isArray(myIndividuals.family) && myIndividuals.family[3]}/>
                </div>
                
                <div className={Listpagestyle.renderedbottom}>
                    {/* <h2 className={Listpagestyle.content}>Content</h2> */}
                    {renderedIndividuals}
                    <div className={Listpagestyle.addbutton}><button className={Listpagestyle.buttonicon}><AddIcon fontSize="large" className={Listpagestyle.addicon}/></button></div>
                    
                </div>
               
            </div>
            
        </div>
        </>
        
        
    )
}

export default Listpage;