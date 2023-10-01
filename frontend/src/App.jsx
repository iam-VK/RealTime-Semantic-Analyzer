import { useState } from 'react'
import './App.css'
import Header from "./components/header/Header.jsx"
import Body from "./components/body/Body.jsx"
import NavBar from './components/navbar/NavBar'

function App()
{
  return (
      <div>
        <Header />
        <Body />
        <NavBar />
      </div>
  )
}

export default App
