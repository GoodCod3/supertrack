import {
    IConsumCategoryProducts,
    IMercadonaCategory,
    MercadonaShoppingList,
} from '@src/modules/shopping_list/interfaces';
import _base from './_base';
import urls from './urls.json';

export type IAddShoppingListProductResponse = {
    status: string,
    error?: string,
    message?: string,
};

export const getMercadonaProducts = (): Promise<IMercadonaCategory> => (
    _base.get(urls.shoppingList.getMercadonaProducts)
);

export const getShoppingList = (): Promise<MercadonaShoppingList> => (
    _base.get(urls.shoppingList.getMercadonaShoppingList)
);

export const addShoppingListProduct = (productId: string, supermarket: string): Promise<IAddShoppingListProductResponse> => (
    _base.post(urls.shoppingList.addMercadonaShoppingListProduct, { productId, supermarket })
);

export const removeShoppingListProduct = (productId: string): Promise<IAddShoppingListProductResponse> => (
    _base.post(urls.shoppingList.removeMercadonaShoppingListProduct, { productId })
);

export const getConsumProducts = (): Promise<IConsumCategoryProducts> => (
    _base.get(urls.shoppingList.getConsumProducts)
);

export default {
    addShoppingListProduct,
    getConsumProducts,
    getMercadonaProducts,
    getShoppingList,
    removeShoppingListProduct,
}