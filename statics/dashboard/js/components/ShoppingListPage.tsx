import React, { useEffect, useState } from 'react';

import ShoppingListCategories from './ShoppingListMercadona';
import {getMercadonaProducts} from '../api/shoppingList';

const ShoppingListPage = () => {
    useEffect(() => {
        console.log('s');
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <ShoppingListCategories />
        </React.Fragment>
    );
}

export default ShoppingListPage;
