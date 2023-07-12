import Profilepagestyle from  "./Profilepage.module.css";
import Table from "../../components/table/Table";
import Leftbar from "../../components/leftbar/Leftbar";
import AddIcon from '@mui/icons-material/Add';

function Profilepage() {
    return (
        <div className={Profilepagestyle.profilecontainer}>
            <h1 className={Profilepagestyle.familymembers}>Family Members</h1>
            
               
            
            <div className={Profilepagestyle.renderedcontainer}>
                <div className={Profilepagestyle.renderedtop}>
                    <Leftbar />
                </div>
                
                <div className={Profilepagestyle.renderedbottom}>
                    <h2 className={Profilepagestyle.content}>Content</h2>
                    <Table />
                    <div className={Profilepagestyle.addbutton}><button className={Profilepagestyle.buttonicon}><AddIcon fontSize="large" className={Profilepagestyle.addicon}/></button></div>
                    
                </div>
               
            </div>
            
        </div>
        
        
    )
}

export default Profilepage;