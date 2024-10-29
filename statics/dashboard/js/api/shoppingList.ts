import { IMercadonaCategory } from '../interfaces/mercadona';
import _base from './_base';
import urls from './urls.json';

export const getMercadonaProducts = (): Promise<IMercadonaCategory> => (
    _base.get(urls.shoppingList.getMercadonaProducts)
);

export default {
    getMercadonaProducts,
}