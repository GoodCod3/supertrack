import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';
import { toast } from 'react-toastify';

import shoppingListAPI, {
    IAddShoppingListProductResponse,
} from '@api/shoppingList';
import type {
    IConsumCategoryProducts,
    IFindLowestShoppingList,
    MercadonaCategoryProducts,
    MercadonaShoppingList,
} from '@src/modules/shopping_list/interfaces';
import {
    ADD_SHOPPING_LIST_PRODUCT,
    CLOSE_SUPERMARKET_PRODUCTS_SUCCESS,
    CLOSE_SUPERMARKET_PRODUCTS,
    DISPLAY_SUPERMARKET_PRODUCTS_SUCCESS,
    DISPLAY_SUPERMARKET_PRODUCTS,
    GET_CONSUM_PRODUCTS,
    GET_MERCADONA_PRODUCTS_SUCCESS,
    GET_MERCADONA_PRODUCTS,
    GET_SHOPPING_LIST_SUCCESS,
    GET_SHOPPING_LIST,
    REMOVE_SHOPPING_LIST_PRODUCT,
    GET_CONSUM_PRODUCTS_SUCCESS,
    FIND_LOWEST_SHOPPING_LIST,
    FIND_LOWEST_SHOPPING_LIST_SUCCESS,
    GET_MERCADONA_SHOPPING_LIST,
    GET_CONSUM_SHOPPING_LIST,
} from './action-types';
import { ISagaParam } from '@src/interfaces/global';


interface IDisplaySupermarketProductsSaga {
    supermarketSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
};

interface IAddShoppingListProductSaga {
    productId: string,
    supermarket: string,
};

interface IFindLowestShoppingListSaga {
    supermarket: string,
};

export function* getMercadonaProducts(): Generator<StrictEffect, void, never> {
    const mercadonaProductsResponse: MercadonaCategoryProducts = yield call(shoppingListAPI.getMercadonaProducts);

    yield put({
        type: GET_MERCADONA_PRODUCTS_SUCCESS,
        payload: { mercadonaProducts: mercadonaProductsResponse },
    });
}

export function* displaySupermarketProducts({ payload }: ISagaParam<IDisplaySupermarketProductsSaga>): Generator<StrictEffect, void, never> {
    yield put({
        type: DISPLAY_SUPERMARKET_PRODUCTS_SUCCESS,
        payload: {
            supermarketProductsSelected: payload.supermarketSelected,
            parentCategorySelected: payload.parentCategorySelected,
            productCategorySelected: payload.productCategorySelected,
            isProductsDisplayed: true,
        },
    });
}

export function* closeSupermarketProducts(): Generator<StrictEffect, void, never> {
    yield put({
        type: CLOSE_SUPERMARKET_PRODUCTS_SUCCESS,
        payload: {
            supermarketProductsSelected: null,
            parentCategorySelected: null,
            productCategorySelected: null,
            isProductsDisplayed: false,
        },
    });
}

export function* getShoppingList(): Generator<StrictEffect, void, never> {
    yield put({type: GET_MERCADONA_SHOPPING_LIST, payload:{}});
    yield put({type: GET_CONSUM_SHOPPING_LIST, payload:{}});
}

export function* getMercadonaShoppingList(): Generator<StrictEffect, void, never> {
    const mercadonaProductsResponse: MercadonaShoppingList = yield call(
        shoppingListAPI.getShoppingList,
        'mercadona',
    );

    yield put({
        type: GET_SHOPPING_LIST_SUCCESS,
        payload: {
            mercadonaShoppingList: mercadonaProductsResponse,
        },
    });
}

export function* getConsumShoppingList(): Generator<StrictEffect, void, never> {
    const mercadonaProductsResponse: MercadonaShoppingList = yield call(
        shoppingListAPI.getShoppingList,
        'consum',
    );

    yield put({
        type: GET_SHOPPING_LIST_SUCCESS,
        payload: {
            consumShoppingList: mercadonaProductsResponse,
        },
    });
}

export function* addShoppingListProduct({ payload }: ISagaParam<IAddShoppingListProductSaga>): Generator<StrictEffect, void, never> {
    try {
        const mercadonaProductsResponse: IAddShoppingListProductResponse = yield call(
            shoppingListAPI.addShoppingListProduct,
            payload.productId,
            payload.supermarket,
        );
        if (mercadonaProductsResponse.status == "success") {
            yield put({ type: GET_SHOPPING_LIST, payload: { supermarket: payload.supermarket } });
            toast.success('Producto añadido a la lista');
        }
    } catch (error) {

    }
}

export function* removeShoppingListProduct({ payload }: ISagaParam<IAddShoppingListProductSaga>): Generator<StrictEffect, void, never> {
    try {
        const mercadonaProductsResponse: IAddShoppingListProductResponse = yield call(
            shoppingListAPI.removeShoppingListProduct,
            payload.productId,
            payload.supermarket,
        );
        if (mercadonaProductsResponse.status == "success") {
            yield put({ type: GET_SHOPPING_LIST, payload: { supermarket: payload.supermarket } });
        }
    } catch (error) {

    }
}

export function* getConsumProducts(): Generator<StrictEffect, void, never> {
    const consumProductsResponse: IConsumCategoryProducts = yield call(shoppingListAPI.getConsumProducts);

    yield put({
        type: GET_CONSUM_PRODUCTS_SUCCESS,
        payload: { consumProducts: consumProductsResponse },
    });
}

export function* findLowestShoppingList({ payload }: ISagaParam<IFindLowestShoppingListSaga>): Generator<StrictEffect, void, never> {
    try{
        const lowestResponse: IFindLowestShoppingList = yield call(
            shoppingListAPI.findLowestShoppingList,
            payload.supermarket
        );
    
        console.log(lowestResponse);

    }catch(error) {

    }
    // yield put({
    //     type: FIND_LOWEST_SHOPPING_LIST_SUCCESS,
    //     payload: { consumProducts: lowestResponse },
    // });
}


export default function* (): Generator {
    yield takeLatest(GET_MERCADONA_PRODUCTS, getMercadonaProducts);
    yield takeLatest(DISPLAY_SUPERMARKET_PRODUCTS, displaySupermarketProducts);
    yield takeLatest(CLOSE_SUPERMARKET_PRODUCTS, closeSupermarketProducts);
    yield takeLatest(GET_SHOPPING_LIST, getShoppingList);
    yield takeLatest(ADD_SHOPPING_LIST_PRODUCT, addShoppingListProduct);
    yield takeLatest(REMOVE_SHOPPING_LIST_PRODUCT, removeShoppingListProduct);
    yield takeLatest(GET_CONSUM_PRODUCTS, getConsumProducts);
    yield takeLatest(FIND_LOWEST_SHOPPING_LIST, findLowestShoppingList);
    yield takeLatest(GET_MERCADONA_SHOPPING_LIST, getMercadonaShoppingList);
    yield takeLatest(GET_CONSUM_SHOPPING_LIST, getConsumShoppingList);
}

