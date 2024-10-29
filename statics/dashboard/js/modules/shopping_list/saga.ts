import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';
import { UnknownAction } from '@reduxjs/toolkit';

import {
    GET_MERCADONA_PRODUCTS,
} from './action-types';


export function* getMercadonaProducts(): Generator<StrictEffect, void, never> {
    console.log('si');
}

export default function* (): Generator {
    yield takeLatest(GET_MERCADONA_PRODUCTS, getMercadonaProducts);
}
