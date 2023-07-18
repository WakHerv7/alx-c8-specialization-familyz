import TableHeader from "./TableHeader";
import TableBody from "./TableBody";
import Tablemain from "./TableStyle.module.css";

function Table({myIndividuals}) {
    return (
        <div>
            <table className={Tablemain.table}>
                <TableHeader />
                <TableBody myIndividuals={myIndividuals}/>
            </table>
        </div>
        
    )
}


export default Table;