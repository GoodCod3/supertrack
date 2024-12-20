import React, { useEffect, useState } from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import type {
    MercadonaCategoryProducts,
    MercadonaShoppingList,
    MercadonaSearchFilteredResult,
    IConsumCategoryProducts,
    IConsumSearchFilteredResult,
    ConsumShoppingList,
} from '@src/modules/shopping_list/interfaces';
import { filterResults } from '@src/modules/shopping_list/helpers';
import ShoppingListMercadona from './components/ShoppingListMercadona';
import ShoppingListConsum from './components/ShoppingListConsum';


type IShoppingListPageProps = {
    addShoppingListProduct: (productId: string, supermarket: string) => void,
    removeShoppingListProduct: (productId: string, supermarket: string) => void,
    findLowestShoppingList: (supermarket: string) => void,
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
    consumProducts: IConsumCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
    mercadonaShoppingList: MercadonaShoppingList,
    consumShoppingList: ConsumShoppingList,
};


const ShoppingListPage = ({
    addShoppingListProduct,
    closeSupermarketProducts,
    consumProducts,
    consumShoppingList,
    displaySupermarketProducts,
    findLowestShoppingList,
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
    const [mercadonaFilteredResults, setMercadonaFilteredResults] = useState<MercadonaSearchFilteredResult[]>([]);
    const [consumFilteredResults, setConsumFilteredResults] = useState<IConsumSearchFilteredResult[]>([]);

    useEffect(() => {
        getMercadonaProducts();
        getConsumProducts();
        getShoppingList();
    }, []);

    useEffect(() => {
        if (searchTerm === '') {
            setMercadonaFilteredResults([]);
            setConsumFilteredResults([]);
            return;
        }
        if (searchTerm.length >= 3) {
            const mercadonaResults: MercadonaSearchFilteredResult[] = filterResults(searchTerm, mercadonaProducts);
            const consumResults: IConsumSearchFilteredResult[] = filterResults(searchTerm, consumProducts);
            
            setMercadonaFilteredResults(mercadonaResults);
            setConsumFilteredResults(consumResults);
        }

    }, [searchTerm, mercadonaProducts, consumProducts]);

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
                        findLowestShoppingList={findLowestShoppingList}
                        filteredResults={mercadonaFilteredResults}
                        searchTerm={searchTerm}
                    />
                </Tab>
                <Tab eventKey="consum" title="Consum">
                    <ShoppingListConsum
                        addShoppingListProduct={addShoppingListProduct}
                        closeSupermarketProducts={closeSupermarketProducts}
                        displaySupermarketProducts={displaySupermarketProducts}
                        isProductsDisplayed={isProductsDisplayed}
                        mercadonaProducts={consumProducts}
                        parentCategorySelected={parentCategorySelected}
                        productCategorySelected={productCategorySelected}
                        supermarketProductsSelected={supermarketProductsSelected}
                        mercadonaShoppingList={consumShoppingList}
                        removeShoppingListProduct={removeShoppingListProduct}
                        findLowestShoppingList={findLowestShoppingList}
                        filteredResults={consumFilteredResults}
                        searchTerm={searchTerm}
                    />
                </Tab>
            </Tabs>
        </React.Fragment>
    );
}

export default ShoppingListPage;
