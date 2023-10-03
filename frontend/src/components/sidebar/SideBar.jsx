// Sidebar.jsx
import React from 'react';
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
                    <li>Classify</li>
                    <li>Corrector</li>
                    <li>About</li>
                </ul>
            </div>
        </div>
    );
}

export default SideBar;
