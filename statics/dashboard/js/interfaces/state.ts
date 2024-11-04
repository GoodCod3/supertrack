import type { IShoppingListState } from "@src/modules/shopping_list/interfaces";
import type ICommonRecord from "./commonRecord";


export type IState = {
    routerReducer: ICommonRecord,
    shoppingListReducer: IShoppingListState
    
}

export default IState;
