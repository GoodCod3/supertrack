import React, { useEffect, useState } from 'react';

import ShoppingListCategories from '@components/ShoppingListCategories';
import {getMercadonaProducts} from '@api/shoppingList';

type IShoppingListPageProps =  {
    getMercadonaProducts: () => void,
    mercadonaProducts: string,
};

const ShoppingListPage = ({getMercadonaProducts, mercadonaProducts}:IShoppingListPageProps) => {
    useEffect(() => {
        getMercadonaProducts();
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <ShoppingListCategories />
        </React.Fragment>
    );
}

export default ShoppingListPage;
