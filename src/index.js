import React from 'react';
import ReactDOM from 'react-dom';
import { 
    BrowserRouter,
    Routes,
    Route,
 } from 'react-router-dom';

import { App } from './App';
import About from './routes/about';
import Terms from './routes/terms';
import Page from './routes/page';
import Stats from './routes/stats';
import NotFound from './routes/notfound';
import Develop from './routes/develop';
import Processing from './routes/processing';


const rootElement = document.getElementById('root');

ReactDOM.render(
    <BrowserRouter>
        <Routes>
            <Route path='*' element={<NotFound />} />
            <Route path="/" element={<App />} />
            <Route path="about" element={<About />} />
            <Route path="terms" element={<Terms />} />
            <Route path="stats" element={<Stats />} />
            <Route path="develop" element={<Develop />} />
            <Route path="processing" element={<Processing />} />
            <Route
                path="page/:id"
                element={<Page />}
            />
        </Routes>
    </BrowserRouter>,
    rootElement
    );
