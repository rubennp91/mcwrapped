import React from 'react';
import { Link } from 'react-router-dom';
export default function Develop () {
    return (
        <div className="other">
            <h2>It looks like your minecraft stats are not developed enough... Go back to the game and punch some trees!</h2>
            <Link to="/">Back to main page</Link>
        </div>
    );
}