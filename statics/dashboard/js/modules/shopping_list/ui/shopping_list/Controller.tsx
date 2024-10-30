import React, { useEffect, useState } from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import type {
    MercadonaCategoryProducts,
    MercadonaShoppingList,
    SearchFilteredResult,
} from '@src/modules/shopping_list/interfaces';
import ShoppingListMercadona from './components/ShoppingListMercadona';


type IShoppingListPageProps = {
    addShoppingListProduct: (productId: string) => void,
    removeShoppingListProduct: (productId: string) => void,
    getMercadonaProducts: () => void,
    getConsumProducts: () => void,
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
    mercadonaShoppingList: MercadonaShoppingList,
};

const filterResults = (
    searchTerm: string,
    products: MercadonaCategoryProducts
): SearchFilteredResult[] => {
    const lowerCasedTerm = searchTerm.toLowerCase();
    const results: SearchFilteredResult[] = [];

    Object.entries(products).forEach(([categoryName, subcategories]) => {
        let categoryMatch = categoryName.toLowerCase().includes(lowerCasedTerm);

        Object.entries(subcategories).forEach(([subcategoryName, products]) => {
            let subcategoryMatch = subcategoryName.toLowerCase().includes(lowerCasedTerm);

            const matchingProducts = products.filter((product) =>
                product.name.toLowerCase().includes(lowerCasedTerm)
            );

            if (categoryMatch || subcategoryMatch || matchingProducts.length > 0) {
                results.push({
                    categoryName,
                    subcategoryName,
                    products: matchingProducts,
                });
            }
        });
    });

    return results;
};

const ShoppingListPage = ({
    addShoppingListProduct,
    closeSupermarketProducts,
    displaySupermarketProducts,
    getConsumProducts,
    getMercadonaProducts,
    getShoppingList,
    isProductsDisplayed,
    mercadonaProducts,
    mercadonaShoppingList,
    parentCategorySelected,
    productCategorySelected,
    removeShoppingListProduct,
    supermarketProductsSelected,
}: IShoppingListPageProps) => {
    const [searchTerm, setSearchTerm] = useState<string>('');
    const [filteredResults, setFilteredResults] = useState<SearchFilteredResult[]>([]);

    useEffect(() => {
        getMercadonaProducts();
        getShoppingList();
        getConsumProducts();
    }, []);

    useEffect(() => {
        if (searchTerm === '') {
            setFilteredResults([]);
            return;
        }

        const results: SearchFilteredResult[] = filterResults(searchTerm, mercadonaProducts);
        setFilteredResults(results);
    }, [searchTerm, mercadonaProducts]);

    const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTerm(event.target.value);
    };


    return (
        <React.Fragment>
            <input
                type="text"
                placeholder="Buscar productos, categorías o subcategorías..."
                className="form-control mb-3"
                onChange={handleSearch}
                value={searchTerm}
            />
            <Tabs
                defaultActiveKey="mercadona"
                id="fill-tab-example"
                className="mb-3"
                fill
            >
                <Tab eventKey="mercadona" title="Mercadona">
                    <ShoppingListMercadona
                        addShoppingListProduct={addShoppingListProduct}
                        closeSupermarketProducts={closeSupermarketProducts}
                        displaySupermarketProducts={displaySupermarketProducts}
                        isProductsDisplayed={isProductsDisplayed}
                        mercadonaProducts={mercadonaProducts}
                        parentCategorySelected={parentCategorySelected}
                        productCategorySelected={productCategorySelected}
                        supermarketProductsSelected={supermarketProductsSelected}
                        mercadonaShoppingList={mercadonaShoppingList}
                        removeShoppingListProduct={removeShoppingListProduct}
                        filteredResults={filteredResults}
                        searchTerm={searchTerm}
                    />
                </Tab>
                <Tab eventKey="consum" title="Consum"></Tab>
            </Tabs>
        </React.Fragment>
    );
}

export default ShoppingListPage;
