import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';



export interface IAction {
    type: string;
    payload?: Record<string, unknown>;
}

export type CustomReducer = Record<string, (state: Record<never, never>, action: IAction) => Record<string, unknown>>;

export type IAppGlobalState = Record<never, never>;

const reducers = {
    routerReducer,
    
} as IAppGlobalState;

export default combineReducers({ ...reducers });