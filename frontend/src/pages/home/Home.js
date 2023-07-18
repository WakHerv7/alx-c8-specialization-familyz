import Header from "../../components/Header";
import Rightbar from "../../components/rightbar/Rightbar";
import Feeds from "../../components/feedsbar/Feeds";
import Leftbar from "../../components/leftbar/Leftbar";
import Homestyle from "./Home.module.css";
function Home() {
    return (
        <>
            {/* <Header /> */}
            <main className={Homestyle.maincontainer}>
                <Leftbar />
                <Feeds />
                <Rightbar />
            </main>
        </>
    );
}

export default Home;
