import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';

import shoppingListAPI from '@api/shoppingList';
import type {MercadonaCategoryProducts} from '@src/modules/shopping_list/interfaces';
import {
    GET_MERCADONA_PRODUCTS,
    GET_MERCADONA_PRODUCTS_SUCCESS,
} from './action-types';


export function* getMercadonaProducts(): Generator<StrictEffect, void, never> {
    const mercadonaProductsResponse: MercadonaCategoryProducts = yield call(shoppingListAPI.getMercadonaProducts);

    yield put({
        type: GET_MERCADONA_PRODUCTS_SUCCESS,
        payload: { mercadonaProducts: mercadonaProductsResponse },
    });
}

export default function* (): Generator {
    yield takeLatest(GET_MERCADONA_PRODUCTS, getMercadonaProducts);
}

