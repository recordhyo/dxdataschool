import React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import vodlist from "./components/vodlist";
import voddetail from "./components/voddetail";


function Router(){
 return(
    <BrowserRouter>
    <Routes>
        <Route path="/vods" element={vodlist}/>
        <Route path="/vods/:id" element={voddetail}/>
    </Routes>
    
    </BrowserRouter>
 )   
}

export default Router;