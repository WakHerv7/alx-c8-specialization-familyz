import Leftbarstyle from "./Leftbar.module.css";
import Avatar from '@mui/material/Avatar';
import HomeIcon from '@mui/icons-material/Home';
import FamilyRestroomIcon from '@mui/icons-material/FamilyRestroom';
import PhotoLibraryIcon from '@mui/icons-material/PhotoLibrary';
import FolderIcon from '@mui/icons-material/Folder';
import LinkIcon from '@mui/icons-material/Link';
import PeopleIcon from '@mui/icons-material/People';
import PersonIcon from '@mui/icons-material/Person';
import avatar from "./images/avatar.JPG";
import { Link } from "react-router-dom";

function Leftbar(props) {
    return (
        <div className={Leftbarstyle.leftbar}>
            <div className={Leftbarstyle.leftbarwrapper}>
                <div className={Leftbarstyle.leftbaravatar}>
                    <Avatar className={Leftbarstyle.profile} alt="Remy Sharp" src={avatar} />
                </div>
                <div className={Leftbarstyle.leftbarnames}>
                    <h3 className={Leftbarstyle.leftbarnamesh3}>Chinwe Chukwuogor {props.name}</h3>
                    <p className={Leftbarstyle.leftbarnamesP} >@Kiraa_Daves {props.username}</p>
                </div>
            </div>
            <div className={Leftbarstyle.leftbarbottomwrapper}>
                <ul className={Leftbarstyle.leftbarlist}>
                    <li className={Leftbarstyle.leftbarlistitems}><HomeIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Home</span></li>
                    <li className={Leftbarstyle.leftbarlistitems}><FamilyRestroomIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Family Tree</span></li>
                    <Link to="./myfamilies" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PhotoLibraryIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Photos</span></li></Link>
                    <li className={Leftbarstyle.leftbarlistitems}><FolderIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Document</span></li>
                    <li className={Leftbarstyle.leftbarlistitems}><LinkIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Link</span></li>
                    <Link to="./profilepage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PeopleIcon className={Leftbarstyle.leftbaricon} /> <span className={Leftbarstyle.leftbarspantext}>Members</span></li></Link>
                    <Link to="./listpage" className={Leftbarstyle.link}><li className={Leftbarstyle.leftbarlistitems}><PersonIcon className={Leftbarstyle.leftbaricon} /><span className={Leftbarstyle.leftbarspantext}>Profile</span></li></Link>
                </ul>
            </div>
        </div>
    )
}

export default Leftbar;