import React from 'react';
import { Link } from 'react-router-dom';
export default function Stats () {
    return (
        <div className="other">
            <h1>Where can I find my stats file?</h1>
            The stats file is only provided if your version of Minecraft is <b>Java</b>. If you play on Bedrock, sorry!
            If you play on Java edition, you can find your stats file by navigating to your stats folder inside your worlds folder inside your minecraft folder.<br />
            The name of your stats file looks something like this:<br />
            <b>61699b2e-d327-4a01-9f1e-0ea8c3f06bc6</b>

            <h2>Windows Users</h2>
            To access your minecraft folder open a 'Run' window by pressing the <i>Windows Key + R</i> key and type <i>%APPDATA%/.minecraft/saves</i> then hit <i>Enter</i>. 
            Once you're there you will see all your saved worlds.
            Open the one you want and inside you'll find a <i>stats</i> folder. Inside there, there will be a file with a lot of numbers and letters, ending with <i>.json</i>. <br />
            That's the one!
            <h2>MAC Users</h2>
            To access your minecraft folder, press <i>Shift + Command + G</i> and Spotlight will open. Type <i>~/Library/Application Support/minecraft/saves</i> then hit Enter.
            Once you're there you will see all your saved worlds.
            Open the one you want and inside you'll find a <i>stats</i> folder. Inside there, there will be a file with a lot of numbers and letters, ending with <i>.json</i>. <br />
            That's the one!
            <h2>Linux Users</h2>
            You will find your worlds folder in <i>~/.minecraft/saves</i>. 
            Open the one you want and inside you'll find a <i>stats</i> folder. Inside there, there will be a file with a lot of numbers and letters, ending with <i>.json</i>. <br />
            That's the one!<br /><br />
            <Link to="/">← Back</Link>
        </div>
    );
}