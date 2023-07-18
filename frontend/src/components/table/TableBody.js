import DeleteForeverOutlinedIcon from '@mui/icons-material/DeleteForeverOutlined';
import Avatar from '@mui/material/Avatar';
import CheckBoxOutlineBlankOutlinedIcon from '@mui/icons-material/CheckBoxOutlineBlankOutlined';
import Tablebodystyle from "./TableStyle.module.css";

function TableBody({myIndividuals}) {
    let renderedIndividuals;

    return (
        <tbody>
            {
                renderedIndividuals = myIndividuals.map((individual, index) => ( 
                    <tr key={index} className={Tablebodystyle.row1}>
                        <td>
                        <div className={Tablebodystyle.checkboxdiv}>
                            {/* <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox}/> */}
                            <div className={Tablebodystyle.avatardiv}>
                                <Avatar />
                                <div className={Tablebodystyle.namediv}>
                                    <h3 className={Tablebodystyle.namedivh3}>{individual.myName}</h3>
                                    {/* <p className={Tablebodystyle.namedivparag}>@{individual.myName}</p> */}
                            </div>     
                            </div>
                        </div>
                        </td>
                        {/* <td className={Tablebodystyle.dataname}>{individual.myGender == 'm' ? 'Male': 'Female'}</td> */}
                        <td className={Tablebodystyle.dataname}>{individual.myGender}</td>
                        <td className={Tablebodystyle.dataname}>{individual.mother.name}</td>
                        <td className={Tablebodystyle.dataname}>{individual.father.name}</td>
                        <td className={Tablebodystyle.dataname}>{individual.spouses.map((elt, index)=> {
                            return index == 0 ? elt.name : ', '+elt.name
                        })}</td>
                        <td className={Tablebodystyle.dataname}>
                        {individual.children.map((elt, index)=> {
                            return index == 0 ? elt.name : ', '+elt.name
                        })}
                        </td>
                        {/* <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td> */}
                    </tr> 
                ))
            }
           
        </tbody>
    )
}

export default TableBody;