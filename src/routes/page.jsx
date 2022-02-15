import React, { useEffect, useState } from 'react';
import { Link, Navigate, useParams } from 'react-router-dom';
import Stories from 'react-insta-stories';
import { TwitterShareButton,
         TwitterIcon,
         FacebookShareButton,
         FacebookIcon,
         TelegramShareButton,
         TelegramIcon,
         WhatsappIcon,
         WhatsappShareButton,
         VKShareButton,
         VKIcon,
         RedditIcon,
         RedditShareButton,
         } from 'react-share';

import './styles.css'
import axios from 'axios';

export default function Page() {
    const { id } = useParams();
    const [slides, setSlides] = useState([]);
    const [error, setError] = useState(0);

    const shareURL = 'mcwrapped.online/page/' + id

       useEffect(() =>{
        axios
        .get('/api/getid', {
            params: {
                ID:id
            }
        })
        .then(res => {
            console.log(res.data)
            if (res.data === "Error 1"){
                setError(1)
            } else if (res.data === "Error 2"){
                setError(2)
            } else {
                setError(0)
                setSlides(res.data)
            }
        }); 
    }, [])

    if (error === 0){
        return(
            <div>
            <Link to="/"><h1>MC Wrapped</h1></Link>
            <div className="App">
                <div>
                    <Stories
                        stories={slides}
                        isPaused={true}
                    />
                    <div>
                        <h3 className="share">Share with your friends:</h3>
                        <TwitterShareButton className="shareIcons"
                            url={shareURL}
                            title={'Check my Minecraft Wrapped here:'}
                            hashtags={['minecraft', 'mcwrapped']}
                        >
                            <TwitterIcon size={32} round={true} />
                        </TwitterShareButton>
                        <FacebookShareButton className="shareIcons"
                            url={shareURL}
                            quote={'Check my Minecraft Wrapped here:'}
                            hashtag={'mcwrapped'}
                        >
                            <FacebookIcon size={32} round={true} />
                        </FacebookShareButton>
                        <TelegramShareButton className="shareIcons"
                            url={shareURL}
                            title={'Check my Minecraft Wrapped here:'}
                        >
                            <TelegramIcon size={32} round={true} />
                        </TelegramShareButton>
                        <WhatsappShareButton className="shareIcons"
                            url={shareURL}
                            title={'Check my Minecraft Wrapped here:'}
                            separator=" "
                        >
                            <WhatsappIcon size={32} round={true} />
                        </WhatsappShareButton>
                        <VKShareButton className="shareIcons"
                            url={shareURL}
                            title={'Check my Minecraft Wrapped here:'}
                        >
                            <VKIcon size={32} round={true} />
                        </VKShareButton>
                        <RedditShareButton className="shareIcons"
                            url={shareURL}
                            title={'Check my Minecraft Wrapped here:'}
                        >
                            <RedditIcon size={32} round={true} />
                        </RedditShareButton>

                    </div>
                </div>
            </div>
            <Link to="/"><h3>Generate yours!</h3></Link>
            </div>
        )
    } else if (error === 2) {
        return (
            <div>
            <h2>The username you're looking for cannot be found. Please try again.</h2>
            <Link to="/">Back to main page</Link>
            </div>
        )
    }
}