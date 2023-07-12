import CheckBoxOutlineBlankOutlinedIcon from '@mui/icons-material/CheckBoxOutlineBlankOutlined';
import Tableheadstyle from "./TableStyle.module.css";


function TableHeader() {
    return (
        <thead>
            <tr className={Tableheadstyle.row1}>
                <th className={Tableheadstyle.firstthead}><div className={Tableheadstyle.thead}><CheckBoxOutlineBlankOutlinedIcon className={Tableheadstyle.checkbox} />
                    <div className={Tableheadstyle.spandiv}><h3>Name</h3></div>
                </div></th>
                <th>Gender</th>
                <th>Mother</th>
                <th>Father</th>
                <th>Spouse</th>
                <th>Children</th>
                <th>Remove</th>
            </tr>
        </thead>
    )
}

export default TableHeader;