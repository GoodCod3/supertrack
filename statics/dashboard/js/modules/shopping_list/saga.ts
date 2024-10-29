import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';

import shoppingListAPI from '@api/shoppingList';

import {
    GET_MERCADONA_PRODUCTS,
} from './action-types';


export function* getMercadonaProducts(): Generator<StrictEffect, void, never> {
    const partnersResponse: any = yield call(shoppingListAPI.getMercadonaProducts);

    console.log(partnersResponse);
}

export default function* (): Generator {
    yield takeLatest(GET_MERCADONA_PRODUCTS, getMercadonaProducts);
}

