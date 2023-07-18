import family from "./images/family.png";
import { Link } from "react-router-dom";
import Welcomestyle from "./Welcome.module.css";
import { Helmet } from 'react-helmet';

<Helmet bodyAttributes={{ style: 'background-color : #50a3a2' }} />

function Welcome() {
    return (
        <div className={Welcomestyle.welcomecontainer}>
            <Helmet>
                <style>{'body { background-color: background: #bae0e0; }'}</style>
            </Helmet>
            <img src={family} alt="family-logo" />
            <h1>Welcome to Familyz</h1>
            <p className={Welcomestyle.welcomeP}>
                A family tree web application designed to help users document and explore their family history in a visually appealing and interactive way. 
                {/* Log in with your account to continue */}
                </p>
            <div>
                <Link to="/login"><button className={Welcomestyle.welcomebutton}>Log in</button></Link>
                <Link to="/signup"><button className={Welcomestyle.welcomebutton}>Sign up</button></Link>
            </div>
        </div>
    )
}

export default Welcome;