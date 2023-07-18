import Rightstyle from "./Rightbarstyle.module.css";
import FamilyRestroomIcon from '@mui/icons-material/FamilyRestroom';

function Rightbar() {
    return (
        <div className={Rightstyle.rightbar}>
            <div className={Rightstyle.rightbarwrapper}>
                <h2>Post Categories</h2>
                <div className={Rightstyle.categorieslist}>
                    <button className={Rightstyle.postcategories}>Marriages</button>
                    <button className={Rightstyle.postcategories}>Funerals</button>
                    <button className={Rightstyle.postcategories}>Babies</button>
                    <button className={Rightstyle.postcategories}>Birthdays</button>
                    <button className={Rightstyle.postcategories}>Anniversaries</button>
                    <button className={Rightstyle.postcategories}>Hangouts</button>
                </div>
            </div>
            <div className={Rightstyle.rightbarbottomwrapper}>
                <h2>Family List</h2>
                <hr className={Rightstyle.horizontalrule}></hr>
                <ul className={Rightstyle.rightbarlist}>
                    <li className={Rightstyle.rightbarlistitems}><FamilyRestroomIcon className={Rightstyle.leftbaricon} /> <span className={Rightstyle.spantext}>Maxwell Family</span></li>
                    <li className={Rightstyle.rightbarlistitems}><FamilyRestroomIcon className={Rightstyle.leftbaricon} /> <span className={Rightstyle.spantext}>Johnson Family</span></li>
                    <li className={Rightstyle.rightbarlistitems}><FamilyRestroomIcon className={Rightstyle.leftbaricon} /> <span className={Rightstyle.spantext}>Adenuga Family</span></li>
                    <li className={Rightstyle.rightbarlistitems}><FamilyRestroomIcon className={Rightstyle.leftbaricon} /> <span className={Rightstyle.spantext}>Adams Family</span></li>
                    <li className={Rightstyle.rightbarlistitems}><FamilyRestroomIcon className={Rightstyle.leftbaricon} /> <span className={Rightstyle.spantext}>Nwankwo Family</span></li>
                </ul>
                <button className={Rightstyle.morebutton}>More</button>
            </div>
        </div>
    )
}

export default Rightbar;