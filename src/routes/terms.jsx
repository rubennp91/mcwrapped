import React from 'react';
import { Link } from 'react-router-dom';

export default function Terms () {
    return (
        <div className="other">
        <h2>Terms and Conditions</h2>
        MC Wrapped and mcrwrapped.online do not use cookies and do not collect any of your data besides the one you willingly provide when you submit your stats.
        Your data will not be sold to third parties. By using the service you agree to these terms and conditions.<br /><br />
        <Link to="/">← Back</Link>
        </div>
    );
}