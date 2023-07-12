import Headerstyle from "./Header.module.css";
import family from "./images/family.png";
import avatar from "./images/avatar.JPG";
import SearchIcon from '@mui/icons-material/Search';
import Avatar from '@mui/material/Avatar';



function Header() {
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
                <Avatar className={Headerstyle.profilepic} alt="Remy Sharp" src={avatar} />
            </div>
        </header>
    );
}

export default Header;