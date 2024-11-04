import { UnknownAction } from '@reduxjs/toolkit';
import { put, StrictEffect, takeLatest, select, call } from 'redux-saga/effects';

import { pushToHistory } from '@src/history';
import {
    REDIRECT_TO,
} from './action-types';
import type { IApiError, IAnyRecord, ISagaParam } from '@src/interfaces/global';


interface RedirectAction {
    type: string;
    payload: {
        url: string;
    };
}

export function* redirectTo({
    payload: { url },
}: RedirectAction): Generator<StrictEffect, void, never> {
    pushToHistory(url as string);
}

export default function* (): Generator {
    yield takeLatest(REDIRECT_TO, redirectTo);
}
