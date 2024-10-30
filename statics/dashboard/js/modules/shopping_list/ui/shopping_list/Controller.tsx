import React, { useEffect, useState } from 'react';

import ShoppingListMercadona from '@src/components/ShoppingListMercadona';
import type {MercadonaCategoryProducts} from '@src/modules/shopping_list/interfaces';


type IShoppingListPageProps =  {
    getMercadonaProducts: () => void,
    mercadonaProducts: MercadonaCategoryProducts,
};

const ShoppingListPage = ({getMercadonaProducts, mercadonaProducts}:IShoppingListPageProps) => {
    useEffect(() => {
        getMercadonaProducts();
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <ShoppingListMercadona mercadonaProducts={mercadonaProducts} />
        </React.Fragment>
    );
}

export default ShoppingListPage;
