import { connect } from 'react-redux';

import { 
    getMercadonaProducts, 
    displaySupermarketProducts,
} from '@src/modules/shopping_list/actions';
import type ICommonRecord from '@src/interfaces/commonRecord';
import type IState from '@src/interfaces/state';

import HomeController from './Controller';


export const mapStateToProps = (state: IState): ICommonRecord => ({
    mercadonaProducts: state.shoppingListReducer.mercadonaProducts,
});

export const mapActionsToProps = {
    getMercadonaProducts,
    displaySupermarketProducts,
};

export default connect(
    mapStateToProps,
    mapActionsToProps,
)(HomeController);