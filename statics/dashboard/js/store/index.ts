import { Store } from 'redux';
import { configureStore, Tuple } from '@reduxjs/toolkit';
import createSagaMiddleware, { END } from 'redux-saga';

import rootReducer from '@src/reducers';


const configureStoreFunc = (): Store => {
    const sagaMiddleware = createSagaMiddleware({});

    const store = configureStore({
        reducer: rootReducer,
        middleware: () => new Tuple(sagaMiddleware)
    });

    store.runSaga = sagaMiddleware.run;
    store.close = (): END => store.dispatch(END);

    return store;
};

export default configureStoreFunc;