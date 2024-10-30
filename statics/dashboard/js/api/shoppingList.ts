import { IMercadonaCategory } from '../interfaces/mercadona';
import _base from './_base';
import urls from './urls.json';

export const getMercadonaProducts = (): Promise<IMercadonaCategory> => (
    _base.get(urls.shoppingList.getMercadonaProducts)
);

export const getShoppingList = (): Promise<IMercadonaCategory> => (
    _base.get(urls.shoppingList.getMercadonaShoppingList)
);

export const addShoppingListProduct = (productId: string): Promise<IMercadonaCategory> => (
    _base.post(urls.shoppingList.addMercadonaShoppingListProduct, { productId })
);

export default {
    addShoppingListProduct,
    getMercadonaProducts,
    getShoppingList,
}