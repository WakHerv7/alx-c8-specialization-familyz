import React from 'react';
import { useRef, useState, useEffect } from "react";
import {
    generateRandomHSLColor,
    getFirst2Initials,
    toRadians,
    getById,
    isFMIncomingSpouse,
    getFMIndex,
    getFMParentIds,
    getCoupleByFMIds,
    removeDuplicates
} from './main.js';

export let gap_v = 450;
export let gap_h = 150;
export let largest_gen = null;
export let nb_gen = null;
export let family = null;
export let familyGenerations = null;
export let fmCoord = [];
export let fmCoupleCoord = [];
export let fmLineCoord = [];
export let lastCoupleId = 0
export let lastLineId = 0
export let radius = 40;
export let extraRadiusWidth = 8;
export let padding_h = 30;
export let padding_v = 30;

export function BuildFamilyTree({response, svgImage, svgContainer, manyCircles,  svgLines, svgCouples, svgCircleTexts, svgCircleTextsBottom}) {
    // const [gap_v, setGap_v] = useState(450);
    // const [gap_h, setGap_h] = useState(150);
    // const [largest_gen, setLargest_gen] = useState(null);
    // const [nb_gen, setNb_gen] = useState(null);
    // const [family, setFamily] = useState(null);
    // const [familyGenerations, setFamilyGenerations] = useState(null);
    // const [fmCoord, setFmCoord] = useState([]);
    // const [fmCoupleCoord, setFmCoupleCoord] = useState([]);
    // const [fmLineCoord, setFmLineCoord] = useState([]);
    // const [lastCoupleId, setLastCoupleId] = useState(0);
    // const [lastLineId, setLastLineId] = useState(0);
    // const [radius, setRadius] = useState(40);
    // const [extraRadiusWidth, setExtraRadiusWidth] = useState(8);
    // const [padding_h, setPadding_h] = useState(30);
    // const [padding_v, setPadding_v] = useState(30);
// ==========================================================================
// ==========================================================================
function createBallSvgCircle(id, x, y) {
    // const manyCirclesRef = useRef(null);
    // const [randomColor, setRandomColor] = useState("");
  
    // useEffect(() => {
    //   const manyCircles = manyCirclesRef.current;
      const circle = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "circle"
      );
      circle.setAttribute("class", `oneBall oneBall${id}`);
      circle.setAttribute("cx", x);
      circle.setAttribute("cy", y);
      circle.setAttribute("r", `${radius}`);
      circle.setAttribute(
        "style",
        `stroke:#ddd; fill:${generateRandomHSLColor()}; stroke-width: 1;`
      );
      manyCircles.append(circle);
  
      return () => {
        manyCircles.removeChild(circle);
      };
    // }, [id, x, y, generateRandomHSLColor()]);
  
    // useEffect(() => {
    //   setRandomColor(generateRandomHSLColor());
    // }, []);
  
    // return (
    //     <></>
    // //   <g id="manyCircles" ref={manyCirclesRef} />
    // );

}
// ==========================================================================
// ==========================================================================
function couple(x1, y1, x2, y2) {
    let rad = radius + extraRadiusWidth;
    let dx = x2-x1;
    let dy = y2-y1;
    let alpha = Math.atan(dx/dy);
    let beta = toRadians(180) - (alpha+toRadians(90));
    // const svgCouples = document.querySelector('#mysvg #manyCouples');
    let path0 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path0.setAttribute('class', `Couple`);
    path0.setAttribute('d', `M${x1 + ((rad)*Math.sin(beta))},${y1 - ((rad)*Math.cos(beta))} 
                            L${x2 + ((rad)*Math.sin(beta))},${y2 - ((rad)*Math.cos(beta))}
                            A30,30 0 0,1 ${x2 - ((rad)*Math.sin(beta))},${y2 + ((rad)*Math.cos(beta))}
                            L${x1 - ((rad)*Math.sin(beta))},${y1 + ((rad)*Math.cos(beta))}
                            A30,30 0 0,1 ${x1 + ((rad)*Math.sin(beta))},${y1 - ((rad)*Math.cos(beta))}`);

    // path0.setAttribute('d', `M${x1},${y1-rad} 
    //                         L${x2},${y2-rad}
    //                         A30,30 0 0,1 ${x2},${y2+rad}
    //                         L${x1},${y1+rad}
    //                         A30,30 0 0,1 ${x1},${y1-rad}`);

    // path0.setAttribute('d', `M${50},${50+(i*gap_v)-30} 
    //                         L${50+((j-1)*gap_h)},${50+(i*gap_v)-30}
    //                         A30,30 0 0,1 ${50+((j-1)*gap_h)},${50+(i*gap_v)+30}
    //                         L${50},${50+(i*gap_v)+30}
    //                         A30,30 0 0,1 ${50},${50+(i*gap_v)-30}`);
                            // L${50},${(i*gap_v)+30}
    path0.setAttribute('style', "stroke:#ffffff99; stroke-width:2; fill:none;");
    svgCouples.append(path0);
}
// ==========================================================================
// ==========================================================================
function createBallSvgInnerText(id, myname, myphoto=null, isIncomingSpouse, x, y) {
    // const svgCircleTexts = document.querySelector('#mysvg #manyCircleTexts');

    const circleTextTop0 = document.createElementNS("http://www.w3.org/2000/svg", "foreignObject");
    circleTextTop0.setAttribute('class', `oneBallTextInner oneBallTextInner${id}`);
    circleTextTop0.setAttribute('x', x-25);
    circleTextTop0.setAttribute('y', y-25);
    circleTextTop0.setAttribute('width', 50);
    circleTextTop0.setAttribute('height', 50);
    const div0 = document.createElement("div");
    if (myphoto) {
        circleTextTop0.setAttribute('x', x-45);
        circleTextTop0.setAttribute('y', y-45);
        circleTextTop0.setAttribute('width', 90);
        circleTextTop0.setAttribute('height', 90);
        div0.setAttribute('onclick',`openBallMenu("oneBallMenu${id}")`)
        div0.setAttribute('style','color: white; width:100%; height:100%; background-image:url("'+myphoto+'"); background-size:cover; background-position: center center; border-radius:50%; border: 2px solid white; text-align:center; font-size:22px; font-weight:bold; user-select: none; display: flex; align-items:center; justify-content:center;')


    } else {        
        div0.innerHTML = getFirst2Initials(myname);
        // div0.setAttribute('onclick',`openBallMenu("oneBallMenu${id}")`)
        div0.setAttribute('style','color: white; width:100%; height:100%; background:transparent; border-radius:50%; text-align:center; font-size:22px; font-weight:bold; user-select: none; display: flex; align-items:center; justify-content:center;')    
    }
    
    circleTextTop0.appendChild(div0);
    svgCircleTexts.append(circleTextTop0);


    // const svgManyMenus = document.querySelector('#mysvg #manyMenus');
    // const circleTextTop1 = document.createElementNS("http://www.w3.org/2000/svg", "foreignObject");
    // circleTextTop1.setAttribute('class', `oneBallMenu oneBallMenu${id} displayNone`);
    // circleTextTop1.setAttribute('id', `oneBallMenu${id}`);
    // circleTextTop1.setAttribute('x', x-1080);
    // circleTextTop1.setAttribute('y', `${y-1200}`);
    // if (isIncomingSpouse) {
    //     circleTextTop1.setAttribute('x', x-1038);
    //     circleTextTop1.setAttribute('y', `${y-1140}`);
    // }
    // // circleTextTop1.setAttribute('width', 200);
    // // circleTextTop1.setAttribute('height', 135);
    // circleTextTop1.setAttribute('width', `${2000}`);
    // circleTextTop1.setAttribute('height', `${2000}`);
    // const div1 = document.createElement("div");
    // if (isIncomingSpouse) {
    //     div1.innerHTML = `
    //     <ul>
    //         <li><a href="show_item/${id}">Show</a></li>
    //         <li><a href="update_item/${id}">Edit</a></li>
    //     </ul>
    //     `;
    // } else {
    //     div1.innerHTML = `
    //     <ul>
    //         <li><a href="show_item/${id}">Show</a></li>
    //         <li><a href="update_item/${id}">Edit</a></li>
    //         <li><a href="new_spouse/${id}">+ Add a spouse</a></li>
    //         <li><a href="new_child/${id}">+ Add a child</a></li>
    //     </ul>
    //     `;
    // }
    
    // div1.setAttribute('class','fm_menu ')
    // div1.setAttribute('onclick',`console.log("oneBallMenu${id}")`)
    // circleTextTop1.appendChild(div1);
    // svgManyMenus.append(circleTextTop1);

}

// ==========================================================================
// ==========================================================================

function createBallSvgLowerText(id, myname, x, y) {
    // const svgCircleTextsBottom = document.querySelector('#mysvg #manyCircleTextsBottom');

    const circleTextTop0 = document.createElementNS("http://www.w3.org/2000/svg", "foreignObject");

    circleTextTop0.setAttribute('class', `oneBallTextBottom oneBallTextBottom${id}`);
    circleTextTop0.setAttribute('x', x-50);
    circleTextTop0.setAttribute('y', y + radius + 15);
    circleTextTop0.setAttribute('width', 100);
    circleTextTop0.setAttribute('height', 70);

    const div0 = document.createElement("div");
    div0.innerHTML = myname;
    div0.setAttribute('style','color: white; text-align:center; width:100px; font-size:13px; font-weight:bold; user-select: none;')
    circleTextTop0.appendChild(div0);
    // let textNode = document.createTextNode(this.ballName);
    // circleTextTop0.appendChild(textNode);
    circleTextTop0.setAttribute('style', 'font-family: 3ds, sans-serif; fill: white; text-anchor: middle; font-size: 14px; text-shadow: 2px 2px 10px black; user-select: none;');

    svgCircleTextsBottom.append(circleTextTop0);
}

// ==========================================================================
// ==========================================================================
function initializeSvgZone(viewboxWidth, viewboxHeight) {
    // const svgImage = document.getElementById('mysvg');
    // const svgContainer = document.getElementById('mysvgcontainer');
    var viewBox = {
        x:-300,
        y:0,
        w:viewboxWidth,
        h:viewboxHeight
    };
    svgImage.setAttribute(
        'viewBox', 
        `${viewBox.x} ${viewBox.y} ${viewBox.w} ${viewBox.h}`
    );
    const svgSize = {
        w:svgImage.clientWidth,
        h:svgImage.clientHeight
    };
    // console.log("svgSize : ", svgSize)
    var isPanning = false;
    var startPoint = {x:0,y:0};
    var endPoint = {x:0,y:0};;
    var scale = 1;

    svgContainer.addEventListener("mousewheel", (e) => {
        e.preventDefault();
        var w = viewBox.w;
        var h = viewBox.h;
        var mx = e.offsetX;//mouse x  
        var my = e.offsetY;    
        var dw = w*Math.sign(e.deltaY)*0.1;
        var dh = h*Math.sign(e.deltaY)*0.1;
        var dx = dw*mx/svgSize.w;
        var dy = dh*my/svgSize.h;
        viewBox = {x:viewBox.x+dx,y:viewBox.y+dy,w:viewBox.w-dw,h:viewBox.h-dh};
        scale = svgSize.w/viewBox.w;
        // console.log("svgSize : ", svgSize)
        // console.log("viewboxWidth : ", viewboxWidth)
        // console.log("largest_gen['size'] : ", largest_gen["size"])
        // console.log("nb_gen : ", nb_gen)
        
        // console.log("viewBox : ", viewBox)
        // console.log("scale : ", scale)
        // zoomValue.innerText = `${Math.round(scale*100)/100}`;
        svgImage.setAttribute('viewBox', `${viewBox.x} ${viewBox.y} ${viewBox.w} ${viewBox.h}`);
    });

    svgContainer.addEventListener("mousedown", (e) =>{
        isPanning = true;
        startPoint = {x:e.x,y:e.y};   
    });
    
    
    svgContainer.addEventListener("mousemove", (e) =>{
        if (isPanning){
            endPoint = {x:e.x,y:e.y};
            var dx = (startPoint.x - endPoint.x)/scale;
            var dy = (startPoint.y - endPoint.y)/scale;
            var movedViewBox = {x:viewBox.x+dx,y:viewBox.y+dy,w:viewBox.w,h:viewBox.h};
            svgImage.setAttribute('viewBox', `${movedViewBox.x} ${movedViewBox.y} ${movedViewBox.w} ${movedViewBox.h}`);
        }
    });
    
    svgContainer.addEventListener("mouseup", (e) =>{
        if (isPanning){ 
            endPoint = {x:e.x,y:e.y};
            var dx = (startPoint.x - endPoint.x)/scale;
            var dy = (startPoint.y - endPoint.y)/scale;
            viewBox = {x:viewBox.x+dx,y:viewBox.y+dy,w:viewBox.w,h:viewBox.h};
            svgImage.setAttribute('viewBox', `${viewBox.x} ${viewBox.y} ${viewBox.w} ${viewBox.h}`);
            isPanning = false;
        }
    });
    
    svgContainer.addEventListener("mouseleave", (e) =>{
        isPanning = false;
    });
}
// ==========================================================================
// ==========================================================================

// draw a curvy line between point (startX,startY) and point (endX,endY)
function drawCurve(id, startX, startY, endX, endY) {
    // M
    var AX = startX;
    // console.log(AX);
    var AY = startY;
    // console.log(AY);
    // L
    var BX = startX;
    var BY = Math.abs(endY - startY) * 0.05 + startY;
    // C
    var CX = startX;
    var CY = (endY - startY) * 0.66  + startY;
    var DX = endX;
    var DY = (endY - startY) * 0.33 + startY;
    var EX = endX;
    var EY =  + endY;
    // L
    var FX = endX;
    var FY = endY;
    var path = 'M' + AX + ',' + AY;
    path += ' L' + BX + ',' + BY;
    path +=  ' ' + 'C' + CX + ',' + CY;
    path += ' ' + DX + ',' + DY;
    path += ' ' + EX + ',' + EY;
    // const svgLines = document.querySelector('#mysvg #manyLines');
    let path0 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path0.setAttribute('class', `Curved Line`);
    path0.setAttribute('d', path);
    path0.setAttribute('style', "stroke:#ffeb3b97; stroke-width:2; fill:none;");
    svgLines.append(path0);
}

// ==========================================================================
// ==========================================================================



// ==========================================================================
// ==========================================================================
// ==========================================================================


// ==========================================================================
// ==========================================================================
// ==========================================================================



// ==========================================================================
// ==========================================================================
// ==========================================================================


// ==========================================================================
// ==========================================================================
// ==========================================================================


function getFamilyMembers(response) {

    
    // setLargest_gen(response["largest_gen"]);
    // setNb_gen(response["nb_gen"]);
    // setFamily(response["family"]);
    // setFamilyGenerations(response["familyGenerations"]);
    largest_gen = response["largest_gen"];
    nb_gen = response["nb_gen"];    
    family = response["family"];
    familyGenerations = response["familyGenerations"];

    // const mySvg = document.getElementById('mysvg');

    // mySvg.setAttribute('width', `${50+(gap_h*largest_gen["size"])}px`);
    // mySvg.setAttribute('height', `${50+(gap_v*nb_gen)}px`);

    let parentTabAllGen = [];
    // let reorganizedGen = [];
    for (let i = 0; i < nb_gen; i++) {
        let parentTab = {"fm":[], "fmsp":[]};
        let reorganizedGen = {"fm":[], "fmsp":[]};
        if (i > 0) {
            parentTab["fm"] = parentTabAllGen[i-1]["fm"]
            parentTab["fmsp"] = parentTabAllGen[i-1]["fmsp"]                               

            for (let k = 0; k < parentTab["fm"].length; k++) {
                let parentHasChildren = false;
                for (let p = 0; p < familyGenerations[i].length; p++) {
                    let myParentIds = getFMParentIds(family, familyGenerations[i][p]);
                    if ((parentTab["fm"][k]["id"] == myParentIds["mother"] && myParentIds["mother"] != null) || 
                    (parentTab["fm"][k]["id"] == myParentIds["father"] && myParentIds["father"] != null)) {
                        reorganizedGen["fm"].push({
                            "id":familyGenerations[i][p], 
                            "children":0, 
                            "allChildren":0, 
                            "parentId": parentTab["fm"][k]["id"]
                        });
                        // parentTab["fm"][k]["children"]++
                        parentTabAllGen[i-1]["fm"][k]["children"]++;
                        parentTabAllGen[i-1]["fm"][k]["allChildren"]++;
                        parentHasChildren = true;
                    }                                        
                }
                if (parentHasChildren == false) {
                    reorganizedGen["fm"].push({
                        "id":null, 
                        "children":0, 
                        "allChildren":0, 
                        "parentId": parentTab["fm"][k]["id"]
                    });
                }
            }
            for (let k = 0; k < familyGenerations[i].length; k++) {
                let flag = false;
                for (let p = 0; p < reorganizedGen["fm"].length; p++) {
                    if (familyGenerations[i][k] == reorganizedGen["fm"][p]["id"]) {
                        flag = true;
                    }
                }
                if (flag == false) {
                    reorganizedGen["fmsp"].push({
                        "id":familyGenerations[i][k], 
                        "children":0, 
                        "allChildren":0, 
                        "parentId": null
                    });
                }
            }
            // console.log(reorganizedGen);
            reorganizedGen['fm'] = removeDuplicates(reorganizedGen['fm'])
            parentTabAllGen.push(reorganizedGen);
            // console.log(parentTabAllGen);
            // for (j = 0; j < reorganizedGen.length; j++) {                                
            //     let fm = {"id":reorganizedGen[j], "x":50+(j*gap_h), "y":50+(i*gap_v), "gender":null, "couples":[]}
            //     fmCoord.push(fm)
            // }
        } else {
            for (let j = 0; j < familyGenerations[i].length; j++) {
                let isIncomingSpouse = isFMIncomingSpouse(family, familyGenerations[i][j]);
                if (isIncomingSpouse == false) {
                    parentTab["fm"].push({"id":familyGenerations[i][j], "children":0, "allChildren":0, "parentId":null})
                } else {
                    parentTab["fmsp"].push({"id":familyGenerations[i][j], "children":0, "allChildren":0, "parentId":null})
                }
                
            }
            parentTabAllGen.push(parentTab)
        }
    }
    for (let i = nb_gen-1; i >=0; i--) {
        for (let j = 0; j < parentTabAllGen[i]["fm"].length; j++) {
            if (i > 0) {
                for (let k = 0; k < parentTabAllGen[i-1]["fm"].length; k++) {
                    if (parentTabAllGen[i]["fm"][j]["parentId"] == parentTabAllGen[i-1]["fm"][k]["id"]) {
                        let nn = parentTabAllGen[i]["fm"][j]["allChildren"];
                        if (nn > 0) {
                            nn = nn - 1;
                        }
                        // nn = parentTabAllGen[i]["fm"][j]["allChildren"] - 1;
                        // console.log(nn);
                        parentTabAllGen[i-1]["fm"][k]["allChildren"] += nn;
                        
                    }
                }
            }

        }
    }
    // console.log("parentTabAllGen[0] : ", parentTabAllGen[0])
    let largest_gen_x = {...largest_gen};
    largest_gen_x["size"] = parentTabAllGen[0]["fm"][0] ? parentTabAllGen[0]["fm"][0]?.allChildren : largest_gen["size"];                        
    largest_gen =  largest_gen_x;
    // console.log("largest_gen['size'] : ", largest_gen["size"])
    // setLargest_gen(largest_gen_x);
    console.log(parentTabAllGen);

    let distTab = [];
    let distTabxx = [];
    for (let i = nb_gen-1; i >=0; i--) {
        let j = 0;
        let prev_x = 0;
        let prev_x_sp = 0;
        let dist = [];
        let distxx = [];
        for (j = 0; j < parentTabAllGen[i]["fm"].length; j++) {
            dist.push(prev_x);
            if (parentTabAllGen[i]["fm"][j]["id"] == null) {
                prev_x += gap_h;
                // console.log('voluntary space')
                // console.log(parentTabAllGen[i]["fm"][j])
            } else {
                if (parentTabAllGen[i]["fm"][j]["allChildren"] > 0) {
                    // radius
                    let ll = (((parentTabAllGen[i]["fm"][j]["allChildren"]-1)*gap_h));
                    let xx = prev_x+(ll/2);
                    let fm = {"id":parentTabAllGen[i]["fm"][j]["id"], "x":xx, "y":50+(i*gap_v), "length": ll, "gender":null, "couples":[]}
                    fmCoord.push(fm)
                    distxx.push({"x":xx, "prev_x": prev_x, "length": ll, "allChildren": (parentTabAllGen[i]["fm"][j]["allChildren"])});
                    prev_x += ll+gap_h;
                } else {
                    
                    // let fm = {"id":parentTabAllGen[i]["fm"][j], "x":50+(j*gap_h), "y":50+(i*gap_v), "length":0, "gender":null, "couples":[]}
                    let fm = {"id":parentTabAllGen[i]["fm"][j]["id"], "x":prev_x, "y":50+(i*gap_v), "length":0, "gender":null, "couples":[]}
                    fmCoord.push(fm);
                    distxx.push({"x":prev_x, "prev_x": prev_x, "length": 0, "allChildren": (parentTabAllGen[i]["fm"][j]["allChildren"])});
                    prev_x += gap_h;
                    
                }
            }
            
            // createBallSvgCircle(familyGenerations[i][j], 50+(j*gap_h), 50+(i*gap_v))
            // createBallSvgInnerText(familyGenerations[i][j], 50+(j*gap_h), 50+(i*gap_v))
        }
        prev_x_sp = prev_x
        for (j = 0; j < parentTabAllGen[i]["fmsp"].length; j++) {                                
            let fm = {"id":parentTabAllGen[i]["fmsp"][j]["id"], "x":prev_x_sp, "y":50+(i*gap_v), "length":0, "gender":null, "couples":[]}
            fmCoord.push(fm);
            prev_x_sp += gap_h;
        }
        // couple(50, 50+(i*gap_v), 50+((j-1)*gap_h), 50+(i*gap_v)) 
        distTab.push(dist);
        distTabxx.push(distxx);                         
    }
    console.log("distTab : ");
    console.log(distTab);
    console.log("distTabxx : ");
    console.log(distTabxx);
    

    // lastCoupleId
    // fmCoupleCoord

    /**
     * CREATE COUPLES
     */
    for (let i = 0; i < fmCoord.length; i++) {
        let fm = getById(family, fmCoord[i]["id"])
        // console.log('fmCoord[i]["id"] : ', fmCoord[i]["id"])
        // console.log('fm : ', fm)
        if (fm) {
            fmCoord[i]["gender"] = fm["gender"]

            if (fmCoord[i]["couples"].length == 0) {
                // console.log("///")
                // console.log(fmCoord[i]["id"])
                // console.log("///")
                if(fm["spouses"].length > 0 && fm["spouses"].length <2) {
                    for (let j = 0; j < fm["spouses"].length; j++) {
                        let fmsp = getById(family, fm["spouses"][j]["id"])
                        
                        let fmc = getById(fmCoord, fm["spouses"][j]["id"])
                        let fmci = getFMIndex(fmCoord, fm["spouses"][j]["id"])
                        // console.log("///")
                        // console.log("fmCoord[i] : ", fmCoord[i])
                        // console.log("fmci : ", fmci)
                        if (fmsp["father"] == null && fmsp["mother"] == null && fmci>=0) {                                                
                            fmCoord[fmci]["x"] = fmCoord[i]["x"]+(gap_h/1.4);
                            fmc["x"] = fmCoord[i]["x"] + (gap_h/1.4)
                            // console.log("///")
                            // console.log(fmCoord[fmci])
                            // console.log(fmc)
                        }

                        if (fmc) {
                            let fmCouple = {"id":lastCoupleId, "id1":fmCoord[i]["id"], "id2":fmc["id"],
                                    "x1": fmCoord[i]["x"], "y1": fmCoord[i]["y"],
                                    "x2": fmc["x"], "y2": fmc["y"],
                                    "xmid": (fmCoord[i]["x"] + fmc["x"])/2,
                                    "ymid": fmc["y"]+radius + extraRadiusWidth
                                };
                            fmCoupleCoord.push(fmCouple);
                            fmCoord[i]["couples"].push(fmCouple["id"]);
                            fmCoord[fmci]["couples"].push(fmCouple["id"]);
                            lastCoupleId++
                        }
                    }
                }
                else if(fm["spouses"].length >= 2) {
                    for (let j = 0; j < fm["spouses"].length; j++) {
                        let fmsp = getById(family, fm["spouses"][j]["id"])                                            
                        let fmc = getById(fmCoord, fm["spouses"][j]["id"])
                        let fmci = getFMIndex(fmCoord, fm["spouses"][j]["id"])

                        if (fmsp["father"] == null && fmsp["mother"] == null) {                                                
                            fmCoord[fmci]["x"] = gap_h*j*2
                            fmc["x"] = gap_h*j*2
                        }
                    }
                    let nb_sp = fm["spouses"].length;
                    let largeur_sp = (nb_sp-1) * gap_h*2;
                    // console.log("largeur_sp : ", largeur_sp);
                    let xmidlsp = largeur_sp/2;
                    // console.log("xmidlsp : ", xmidlsp);
                    // console.log("fmCoord[i][x] : ", fmCoord[i]["x"]);
                    let dxx = fmCoord[i]["x"] - xmidlsp;
                    // console.log("dxx : ", dxx);

                    for (let j = 0; j < fm["spouses"].length; j++) {
                        let fmsp = getById(family, fm["spouses"][j]["id"])
                        
                        let fmc = getById(fmCoord, fm["spouses"][j]["id"])
                        let fmci = getFMIndex(fmCoord, fm["spouses"][j]["id"])
                        // console.log("///")
                        // console.log("fmsp : ", fmsp)
                        // console.log("fmc : ", fmc)
                        // console.log("fmci : ", fmci)
                        if (fmsp["father"] == null && fmsp["mother"] == null) {                                                
                            fmCoord[fmci]["x"] = fmCoord[fmci]["x"];
                            fmc["x"] = fmc["x"]+dxx;
                            console.log("fmc[x] : ", fmc["x"]+dxx);
                            // debugger
                            // fmCoord[fmci]["y"] = fmCoord[i]["y"]+(gap_v/2)
                            fmc["y"] = fmCoord[i]["y"] + (gap_v/3.3)
                            
                            // console.log("///")
                            // console.log(fmCoord[fmci])
                            // console.log(fmc)
                        }

                        if (fmc) {
                            let fmCouple = {"id":lastCoupleId, "id1":fmCoord[i]["id"], "id2":fmc["id"],
                                    "x1": fmCoord[i]["x"], "y1": fmCoord[i]["y"],
                                    "x2": fmc["x"], "y2": fmc["y"],
                                    "xmid": fmc["x"],
                                    "ymid": fmc["y"]+radius + extraRadiusWidth
                                };
                            
                                console.log("fmCouple: ", fmCouple)

                            fmCoupleCoord.push(fmCouple);
                            fmCoord[i]["couples"].push(fmCouple["id"]);
                            fmCoord[fmci]["couples"].push(fmCouple["id"]);
                            lastCoupleId++
                        }
                    }
                }
            }
            
        }
        
    }


    /**
     * CREATE LINES
     */
        for (let i = 0; i < fmCoord.length; i++){
        let fm = getById(family, fmCoord[i]["id"])
        let mfCouple = null;
        let hasFatherSpouse = false; 
        let hasMotherSpouse = false;                     
        // console.log('fm : ', fm)
        if (fm) {
            // fm["father"] != null &&
            if (fm["mother"]["id"] != null) {
                // console.log('fm["mother"]["id"] : ', fm["mother"]["id"])
                // let fmmc = getById(fmCoord, fm["mother"])
                let fmm = getById(family, fm["mother"]["id"])
                // console.log('fmm : ', fmm)
                if (fmm) {
                    if (fmm["spouses"].length > 0) {
                        for (let j = 0; j < fmm["spouses"].length; j++) {
                            if (fm["father"]["id"] == fmm["spouses"][j]["id"]) {
                                hasFatherSpouse = true;
                                let fmf = getById(family, fm["father"]["id"])
                                mfCouple = getCoupleByFMIds(fmCoupleCoord, fmf["id"], fmm["id"])
                            }
                        }
                    }
                }
                // 
                if (mfCouple) {
                    console.log("mfCouple: ", mfCouple)
                    
                    let oneLine = {"id": lastLineId, "x1":fmCoord[i]["x"], "y1": fmCoord[i]["y"], "x2":mfCouple["xmid"], "y2":mfCouple["ymid"]}
                    fmLineCoord.push(oneLine)
                    // drawLine(lastLineId, fmCoord[i]["x"], fmCoord[i]["y"], mfCouple["xmid"], mfCouple["ymid"])
                    lastLineId++
                } else {
                    let fmmc = getById(fmCoord, fm["mother"]["id"])
                    // console.log("fmmc-mother : ", fmmc)
                    if (fmmc) {
                        let oneLine = {"id": lastLineId, "x1":fmCoord[i]["x"], "y1": fmCoord[i]["y"], "x2":fmmc["x"], "y2":fmmc["y"]}
                        fmLineCoord.push(oneLine)                                        
                        lastLineId++
                    }
                    
                }
            }
            if (fm["father"] != null && !hasFatherSpouse) {
                mfCouple = null;
                let fmm = getById(family, fm["father"]["id"])
                if (fmm) {
                    if (fmm["spouses"].length > 0) {
                        for (let j = 0; j < fmm["spouses"].length; j++) {
                            if (fm["mother"]["id"] == fmm["spouses"][j]["id"]) {
                                hasMotherSpouse = true;
                                let fmf = getById(family, fm["father"]["id"])
                                mfCouple = getCoupleByFMIds(fmCoupleCoord, fmf["id"], fmm["id"])
                            }
                        }
                    }
                }
                // 
                if (mfCouple) {
                    let oneLine = {"id": lastLineId, "x1":fmCoord[i]["x"], "y1": fmCoord[i]["y"], "x2":mfCouple["xmid"], "y2":mfCouple["ymid"]}
                    fmLineCoord.push(oneLine)                                        
                    lastLineId++
                } else {
                    let fmmc = getById(fmCoord, fm["father"]["id"])
                    console.log("fmmc-father: ", fmmc)
                    if (fmmc) {
                        let oneLine = {"id": lastLineId, "x1":fmCoord[i]["x"], "y1": fmCoord[i]["y"], "x2":fmmc["x"], "y2":fmmc["y"]}
                        fmLineCoord.push(oneLine)                                        
                        lastLineId++
                    }
                    
                }
            }
        }
        }


//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
//================================================================================
    // console.log("Family Members Coordinates", fmCoord)
    // console.log("Family Couples Coordinates", fmCoupleCoord)

    for (let i = 0; i < fmCoord.length; i++) {
        let fm = getById(family, fmCoord[i]["id"])
        
        if (!fm) {
            console.log("__fm__")
            console.log(fm)
            console.log(fmCoord[i])
        }
        if (fm) {
            createBallSvgCircle(fmCoord[i]["id"], fmCoord[i]["x"]+padding_h, fmCoord[i]["y"]+padding_v)
            createBallSvgInnerText(fmCoord[i]["id"], fm["myName"], fm["photo"], fm["isIncomingSpouse"], fmCoord[i]["x"]+padding_h, fmCoord[i]["y"]+padding_v)                            
            createBallSvgLowerText(fmCoord[i]["id"], fm["myName"], fmCoord[i]["x"]+padding_h, fmCoord[i]["y"]+padding_v)
        }
    }
    for (let i = 0; i < fmCoupleCoord.length; i++) {                            
        couple(fmCoupleCoord[i]["x1"]+padding_h, fmCoupleCoord[i]["y1"]+padding_v, fmCoupleCoord[i]["x2"]+padding_h, fmCoupleCoord[i]["y2"]+padding_v)
    }
    for (let i = 0; i < fmLineCoord.length; i++) {                            
        // drawLine(fmLineCoord[i]["id"], fmLineCoord[i]["x1"], fmLineCoord[i]["y1"], fmLineCoord[i]["x2"], fmLineCoord[i]["y2"])
        
        // console.log('fmLineCoord[i]["id"] : ', fmLineCoord[i]["id"])
        // console.log('padding_h : ', padding_h)
        // console.log('padding_v : ', padding_v)
        // console.log('fmLineCoord[i]["x1"]+padding_h : ', fmLineCoord[i]["x1"]+padding_h)
        // console.log('fmLineCoord[i]["y1"]+padding_v : ', fmLineCoord[i]["y1"]+padding_v)
        // console.log('fmLineCoord[i]["x2"] : ', fmLineCoord[i]["x2"])
        // console.log('fmLineCoord[i]["y2"]+padding_v : ', fmLineCoord[i]["y2"]+padding_v)
        
        drawCurve(fmLineCoord[i]["id"], fmLineCoord[i]["x1"]+padding_h, fmLineCoord[i]["y1"]+padding_v, fmLineCoord[i]["x2"]+padding_h, fmLineCoord[i]["y2"]+padding_v)
        
        
        
        // if (i == 0) {
        //     drawCurve(fmLineCoord[i]["id"], fmLineCoord[i]["x1"], fmLineCoord[i]["y1"], fmLineCoord[i]["x2"], fmLineCoord[i]["y2"])
        // }
    }

    // mySvg.setAttribute('width', `${50+(gap_h*largest_gen["size"])}px`);
    // mySvg.setAttribute('height', `${50+(gap_v*nb_gen)}px`);
    
    
    initializeSvgZone(500+(gap_h*largest_gen["size"]), 80+(gap_v*nb_gen))

    // console.log(allClients)
    // alert("ALL CLIENTS LIST SET !!!");


}


// ==========================================================================
// ==========================================================================
// ==========================================================================

    return (
        <>
            {getFamilyMembers(response)}
        </>
    );
}

// export default app;




