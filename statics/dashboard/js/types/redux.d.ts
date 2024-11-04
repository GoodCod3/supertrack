import * as Redux from 'redux'; // eslint-disable-line

declare module 'redux' {
    export interface Store {
        runSaga: any;
        close: any;
        dispatch: any;
    }
}