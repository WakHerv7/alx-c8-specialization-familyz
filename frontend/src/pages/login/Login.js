import Loginstyle from "./Login.module.css";
import { Link } from "react-router-dom";

function Login() {
    return (
        <div className={Loginstyle.logincontainer}>
            <h1>Welcome back!</h1>
            <form>
                <input className={Loginstyle.logininput} type="email" placeholder="Email Address" />
                <input className={Loginstyle.logininput} type="password" placeholder="Password" />
                <Link to={"/"}><button className={Loginstyle.loginbutton}>Continue</button></Link>
            </form>
            <p className={Loginstyle.loginparagraph}>
                Don't have an account?
                <Link className={Loginstyle.loginparagraph} to="/signup">Sign up</Link>
                
            </p>

            <button className={Loginstyle.loginbutton}>Continue with Google</button><br></br>
            <button className={Loginstyle.loginbutton}>Continue with Apple</button>
        </div>
    )
}

export default Login;