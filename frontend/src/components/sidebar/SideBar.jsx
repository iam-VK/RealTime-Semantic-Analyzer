// Sidebar.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './sidebar.css';
import HomeIcon from '@mui/icons-material/Home';

function SideBar()
{
    return (
        <div className="Sidebar">
            <div className="sidebar-content">
                <div className="sidebar-header">
                    <HomeIcon fontSize="large" />
                    <h3>Home</h3>
                </div>
                <ul className="sidebar-options">
                    <li><Link to="/classify-emotion">Emotion Analysis</Link></li>
                    <li><Link to="/classify-sentence">Sentence Analysis</Link></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </div>
        </div>
    );
}

export default SideBar;
