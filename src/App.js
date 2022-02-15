import axios from 'axios';
import React, { useState } from 'react'; 
import { Outlet, Link, useNavigate } from 'react-router-dom';

import './styles.css'

export function App(props) {

    // Initialize states of variables
    const [playerName, setPlayername] = useState('');
    const [serverName, setServername] = useState('');
    const [email, setEmail] = useState('');
    const [stats, setStats] = useState('');

    let navigate = useNavigate();

    // Handle functions for the form
    const handleplayerNameChange = (e) => {
        setPlayername(e.target.value)
    }

    const handleserverNameChange = (e) => {
        setServername(e.target.value)
    }

    const handleemailChange = (e) => {
        setEmail(e.target.value)
    }

    const handlestatsChange = (e) => {
        setStats(e.target.files[0])
    }

    const handleSubmit = () => {
        
        // Only execute this if form is complete
        if ((playerName) && (serverName) && (stats) && (email)){  
            const formData = new FormData();
            formData.append(
                "stats",
                stats,
                stats.name
            );

            formData.append(
                "playername",
                playerName,
            );

            formData.append(
                "servername",
                serverName,
            );

            formData.append(
                "email",
                email,
            );
                        
            // Send data to server
            axios.post('/api/upload', formData)
            .then(function(response)
            {
                // When data is finally loaded, redirect to user page
                if (response.data === "Error 1"){
                    navigate('/develop/')
                } else {
                    navigate('/processing/');
                }
            })
        }
    }

    return ( 
        <div>
        <div className="App">
            <div className="left">
            <Link to="/"><h1>MC Wrapped</h1></Link>
            <div>
                MC Wrapped generates a stories like presentation of 
                your world or server stats. Generate yours and compare
                it with your friends!
            </div>
            <div>
                <h2>Generate your own</h2>
                <h3>Minecraft Name:</h3>
                <input type="text" name="playername" value={playerName} onChange={handleplayerNameChange}></input>
                <h3>Server or World Name:</h3>
                <input type="text" name="servername" value={serverName} onChange={handleserverNameChange}></input>
                <h3>Your Email:</h3>
                <input type="email" name="email" value={email} onChange={handleemailChange}></input>
                <h3>Select your stats file</h3>
                <input type="file" name="stats" onChange={handlestatsChange}></input>
                <button className="bn632-hover bn25" onClick={handleSubmit}>
                Upload! 
                </button>
                <div>
                <Link to="/stats">Where can I find my stats file?</ Link><br /><br />
                </div>
            </div>
            </div>
            <div className="stories">
                <img src="https://i.imgur.com/sDpIMQ9.png" width="360" height="640" />
            </div>
        </div>
            <div>
            <a href="https://twitter.com/search?q=%23mcwrapped&src=typed_query&f=top" target="_blank" rel="noopener noreferrer">Explore #mcwrapped on Twitter</a> |{" "}
            <Link to="/about">About</Link> |{" "}
            <Link to="/terms">Terms and conditions</Link>
            </div>
        <Outlet />
        </div>
    );
}


const stories = require('./example_slides.json');