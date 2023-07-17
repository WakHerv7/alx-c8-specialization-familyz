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
import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import {  selectIndividualById, fetchIndividuals, selectAllIndividuals,  getIndividualsStatus, getIndividualsError, fetchIndividualById }from '../../reducers/IndividualSlice';
import {  selectPostById, fetchPosts, selectAllPosts,  getPostsStatus, getPostsError, fetchPostById }from '../../reducers/PostSlice';

function Sharedfeeds(props) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    // --------------------------------------------------------
    // const oneIndividual = useSelector(selectAllIndividuals);
    // const individualsStatus = useSelector(getIndividualsStatus);
    // const individualsError = useSelector(getIndividualsError);
    // useEffect(() => {
    //     if (individualsStatus === 'idle') {
    //         dispatch(fetchIndividualById({id:4}))            
    //     }
    //     else if (individualsStatus === 'succeeded') {
    //         console.log("======================")
    //         console.log("myIndividuals:", oneIndividual)
    //         console.log("======================")
    //     }
    // }, [individualsStatus, dispatch])
    // --------------------------------------------------------
    const myPosts = useSelector(selectAllPosts);
    const postsStatus = useSelector(getPostsStatus);
    const postsError = useSelector(getPostsError);
    useEffect(() => {
        if (postsStatus === 'idle') {
            dispatch(fetchPosts())            
        }
        else if (postsStatus === 'succeeded') {
            console.log("======================")
            console.log("myPosts:", myPosts)
            console.log("======================")
        }
    }, [postsStatus, dispatch])
    // --------------------------------------------------------

    function dateDifference(dateText) {
        let date1 = new Date()
        let date2 = new Date(dateText)
        const millisecondsInMinute = 1000 * 60;
        const millisecondsInHour = millisecondsInMinute * 60;
        const millisecondsInDay = millisecondsInHour * 24;

        const diffMilliseconds = Math.abs(date1 - date2);
        
        const days = Math.floor(diffMilliseconds / millisecondsInDay);
        const hours = Math.floor((diffMilliseconds % millisecondsInDay) / millisecondsInHour);
        const minutes = Math.floor((diffMilliseconds % millisecondsInHour) / millisecondsInMinute);
        // console.log("days:", days)
        // console.log("hours:", hours)
        // console.log("minutes:", minutes)
        // console.log("======================")
        // return { days: daysDifference, hours: hoursDifference };
        return `${days>0 ? days+' days,': ''} ${hours>0 ? hours+' hours ': ''}${minutes>0 ? minutes+' minutes': ''} ago`
      }

    let renderedPosts;
    if (postsStatus === 'loading') {
        renderedPosts = <tr><td>...</td></tr>;
    } else if (postsStatus === 'succeeded' && Array.isArray(myPosts)) {
        // renderedPosts =  <Table myPosts= {myPosts.family}/>
        renderedPosts = myPosts.map((post, index) => ( 
            <div key={index} className={Sharedstyle.feedswrapper}>
                <div className={Sharedstyle.secondfeedsfirstdiv}>
                    <div className={Sharedstyle.leftbaravatar}>
                        <Avatar/>
                        {/* <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photoone} /> */}
                    </div>
                    <div className={Sharedstyle.leftbarnames}>
                        <h3>{post.author.myName}</h3>
                        <p className={Sharedstyle.ptext}>@{post.author.myUsername}</p>
                    </div>
                    <div className={Sharedstyle.time}>
                        <small className={Sharedstyle.timeptext}>{dateDifference(post.created_at)}</small>
                        {/* <span>{post.created_at}</span> */}
                    </div>
                </div>
                <div className={Sharedstyle.secondfeedsseconddiv}>
                    <h3>{post.title}</h3>
                    <p className={Sharedstyle.ptext}>{post.content}</p>
                    {/* <img className={Sharedstyle.secondfeedsphotoicon} alt="posted-pic" src={postpic} /> */}
                </div>
                <hr/>
                <div className={Sharedstyle.secondfeedsthirddiv}>
                    <div className={Sharedstyle.thumbout}>
                        <ThumbUpOutlinedIcon />
                        <p className={Sharedstyle.likes}><span className={Sharedstyle.dot}>.</span> {post?.likes?.length} Likes</p>
                    </div>
                    <div className={Sharedstyle.comments}> <p className={Sharedstyle.commentstext}>{post?.comments?.length} comments</p></div>
                </div>
                {post.comments.map((comment, index) => (<>
                    <div className={Sharedstyle.secondfeedsfourthdiv}>
                        <div className={Sharedstyle.commenterpic}>
                            {/* <Avatar className={Sharedstyle.profilepic} alt="Remy Sharp" src={photo2} /> */}
                            <Avatar/>
                        </div>
                        <div className={Sharedstyle.commentinput}>
                            <small>{comment.author_name}</small>
                            <p className={Sharedstyle.commentparagraph}>{comment.content}</p>
                        </div>
                        
                    </div>
                </>))}
                <div className={Sharedstyle.feedssharediv}>
                    <input placeholder="Say something..." />
                    <div className={Sharedstyle.feedssendicon}><SendIcon className={Sharedstyle.sendicon} /></div>
                </div>
            </div>
        ))

    } else if (postsStatus === 'failed') {
        renderedPosts = {postsError};
    }

    return (
        <div>
            <div className={Sharedstyle.feedswrapper}>
                <input placeholder="What's on your mind?" />
                <div className={Sharedstyle.feedssharediv}>
                    <PhotoIcon className={Sharedstyle.photoicon} />
                    <button className={Sharedstyle.feedssharebutton}>Share</button>
                </div>
            </div>

            {renderedPosts}
            {/* <div className={Sharedstyle.feedswrapper}>
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
            </div> */}

        </div>
    );
}

export default Sharedfeeds;

