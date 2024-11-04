import { mergeObject } from '@src/helpers/utils';
import type IAction from '@src/interfaces/action';
import type ICommonRecord from '@src/interfaces/commonRecord';


const reducer = (
    state: ICommonRecord,
    action: IAction,
    reducerMap: Array<string>,
): Record<string, unknown> => {
    const isValidAction: boolean = reducerMap.indexOf(action.type) !== -1;

    return isValidAction ? mergeObject(state, action.payload) : state;
};

export default reducer;