import React from 'react';
import { Link } from 'react-router-dom';
export default function About () {
    return (
        <div className="other">
            <h2>About MCWrapped</h2>
            <div>MC Wrapped is a project by <a href="https://twitter.com/ruben_np91" target="_blank" rel="noopener noreferrer">rubenlosud</a>.
            MC Wrapped is not affiliated to Mojang® or Minecraft®. All videos shown in MC Wrapped were recorded by rubenlosud using Minecraft Java Edition®.
            The music in the videos belongs to C418 and Lena Raine (Minecraft Studios Music)<br /><br />
            <h3>Why do I need to input my email?</h3>
            MCWrapped slides take a while to create and if you were to wait for them to be processed when there's a lot of people doing the same... You would
            be waiting for a long time. MCWrapped uses your email to send you the generated slides and nothing else. Mail will not be sent to you again unless
            you submit your data again. Your mail will not be shared with third parties or used for spam or advertisement (ours or otherwise.)
            <h3>How does the website work?</h3>
            The website takes your minecraft stats file and reads it for interesting data! It is designed for survival worlds so it won't probably work on
            creative stats files or other types of gameplay. For survival, some specific things need to have happened inside the world, if it's a new world
            it might not work either. If the website has not generated a MCWrapped for you and you think it's a mistake, please get in
            contact with me.
            <h3>Do you have any comments?</h3>
            Let's get in touch:
            <ul>
                <li>
                    Email me at webmaster@mcwrapped.online
                </li>
                <li>
                    Message me <a href="https://twitter.com/ruben_np91" target="_blank" rel="noopener noreferrer">on Twitter</a>
                </li>
            </ul>
            MC Wrapped is possible thanks to the internet and its magic! Check out the things that made MC Wrapped possible:
            <ul>
                <li>
                    <a href="https://www.npmjs.com/package/react-insta-stories" target="_blank" rel="noopener noreferrer">react-insta-stories</a> by mohitk05
                </li>
                <li>
                    <a href="https://www.npmjs.com/package/react-share" target="_blank" rel="noopener noreferrer">react-share</a> by nygardk
                </li>
                <li>
                    <a href="https://pypi.org/project/Pillow/" target="_blank" rel="noopener noreferrer">Pillow</a>
                </li>
                <li>
                    <a href="https://pypi.org/project/moviepy/" target="_blank" rel="noopener noreferrer">Moviepy</a>
                </li>
                <li>
                    <a href="https://github.com/RyanHecht/php-Minecraft-3D-Skin-Renderer" target="_blank" rel="noopener noreferrer">3D Skin Renderer</a> by RyanHecht
                </li>
                <li>
                    The animated cubes logo by <a href="https://isionindustries.myportfolio.com/" target="_blank" rel="noopener noreferrer">Ision Industries</a>
                </li>
                <li>
                    The font shown in the stories by <a href="https://www.dafont.com/craftron-gaming.d6128"target="_blank" rel="noopener noreferrer">Craftron Gaming</a>
                </li>
            </ul>
            <h3>Contribute to the project</h3>
            If you want to contribute to the project, share it with your friends!
            </div><br /><br />
            <Link to="/">← Back</Link>
        </div>
    );
}