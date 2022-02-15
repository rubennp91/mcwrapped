import React from 'react';
import { Link } from 'react-router-dom';
export default function NotFound () {
    return (
        <div className="other">
            <h1>404</h1><br />
            <img src="https://i.imgur.com/Fdc3avG.png" /><br />
            Whatever you were looking for is not here...<br /><br />
            <Link to="/">Back to main page</Link>
        </div>
    );
}