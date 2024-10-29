/* eslint-disable @typescript-eslint/no-unsafe-call */
import React from 'react';
import { Provider } from 'react-redux';
import { History } from 'history';
import type { Store } from 'redux';

import { generateHistory } from '@src/history';
import Routes from '@src/routes';
import configureStore from '@src/store';
import rootSagas from '@src/sagas';


type IProviderAppProps = Record<never, never>;

class ProviderApp extends React.Component {
    store: Store;
    history: History;
    
    constructor(props: IProviderAppProps) {
        super(props);

        this.store = configureStore();
        this.store.runSaga(rootSagas);

        this.history = generateHistory();
    }

    render(): React.ReactElement {
        return (
            <Provider store={this.store}>
                <Routes history={this.history} />
            </Provider>
        );
    }
}


export default ProviderApp;
