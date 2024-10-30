import {
    ADD_SHOPPING_LIST_PRODUCT,
    CLOSE_SUPERMARKET_PRODUCTS,
    DISPLAY_SUPERMARKET_PRODUCTS,
    GET_CONSUM_PRODUCTS,
    GET_MERCADONA_PRODUCTS,
    GET_SHOPPING_LIST,
    REMOVE_SHOPPING_LIST_PRODUCT,
} from './action-types';


interface IAction<P = unknown> {
    type:
    | typeof ADD_SHOPPING_LIST_PRODUCT
    | typeof CLOSE_SUPERMARKET_PRODUCTS
    | typeof DISPLAY_SUPERMARKET_PRODUCTS
    | typeof GET_CONSUM_PRODUCTS
    | typeof GET_MERCADONA_PRODUCTS
    | typeof GET_SHOPPING_LIST
    | typeof REMOVE_SHOPPING_LIST_PRODUCT
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

export const getShoppingList = (supermarket: string): IAction => ({
    type: GET_SHOPPING_LIST,
    payload: { supermarket },
});

export const addShoppingListProduct = (productId: string, supermarket: string): IAction => ({
    type: ADD_SHOPPING_LIST_PRODUCT,
    payload: { productId, supermarket },
});

export const removeShoppingListProduct = (productId: string, supermarket: string): IAction => ({
    type: REMOVE_SHOPPING_LIST_PRODUCT,
    payload: { productId, supermarket },
});

export const getConsumProducts = (): IAction<string> => ({
    type: GET_CONSUM_PRODUCTS,
    payload: {},
});
