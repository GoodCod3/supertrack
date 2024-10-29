import helperReducer from '@src/helpers/reducer';
import type IAction from '@src/interfaces/action';

import {
    GET_MERCADONA_PRODUCTS_SUCCESS
} from './action-types';
import initialState from './state';
import type { IShoppingListState } from './interfaces';


const reducerMap = [
    GET_MERCADONA_PRODUCTS_SUCCESS,
];

const reducer = (state: IShoppingListState = initialState, action: IAction): Record<string, unknown> => (
    helperReducer(state, action, reducerMap)
);

export default reducer;