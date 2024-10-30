import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';

import shoppingListAPI from '@api/shoppingList';
import type {MercadonaCategoryProducts} from '@src/modules/shopping_list/interfaces';
import {
    GET_MERCADONA_PRODUCTS,
    GET_MERCADONA_PRODUCTS_SUCCESS,
    DISPLAY_SUPERMARKET_PRODUCTS,
    DISPLAY_SUPERMARKET_PRODUCTS_SUCCESS,
} from './action-types';
import { ISagaParam } from '@src/interfaces/global';


interface IDisplaySupermarketProductsSaga {
    supermarketSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
};

export function* getMercadonaProducts(): Generator<StrictEffect, void, never> {
    const mercadonaProductsResponse: MercadonaCategoryProducts = yield call(shoppingListAPI.getMercadonaProducts);

    yield put({
        type: GET_MERCADONA_PRODUCTS_SUCCESS,
        payload: { mercadonaProducts: mercadonaProductsResponse },
    });
}

export function* displaySupermarketProducts({payload}: ISagaParam<IDisplaySupermarketProductsSaga>): Generator<StrictEffect, void, never> {
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

export default function* (): Generator {
    yield takeLatest(GET_MERCADONA_PRODUCTS, getMercadonaProducts);
    yield takeLatest(DISPLAY_SUPERMARKET_PRODUCTS, displaySupermarketProducts);
}

