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
            {/* <tr className={Tablebodystyle.row1}>
                <td>
                <div className={Tablebodystyle.checkboxdiv}>
                    <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox}/>
                    <div className={Tablebodystyle.avatardiv}>
                        <Avatar />
                        <div className={Tablebodystyle.namediv}>
                            <h3 className={Tablebodystyle.namedivh3}>Olivia Rhye</h3>
                            <p className={Tablebodystyle.namedivparag}>@olivia</p>
                       </div>     
                    </div>
                </div>
                </td>
                <td className={Tablebodystyle.dataname}>Female</td>
                <td className={Tablebodystyle.dataname}>Michael</td>
                <td className={Tablebodystyle.dataname}>Maureen</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Lily</li>
                        <li>Michael Jnr</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox}/>
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox}/>
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}> 
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                    <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr>
            <tr className={Tablebodystyle.row1}>
                <td>
                    <div className={Tablebodystyle.checkboxdiv}>
                        <CheckBoxOutlineBlankOutlinedIcon className={Tablebodystyle.checkbox} />
                        <div className={Tablebodystyle.avatardiv}>
                            <Avatar />
                            <div className={Tablebodystyle.namediv}>
                                <h3>Phoenix Baker</h3>
                                <p>@phoenix</p>
                            </div>
                        </div>
                    </div></td>
                <td className={Tablebodystyle.dataname}>Male</td>
                <td className={Tablebodystyle.dataname}>Jacob</td>
                <td className={Tablebodystyle.dataname}>Michelle</td>
                <td className={Tablebodystyle.dataname}>Malimba</td>
                <td className={Tablebodystyle.dataname}>
                <ul className={Tablebodystyle.list}>
                        <li>Annabelle</li>
                        <li>Troy</li>
                        <li>Dylan</li>
                    </ul>
                </td>
                <td className={Tablebodystyle.dataname}><DeleteForeverOutlinedIcon /></td>
            </tr> */}
        </tbody>
    )
}

export default TableBody;