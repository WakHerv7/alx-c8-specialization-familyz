import Feedstyle from "./Feeds.module.css";
import Sharedfeeds from "../sharedfeeds/Sharedfeeds"
function Feeds() {
    return (
        <div className={Feedstyle.feeds}>
          <Sharedfeeds />  
            
        </div>
    )
}

export default Feeds;