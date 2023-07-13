import Listpagestyle from "./Listpage.module.css";
import Header from "../../components/Header";
import Leftbar from "../../components/leftbar/Leftbar";
import PhotoIcon from '@mui/icons-material/Photo';

function Listpage() {
    return (
        <div className={Listpagestyle.maincontainer}>
            <Header />
            <div className={Listpagestyle.containerdiv}>
                <div className={Listpagestyle.leftdiv}>
                    <Leftbar />
                </div>
                <div className={Listpagestyle.rightdiv}>
                    <header className={Listpagestyle.headertext}><h1>My Profile</h1></header>
                    <div className={Listpagestyle.rightbottomdiv}>
                        <div className={Listpagestyle.bottomleftdiv}>
                            <PhotoIcon className={Listpagestyle.photoicon} />
                            <div className={Listpagestyle.innerdiv}><p>Anastasia Brooklin</p></div>
                            <div className={Listpagestyle.innerdiv}>
                                <p className={Listpagestyle.ptext}>I.D</p>
                                <h3 className={Listpagestyle.h3text}>0056NZ98</h3>
                            </div>
                            <div className={Listpagestyle.innerdiv}>
                                <p className={Listpagestyle.ptext}>Date joined</p>
                                <h3 className={Listpagestyle.h3text}>18/02/2012</h3>
                            </div>
                            <div className={Listpagestyle.innerdiv}>
                                <p className={Listpagestyle.ptext}>Language</p>
                                <h3 className={Listpagestyle.h3text}>English</h3>
                            </div>
                            <div className={Listpagestyle.innerdiv}>
                                <p className={Listpagestyle.ptext}>Country</p>
                                <h3 className={Listpagestyle.h3text}>Canada</h3>
                            </div>
                            <div className={Listpagestyle.innerdiv}>
                                <p className={Listpagestyle.ptextbottom}>Status</p>
                                <h3 className={Listpagestyle.h3text}>Online</h3>
                            </div>
                        </div>
                        <div className={Listpagestyle.bottomcenterdiv}>
                            <div>
                                <h1 className={Listpagestyle.personalh1}>Personal details</h1>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>First name</p>
                                    <h3 className={Listpagestyle.bottomh3text}>Anastasia</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Last name</p>
                                    <h3 className={Listpagestyle.bottomh3text}>Brooklin</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Gender</p>
                                    <h3 className={Listpagestyle.bottomh3text}>Female</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Date of birth</p>
                                    <h3 className={Listpagestyle.bottomh3text}>28/02/2023</h3>
                                </div>
                            </div>
                            <div>
                                <h1 className={Listpagestyle.centerh1}>Contact details</h1>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Home address</p>
                                    <h3 className={Listpagestyle.bottomh3text}>9, Wakam street, fisayo close, Lagos</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Phone number</p>
                                    <h3 className={Listpagestyle.bottomh3text}>+234123456989</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Email</p>
                                    <h3 className={Listpagestyle.bottomh3text}>Brooklin@gmail.com</h3>
                                </div>
                                <div className={Listpagestyle.innerdiv}>
                                    <p className={Listpagestyle.bottominnerdiv}>Date of birth</p>
                                    <h3 className={Listpagestyle.bottomh3text}>28/02/2023</h3>
                                </div>
                            </div>
                        </div>
                        <div className={Listpagestyle.bottomrightdiv}>
                            <div className={Listpagestyle.rightinnerdiv}>
                                <p className={Listpagestyle.rightinnerdiv}>Middle name</p>
                                <h3 className={Listpagestyle.righth3text}>Olanike</h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Listpage;