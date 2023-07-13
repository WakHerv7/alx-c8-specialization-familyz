import TableHeader from "./TableHeader";
import TableBody from "./TableBody";
import Tablemain from "./TableStyle.module.css";

function Table() {
    return (
        <div>
            <table className={Tablemain.table}>
                <TableHeader />
                <TableBody />
            </table>
        </div>
        
    )
}


export default Table;