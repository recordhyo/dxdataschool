import React, {useEffect} from "react";
import ApiService from "../api/ApiService";

function voddetail() {
const Vod = ({id, apiid, vodname, director, actor, category, description, imgpath}) => {
    useEffect(()=> {

    }, []);

}

return (
    <div>
        <h2 className="text-center">{vodname}</h2>
            <img src={`https://image.tmdb.org/t/p/w300${imgpath}`} alt="posterimg"></img>

            <div className="text-end me-3"></div>
                <p className="text-center" color="gray">감독 : {director}</p>
                <p className="text-center" color="gray">배우 : {actor} </p>
            <br/>
            <hr />
            <br/>
            <div className="text-center">
                <p>{description}</p>
            </div>
            <br/>

    

    </div>
)
}

export default voddetail