import { useState } from 'react'
import './App.css'
import Header from "./components/header/Header.jsx"
import Body from "./components/body/Body.jsx"
import SideBar from './components/sidebar/SideBar'

function App()
{
  return (
    <div>
      <div className="sidebar">
        <SideBar />
      </div>
      <div className="appcontent">
        <Header />
        <Body />
      </div>
    </div>
  )
}

export default App
