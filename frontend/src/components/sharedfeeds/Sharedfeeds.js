import Sharedstyle from "./Sharedfeedstyle.module.css";
import postpic from "./images/postpic.jpg"
import PhotoIcon from '@mui/icons-material/Photo';
import Avatar from '@mui/material/Avatar';
import photoone from "../feedsbar/images/photoone.jpeg";
import photo2 from "../feedsbar/images/photo2.jpg";
import photo3 from "../feedsbar/images/photo3.jpg";
import photo4 from "../feedsbar/images/photo4.jpg";
import SendIcon from '@mui/icons-material/Send';
import ThumbUpOutlinedIcon from '@mui/icons-material/ThumbUpOutlined';
function Sharedfeeds(props) {
    return (
        <div>
            <div className={Sharedstyle.feedswrapper}>
                <input placeholder="What's on your mind?" />
                <div className={Sharedstyle.feedssharediv}>
                    <PhotoIcon className={Sharedstyle.photoicon} />
                    <button className={Sharedstyle.feedssharebutton}>Share</button>
                </div>
            </div>
            <div className={Sharedstyle.feedswrapper}>
                <div className={Sharedstyle.secondfeedsfirstdiv}>
                    <div className={Sharedstyle.leftbaravatar}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} />
                    </div>
                    <div className={Sharedstyle.leftbarnames}>
                        <h3>Chinwe Chukwuogor {props.name}</h3>
                        <p className={Sharedstyle.ptext}>@Kiraa_Daves {props.username}</p>
                    </div>
                    <div className={Sharedstyle.time}><p className={Sharedstyle.timeptext}>1h ago - Lagos, Nigeria</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsseconddiv}>
                    <img className={Sharedstyle.secondfeedsphotoicon} alt="posted-pic" src={postpic} />
                </div>
                <div className={Sharedstyle.secondfeedsthirddiv}>
                    <div className={Sharedstyle.thumbout}>
                        <ThumbUpOutlinedIcon />
                        <p className={Sharedstyle.likes}><span className={Sharedstyle.dot}>.</span> 10 Likes</p>
                    </div>
                    <div className={Sharedstyle.comments}> <p className={Sharedstyle.commentstext}>3 comments</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo2} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p className={Sharedstyle.commentparagraph}>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo2} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo2} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.feedssharediv}>
                    <input placeholder="Say something..." />
                    <div className={Sharedstyle.feedssendicon}><SendIcon className={Sharedstyle.sendicon} /></div>
                </div>
            </div>
            <div className={Sharedstyle.feedswrapper}>
                <div className={Sharedstyle.secondfeedsfirstdiv}>
                    <div className={Sharedstyle.leftbaravatar}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo3} />
                    </div>
                    <div className={Sharedstyle.leftbarnames}>
                        <h3>John Nnaemeka {props.name}</h3>
                        <p>@jhonny2 {props.username}</p>
                    </div>
                    <div className={Sharedstyle.time}><p>1h ago - Lagos, Nigeria</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsseconddiv}>
                    <img className={Sharedstyle.secondfeedsphotoicon} alt="posted-pic" src={postpic} />
                </div>
                <div className={Sharedstyle.secondfeedsthirddiv}>
                    <div className={Sharedstyle.thumbout}>
                        <ThumbUpOutlinedIcon />
                        <p className={Sharedstyle.likes}><span className={Sharedstyle.dot}>.</span> 10 Likes</p>
                    </div>
                    <div className={Sharedstyle.comments}> <p className={Sharedstyle.commentstext}>3 comments</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo4} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.feedssharediv}>
                    <input placeholder="Say something..." />
                    <div className={Sharedstyle.feedssendicon}><SendIcon className={Sharedstyle.sendicon} /></div>
                </div>
            </div>
            <div className={Sharedstyle.feedswrapper}>
                <div className={Sharedstyle.secondfeedsfirstdiv}>
                    <div className={Sharedstyle.leftbaravatar}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} />
                    </div>
                    <div className={Sharedstyle.leftbarnames}>
                        <h3>Chinwe Chukwuogor {props.name}</h3>
                        <p>@Kiraa_Daves {props.username}</p>
                    </div>
                    <div className={Sharedstyle.time}><p>1h ago - Lagos, Nigeria</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsseconddiv}>
                    <img className={Sharedstyle.secondfeedsphotoicon} alt="posted-pic" src={postpic} />
                </div>
                <div className={Sharedstyle.secondfeedsthirddiv}>
                    <div className={Sharedstyle.thumbout}>
                        <ThumbUpOutlinedIcon />
                        <p className={Sharedstyle.likes}><span className={Sharedstyle.dot}>.</span> 10 Likes</p>
                    </div>
                    <div className={Sharedstyle.comments}> <p className={Sharedstyle.commentstext}>3 comments</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.feedssharediv}>
                    <input placeholder="Say something..." />
                    <div className={Sharedstyle.feedssendicon}><SendIcon className={Sharedstyle.sendicon} /></div>
                </div>
            </div>
            <div className={Sharedstyle.feedswrapper}>
                <div className={Sharedstyle.secondfeedsfirstdiv}>
                    <div className={Sharedstyle.leftbaravatar}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} />
                    </div>
                    <div className={Sharedstyle.leftbarnames}>
                        <h3>Chinwe Chukwuogor {props.name}</h3>
                        <p>@Kiraa_Daves {props.username}</p>
                    </div>
                    <div className={Sharedstyle.time}><p className={Sharedstyle.commentstext}>1h ago - Lagos, Nigeria</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsseconddiv}>
                    <img className={Sharedstyle.secondfeedsphotoicon} alt="posted-pic" src={postpic} />
                </div>
                <div className={Sharedstyle.secondfeedsthirddiv}>
                    <div className={Sharedstyle.thumbout}>
                        <ThumbUpOutlinedIcon />
                        <p className={Sharedstyle.likes}><span className={Sharedstyle.dot}>.</span> 10 Likes</p>
                    </div>
                    <div className={Sharedstyle.comments}> <p className={Sharedstyle.commentstext}>3 comments</p></div>
                </div>
                <div className={Sharedstyle.secondfeedsfourthdiv}>
                    <div className={Sharedstyle.commenterpic}>
                        <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} />
                    </div>
                    <div className={Sharedstyle.commentinput}>
                        <h3>Anya Wright</h3>
                        <p>Gorgeous gorgeous gorgeous! Nothing like a mother and child photo. By the way your little one is growing up so fast! Good to see. xoxo</p>
                    </div>
                </div>
                <div className={Sharedstyle.feedssharediv}>
                    <input placeholder="Say something..." />
                    <div className={Sharedstyle.feedssendicon}><SendIcon className={Sharedstyle.sendicon} /></div>
                </div>
            </div>
        </div>
    );
}

export default Sharedfeeds;

