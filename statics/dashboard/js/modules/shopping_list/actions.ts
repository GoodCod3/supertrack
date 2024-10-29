import {
    GET_MERCADONA_PRODUCTS,
} from './action-types';


interface IAction<P = unknown> {
    type:
    | typeof GET_MERCADONA_PRODUCTS
    payload?: Record<string, P>;
}

export const getMercadonaProducts = (): IAction<string> => ({
    type: GET_MERCADONA_PRODUCTS,
    payload: {  },
});
