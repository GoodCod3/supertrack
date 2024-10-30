import React, { useEffect } from 'react';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';
import ShoppingListMercadona from './components/ShoppingListMercadona';


type IShoppingListPageProps = {
    getMercadonaProducts: () => void,
    closeSupermarketProducts: () => void,
    displaySupermarketProducts: (supermarketSelected: string) => void,
    mercadonaProducts: MercadonaCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
};

const ShoppingListPage = ({
    closeSupermarketProducts,
    displaySupermarketProducts,
    getMercadonaProducts,
    isProductsDisplayed,
    mercadonaProducts,
    parentCategorySelected,
    productCategorySelected,
    supermarketProductsSelected,
}: IShoppingListPageProps) => {
    useEffect(() => {
        getMercadonaProducts();
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <ShoppingListMercadona
                closeSupermarketProducts={closeSupermarketProducts}
                displaySupermarketProducts={displaySupermarketProducts}
                isProductsDisplayed={isProductsDisplayed}
                mercadonaProducts={mercadonaProducts}
                parentCategorySelected={parentCategorySelected}
                productCategorySelected={productCategorySelected}
                supermarketProductsSelected={supermarketProductsSelected}
            />
        </React.Fragment>
    );
}

export default ShoppingListPage;
