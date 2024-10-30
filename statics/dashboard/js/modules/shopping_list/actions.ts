import {
    CLOSE_SUPERMARKET_PRODUCTS,
    DISPLAY_SUPERMARKET_PRODUCTS,
    GET_MERCADONA_PRODUCTS,
} from './action-types';


interface IAction<P = unknown> {
    type:
    | typeof CLOSE_SUPERMARKET_PRODUCTS
    | typeof DISPLAY_SUPERMARKET_PRODUCTS
    | typeof GET_MERCADONA_PRODUCTS
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
): IAction<string | undefined | null> => ({
    type: DISPLAY_SUPERMARKET_PRODUCTS,
    payload: {
        supermarketSelected,
        parentCategorySelected,
        productCategorySelected,
    },
});

export const closeSupermarketProducts = (): IAction => ({
    type: CLOSE_SUPERMARKET_PRODUCTS,
    payload: {},
});
