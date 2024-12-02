import React from 'react';
import ReactDOM from 'react-dom/client';

import Provider from './Provider';
import 'bootstrap/dist/css/bootstrap.min.css';

const rootElement = document.getElementById('root');
if (rootElement) {
    const root = ReactDOM.createRoot(
        rootElement
    );

    root.render(
        <Provider />
    );
}
