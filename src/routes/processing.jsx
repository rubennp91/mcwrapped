import React, { useEffect, useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import quotes from '../quotes.json';
import lottie from 'lottie-web';
import loadingLogo from '../loading.json'

export default function Processing () {

    const [quote, setQuote] = useState('Processing...');

    // Quotes
    const shuffle = useCallback(() => {
        const index = Math.floor(Math.random() * quotes.length);
        setQuote(quotes[index].quote)
    }, []);

    useEffect(() => {
        const intervalID = setInterval(shuffle, 3000);
        return () => clearInterval(intervalID);
    }, [shuffle])

    useEffect(() =>{
        lottie.loadAnimation({
            container: document.querySelector("#loading"),
            animationData: loadingLogo
        });
    }, []);

    return (
        <div className="other">
            <h2>We're processing your stats... You will receive an email when we are done.</h2>
            <div id="loading" className="loading-style" />
            <h2>{quote}</h2><br />
            <Link to="/">Back to main page</Link><br /><br />
            <a href="https://twitter.com/search?q=%23mcwrapped&src=typed_query&f=top">Explore <b>#MCWrapped</b> on Twitter while you wait</a>
        </div>
    );
}