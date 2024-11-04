import { all, fork } from 'redux-saga/effects';

import shoppingListSagas from '@src/modules/shopping_list/saga';


export default function* sagas() {
    yield all([
        fork(shoppingListSagas),
    ]);
}