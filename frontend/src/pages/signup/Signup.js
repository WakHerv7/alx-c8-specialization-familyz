import Signupstyle from "./Signup.module.css";
function Signup() {
    return (
        <div className={Signupstyle.logincontainer}>
            <h1>Create your account </h1>
            <p className={Signupstyle.signupparagraph}>Please note that phone verification may be required via your number  for security reasons.</p>
            <form>
                <input className={Signupstyle.signupinput} type="text" placeholder="First Name" />
                <input className={Signupstyle.signupinput} type="text" placeholder="Last Name" />
                <input className={Signupstyle.signupinput} type="tel" placeholder="Phone Number" />
                <input className={Signupstyle.signupinput} type="email" placeholder="Email Address" />
                <input className={Signupstyle.signupinput} type="password" placeholder="Password" />
                <button className={Signupstyle.signupbutton}>Continue</button>
            </form>
            <p className={Signupstyle.signupparagraph} >Already have an account? Log in</p>

            <button className={Signupstyle.signupbutton}>Continue with Google</button><br></br>
            <button className={Signupstyle.signupbutton}>Continue with Apple</button>
        </div>
    )
}

export default Signup;