import { connect } from 'react-redux';

import { 
    closeSupermarketProducts,
    displaySupermarketProducts,
    getMercadonaProducts, 
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
});

export const mapActionsToProps = {
    closeSupermarketProducts,
    displaySupermarketProducts,
    getMercadonaProducts,
};

export default connect(
    mapStateToProps,
    mapActionsToProps,
)(Controller);