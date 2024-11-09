import React from "react"
import {BrowserRouter,Routes,Route, Navigate} from "react-router-dom"
import Login from "./pages/login"
import Home from "./pages/home"
import  Register from "./pages/register"
import notFound from "./pages/notFound"
import ProtectedRoute from "./components/ProtectedRoute"

function Logout(){
    localStorage.clear()
    return <Navigate to="/login"/>
}

function RegisterAndLogout(){
    localStorage.clear()
    return <Register/>
}
function App() {
return(
    <BrowserRouter>
    <Routes>
        <Route path="/" element={
           <ProtectedRoute>
            <Home/>
             </ProtectedRoute>
        }
        />
        <Route path="/login" element={<Login/>}/>
        <Route path="/logout" element={<Logout/>}/>
        <Route path="/register" element={<RegisterAndLogout/>}/>
        <Route path="*" element={<notFound/>} />
    </Routes>
    </BrowserRouter>
)
}

export default App
