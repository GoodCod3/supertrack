import helperReducer from '@src/helpers/reducer';
import type IAction from '@src/interfaces/action';

import {
    ADD_SHOPPING_LIST_PRODUCT_SUCCESS,
    CLOSE_SUPERMARKET_PRODUCTS_SUCCESS,
    DISPLAY_SUPERMARKET_PRODUCTS_SUCCESS,
    GET_MERCADONA_PRODUCTS_SUCCESS,
    GET_SHOPPING_LIST_SUCCESS,
    GET_CONSUM_PRODUCTS_SUCCESS,
} from './action-types';
import initialState from './state';
import type { IShoppingListState } from './interfaces';


const reducerMap = [
    ADD_SHOPPING_LIST_PRODUCT_SUCCESS,
    CLOSE_SUPERMARKET_PRODUCTS_SUCCESS,
    DISPLAY_SUPERMARKET_PRODUCTS_SUCCESS,
    GET_CONSUM_PRODUCTS_SUCCESS,
    GET_MERCADONA_PRODUCTS_SUCCESS,
    GET_SHOPPING_LIST_SUCCESS,
];

const reducer = (state: IShoppingListState = initialState, action: IAction): Record<string, unknown> => (
    helperReducer(state, action, reducerMap)
);

export default reducer;