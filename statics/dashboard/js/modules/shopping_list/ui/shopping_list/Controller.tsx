import React, { useEffect } from 'react';
import Accordion from 'react-bootstrap/Accordion';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';
import ShoppingListMercadona from './components/ShoppingListMercadona';


type IShoppingListPageProps = {
    addShoppingListProduct: (productId: string) => void,
    getMercadonaProducts: () => void,
    closeSupermarketProducts: () => void,
    getShoppingList: () => void,
    displaySupermarketProducts: (
        supermarketSelected: string,
        parentCategorySelected: string,
        productCategorySelected?: string | null,
    ) => void,
    mercadonaProducts: MercadonaCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
};

const ShoppingListPage = ({
    addShoppingListProduct,
    closeSupermarketProducts,
    displaySupermarketProducts,
    getMercadonaProducts,
    getShoppingList,
    isProductsDisplayed,
    mercadonaProducts,
    parentCategorySelected,
    productCategorySelected,
    supermarketProductsSelected,
}: IShoppingListPageProps) => {
    useEffect(() => {
        getMercadonaProducts();
        getShoppingList();
    }, []);

    return (
        <React.Fragment>
            <input type="text" id="searchInput" placeholder="Buscar productos..." className="form-control mb-3" />
            <Accordion defaultActiveKey="0">
                <Accordion.Item eventKey='shopping-list'>
                    <Accordion.Header>Mi lista de la compra</Accordion.Header>
                    <Accordion.Body>
                        Aún no has agregado ningún producto.
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
            <ShoppingListMercadona
                addShoppingListProduct={addShoppingListProduct}
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
