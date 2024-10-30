import React, { useEffect } from 'react';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';
import ShoppingListMercadona from './components/ShoppingListMercadona';


type IShoppingListPageProps = {
    getMercadonaProducts: () => void,
    displaySupermarketProducts: (supermarketSelected: string) => void,
    mercadonaProducts: MercadonaCategoryProducts,
};

const ShoppingListPage = ({
    getMercadonaProducts,
    mercadonaProducts,
    displaySupermarketProducts,
}: IShoppingListPageProps) => {
    useEffect(() => {
        getMercadonaProducts();
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <ShoppingListMercadona
                mercadonaProducts={mercadonaProducts}
                displaySupermarketProducts={displaySupermarketProducts}
            />
        </React.Fragment>
    );
}

export default ShoppingListPage;
