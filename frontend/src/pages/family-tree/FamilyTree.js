import React, {useState, useEffect }from 'react';
import Header from "../../components/Header";
import FamilyTreestyle from  "./FamilyTree.module.css";
import Listpagestyle from  "../listpage/Listpage.module.css";
// import "./css/style_new_member.css";
// import "./css/style_upload_area.css";
import "./css/style.css";
import {containerH1,
    mysvgcontainerStyle,
    svgStyle} from "./js/style.js";
import Table from "../../components/table/Table";
import Leftbar from "../../components/leftbar/Leftbar";
import AddIcon from '@mui/icons-material/Add';
import {BuildFamilyTree} from './js/BuildFamilyTree';
import { Link, useNavigate } from 'react-router-dom';
import { useSelector, useDispatch }from 'react-redux';
import { selectAllIndividuals,  getIndividualsStatus, getIndividualsError, fetchIndividuals }from '../../reducers/IndividualSlice';

function FamilyTree() {
    const svgContainer = React.useRef();
    const svgImage = React.useRef();

    const dispatch = useDispatch();    
    const navigate = useNavigate();
    // console.log("process.env.REACT_APP_API_URL :", process.env.REACT_APP_API_URL)
    // --------------------------------------------------------
    const myIndividuals = useSelector(selectAllIndividuals);
    const individualsStatus = useSelector(getIndividualsStatus);
    const individualsError = useSelector(getIndividualsError);
    useEffect(() => {
        if (individualsStatus === 'idle') {
            dispatch(fetchIndividuals())            
        }
        else if (individualsStatus === 'succeeded') {
            console.log("======================")
            console.log("myIndividuals:", myIndividuals)
            console.log("======================")
            Array.isArray(myIndividuals.family) && BuildFamilyTree({
                response: myIndividuals, 
                svgImage: svgImage.current,
                svgContainer:svgContainer.current,
                manyCircles: svgImage.current.querySelector("#manyCircles"), 
                svgLines: svgImage.current.querySelector("#manyLines"),
                svgCouples: svgImage.current.querySelector("#manyCouples"),
                svgCircleTexts: svgImage.current.querySelector("#manyCircleTexts"), 
                svgCircleTextsBottom: svgImage.current.querySelector("#manyCircleTextsBottom"),
            })
        }
    }, [individualsStatus, dispatch])
    // --------------------------------------------------------
    // const svgContainer = React.useRef();
    // const svgImage = React.useRef();
    const zoomValue = React.useRef();
    
    const viewBox = React.useRef(
        {
            x:54,
            y:135,
            w:984,
            h:1535            
        }
    );
    const svgSize = React.useRef(
        {
            w:0,
            h:0            
        }
    );
    const isPanning = React.useRef(false);
    const startPoint = React.useRef({x:0,y:0});
    const endPoint = React.useRef({x:0,y:0});
    const scale = React.useRef(1);
    // let viewBox = {
    //     x:54,
    //     y:135,
    //     w:984,
    //     h:1535            
    // };

    // React.useEffect(()=>{
    //     svgImage.current.setAttribute(
    //         'viewBox', 
    //         `${viewBox.current.x} ${viewBox.current.y} ${viewBox.current.w} ${viewBox.current.h}`
    //     );
    //     svgSize.current.w = svgImage.current.clientWidth
    //     svgSize.current.h = svgImage.current.clientHeight
    //     // let isPanning = false;
    //     // let startPoint = {x:0,y:0};
    //     // let endPoint = {x:0,y:0};;
    //     // let scale = 1;        
    //     svgContainer.current.addEventListener("mousewheel", (e) => {
    //         e.preventDefault();
    //         let w = viewBox.current.w;
    //         let h = viewBox.current.h;
    //         let mx = e.offsetX;//mouse x  
    //         let my = e.offsetY;    
    //         let dw = w*Math.sign(e.deltaY)*0.1;
    //         let dh = h*Math.sign(e.deltaY)*0.1;
    //         let dx = dw*mx/svgSize.current.w;
    //         let dy = dh*my/svgSize.current.h;            
    //         viewBox.current = {x:viewBox.current.x+dx,y:viewBox.current.y+dy,w:viewBox.current.w-dw,h:viewBox.current.h-dh};
    //         scale.current = svgSize.current.w/viewBox.current.w;
    //         console.log( svgSize.current) 
    //         console.log( viewBox.current)            
    //         console.log("scale : ", scale.current)            
    //         // zoomValue.current.innerText = `${Math.round(scale.current*100)/100}`;
    //         // zoomValue.current.innerText = `---${Math.round(viewBox.x)} - ${Math.round(viewBox.y)} - ${Math.round(viewBox.w)} - ${Math.round(viewBox.h)}`;
    //         svgImage.current.setAttribute('viewBox', `${viewBox.current.x} ${viewBox.current.y} ${viewBox.current.w} ${viewBox.current.h}`);
    //      });
    //      svgContainer.current.addEventListener("mousedown", (e) =>{
    //         isPanning.current = true;
    //         startPoint.current = {x:e.x,y:e.y};   
    //      });
    //     svgContainer.current.addEventListener("mousemove", (e) =>{
    //         if (isPanning.current){
    //             endPoint.current = {x:e.x,y:e.y};
    //             var dx = (startPoint.current.x - endPoint.current.x)/scale.current;
    //             var dy = (startPoint.current.y - endPoint.current.y)/scale.current;
    //             var movedViewBox = {x:viewBox.current.x+dx,y:viewBox.current.y+dy,w:viewBox.current.w,h:viewBox.current.h};
    //             svgImage.current.setAttribute('viewBox', `${movedViewBox.x} ${movedViewBox.y} ${movedViewBox.w} ${movedViewBox.h}`);
    //         }
    //      });
    //     svgContainer.current.addEventListener("mouseup", (e) =>{
    //         if (isPanning.current){ 
    //             endPoint.current = {x:e.x,y:e.y};
    //             var dx = (startPoint.current.x - endPoint.current.x)/scale.current;
    //             var dy = (startPoint.current.y - endPoint.current.y)/scale.current;
    //             viewBox.current = {x:viewBox.current.x+dx,y:viewBox.current.y+dy,w:viewBox.current.w,h:viewBox.current.h};
    //             svgImage.current.setAttribute('viewBox', `${viewBox.current.x} ${viewBox.current.y} ${viewBox.current.w} ${viewBox.current.h}`);
    //             isPanning.current = false;
    //         }
    //      });         
    //     svgContainer.current.addEventListener("mouseleave", (e) =>{
    //         isPanning.current = false;
    //      });
    // }, [])

    return (
        <>
        {/* {Array.isArray(myIndividuals.family) && <Header currentUser={myIndividuals.family[3]}/>} */}
        <div className={Listpagestyle.profilecontainer}>
            <h1 className={Listpagestyle.familymembers}>Family Tree</h1>
            <div className={Listpagestyle.renderedcontainer}>
                <div className={Listpagestyle.renderedtop}>
                    <Leftbar currentUser={Array.isArray(myIndividuals.family) && myIndividuals.family[3]}/>
                </div>
                
                <div class="container_wh">
            {/* <h1 
                style={containerH1}>
                Family tree
            </h1> */}
            {/* <div class="fm_menu">
                <ul>
                    <li><a href="#">Modifier</a></li>
                    <li><a href="#">Ajouter un conjoint</a></li>
                    <li><a href="#">Ajouter un enfant</a></li>
                </ul>
            </div> */}
            <div ref={svgContainer} id="mysvgcontainer" style={mysvgcontainerStyle}>
                {/* <div id="bg_screen0" class="bg_screen0 displayNone"></div> */}
                <svg 
                ref={svgImage} 
                id="mysvg" 
                width="100%" 
                height="100vh" 
                style={svgStyle}
                >

                    {/*

                    <defs>
                        <linearGradient id="g2" x1="-50%" x2="100%" y1="0%" y2="-30%">
                            <stop style="stop-color: rgb(12, 0, 66);" offset="0" />
                            <stop style="stop-color: rgb(0, 53, 18);" offset="1" />
                        </linearGradient>
                    </defs>
                    <rect style="fill: url(#g2);" stroke="green" stroke-width="10" height="100%" width="100%" y="1" x="1" /> 
                    
                    */}
                    
                    <g id="manyCouples"></g>
                    <g id="manyLines"></g>
                    <g id="manyCircles"></g>
                    <foreignObject id="modalScreen" x="0" y="0" width="100%" height="100%">
                        <div id="modalScreenDiv" class="modalScreenDiv displayNone">
                        </div>
                    </foreignObject>
                    <g id="manyCircleTexts"></g>
                    <g id="manyCircleTextsBottom"></g>
                    <g id="manyMenus"></g>
                
                    {/* <g stroke="black" stroke-width="3" fill="yellow">
                        <circle id="pointA" cx="318" cy="345" r="5" />
                        <circle id="pointB" cx="330" cy="345" r="5" />
                    </g>
                    <g stroke="red" stroke-width="3" fill="lightblue">
                        <circle id="pointC" cx="450" cy="345" r="5" />
                    </g>
                    <g stroke="green" stroke-width="3" fill="coral">
                        <circle id="pointD" cx="380" cy="124" r="5" />
                    </g>
                    <g stroke="black" stroke-width="3" fill="yellow">
                        <circle id="pointE" cx="504" cy="124" r="5" />
                        <circle id="pointF" cx="519" cy="124" r="5" />
                    </g> */}
                
                </svg>
            </div>
        </div>
               
            </div>
            
        </div>
        
        </>
        
        
    )
}

export default FamilyTree;