import type ICommonRecord from "./commonRecord";

export type IAction = {
    type: string,
    payload: ICommonRecord
}

export default IAction;
