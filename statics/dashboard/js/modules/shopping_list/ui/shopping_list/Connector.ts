import { connect } from 'react-redux';

import {
    addShoppingListProduct,
    closeSupermarketProducts,
    displaySupermarketProducts,
    findLowestShoppingList,
    getConsumProducts,
    getMercadonaProducts,
    getShoppingList,
    removeShoppingListProduct,
} from '@src/modules/shopping_list/actions';
import type ICommonRecord from '@src/interfaces/commonRecord';
import type IState from '@src/interfaces/state';

import Controller from './Controller';


export const mapStateToProps = (state: IState): ICommonRecord => ({
    mercadonaProducts: state.shoppingListReducer.mercadonaProducts,
    isProductsDisplayed: state.shoppingListReducer.isProductsDisplayed,
    supermarketProductsSelected: state.shoppingListReducer.supermarketProductsSelected,
    parentCategorySelected: state.shoppingListReducer.parentCategorySelected,
    productCategorySelected: state.shoppingListReducer.productCategorySelected,
    mercadonaShoppingList: state.shoppingListReducer.mercadonaShoppingList,
    consumShoppingList: state.shoppingListReducer.consumShoppingList,
    consumProducts: state.shoppingListReducer.consumProducts,
});

export const mapActionsToProps = {
    addShoppingListProduct,
    closeSupermarketProducts,
    displaySupermarketProducts,
    findLowestShoppingList,
    getConsumProducts,
    getMercadonaProducts,
    getShoppingList,
    removeShoppingListProduct,
};

export default connect(
    mapStateToProps,
    mapActionsToProps,
)(Controller);