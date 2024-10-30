import {
    GET_MERCADONA_PRODUCTS,
    DISPLAY_SUPERMARKET_PRODUCTS,
} from './action-types';


interface IAction<P = unknown> {
    type:
    | typeof GET_MERCADONA_PRODUCTS
    | typeof DISPLAY_SUPERMARKET_PRODUCTS
    payload?: Record<string, P>;
}

export const getMercadonaProducts = (): IAction<string> => ({
    type: GET_MERCADONA_PRODUCTS,
    payload: {},
});

export const displaySupermarketProducts = (
    supermarketSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
): IAction<string | null> => ({
    type: DISPLAY_SUPERMARKET_PRODUCTS,
    payload: {
        supermarketSelected,
        parentCategorySelected,
        productCategorySelected,
    },
});
