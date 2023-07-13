import Myfamiliesstyle from "./Myfamilies.module.css";
import Header from "../../components/Header";
import { Helmet } from 'react-helmet';
import photo1 from "./images/photo1.jpg"

<Helmet bodyAttributes={{ style: 'background-color : #fff' }} />

function Myfamilies() {
    return (
        <div className={Myfamiliesstyle.myfamcontainer}>
            <Helmet>
                <style>{'body { background-color: #bae0e0; }'}</style>
            </Helmet>
            <Header />
            <div className={Myfamiliesstyle.myfamdiv}>
                <div className={Myfamiliesstyle.myfamdiv2}>
                    <div className={Myfamiliesstyle.myfamdivleft}>
                        <h1 className={Myfamiliesstyle.h1}>My Family</h1>
                        <button className={Myfamiliesstyle.button1}>See my family</button>
                    </div>
                    <div className={Myfamiliesstyle.myfamdivright}>
                        <button className={Myfamiliesstyle.button2}>Add new</button>
                    </div>
                </div>
            </div>
            <div className={Myfamiliesstyle.imagesdiv}>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
                <div className={Myfamiliesstyle.images}>
                    <div>
                        <img alt="familypic" src={photo1} className={Myfamiliesstyle.img}></img>
                    </div>
                    <button className={Myfamiliesstyle.imagetext}>Nwankwo Family</button>
                </div>
            </div>
        </div>
    )
}

export default Myfamilies;
