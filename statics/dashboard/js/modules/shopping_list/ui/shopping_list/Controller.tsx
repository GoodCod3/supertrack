import React, { useEffect } from 'react';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';
import ShoppingListMercadona from './components/ShoppingListMercadona';


type IShoppingListPageProps = {
    getMercadonaProducts: () => void,
    displaySupermarketProducts: (supermarketSelected: string) => void,
    mercadonaProducts: MercadonaCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
};

const ShoppingListPage = ({
    getMercadonaProducts,
    mercadonaProducts,
    displaySupermarketProducts,
    isProductsDisplayed,
    supermarketProductsSelected,
    parentCategorySelected,
    productCategorySelected,
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
                isProductsDisplayed={isProductsDisplayed}
                supermarketProductsSelected={supermarketProductsSelected}
                parentCategorySelected={parentCategorySelected}
                productCategorySelected={productCategorySelected}
            />
        </React.Fragment>
    );
}

export default ShoppingListPage;
