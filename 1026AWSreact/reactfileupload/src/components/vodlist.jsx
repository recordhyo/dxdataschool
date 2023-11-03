import React, { useEffect, useState } from "react";
import ApiService from "../api/ApiService";


function vodlist() {
    const [vodList, setvodList] = useState([]);

    useEffect(() => {
        ApiService.LoadVOD().then(response => {
            setvodList(response.data);
            console.log(response.data)
        })
    }, []);
    return (
        <div>
            <h2 className="text-center">vod</h2>
            <br/>
            <br/>
            <hr />
            <br/>
                <List>
                    {vodList.map( (a)=> (
                    <ListItem key={a.id}>
                        <ListItemText>
                            <a href={`/voddetail/${a.id}`} className="text-decoration-none" ><h4 className="fs-2 text-body-emphasis">{a.title}</h4></a>
                        </ListItemText>
                    </ListItem>
                        ))}
                </List>

        </div>
    );
}

export default vodlist;