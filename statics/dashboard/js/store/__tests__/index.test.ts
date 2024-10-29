/* eslint-env node, jest */
import { configureStore } from '@reduxjs/toolkit';

import configureStoreFunc from '../';


jest.mock('@reduxjs/toolkit', () => ({
    configureStore: jest.fn(() => ({
        dispatch: jest.fn(),
    })),
}));

jest.mock('redux-saga', () => jest.fn(() => ({
    run: 'RUN_TEST'
})));

jest.mock('@src/reducers', () => 'REDUCERS');

describe('SPA -> Store', () => {
    test('Store function will create store and register middlewares', () => {
        configureStoreFunc();

        const expectedConfigureStoreParams = { "middleware": [{ run: 'RUN_TEST' }], "reducer": "REDUCERS" };

        expect(configureStore).toBeCalledWith(expectedConfigureStoreParams);
    });
});
