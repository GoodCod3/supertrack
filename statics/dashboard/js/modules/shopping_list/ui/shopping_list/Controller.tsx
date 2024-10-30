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

    const defaultActiveKeys = filteredResults.map((_, index) => `search-result-list-${index}`);

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
                    <Accordion defaultActiveKey="0">
                        <Accordion.Item eventKey='shopping-list'>
                            <Accordion.Header>
                                Mi lista de la compra
                                {mercadonaShoppingList?.products?.length > 0 && (
                                    <span> (Total: {mercadonaShoppingList.total} €)</span>
                                )}
                            </Accordion.Header>
                            <Accordion.Body>
                                {mercadonaShoppingList?.products?.length > 0 ? (
                                    <ol className='list-group list-group-numbered'>
                                        {mercadonaShoppingList.products.map((product, productIndex) => (
                                            <li
                                                className='list-group-item d-flex justify-content-between align-items-start'
                                                key={`product-${productIndex}`}
                                            >
                                                <img src={product.image} className="card-img-top" style={{ "width": "4rem" }} loading="lazy" />
                                                <div className="ms-2 me-auto">
                                                    <div className="product-name-shopping-list">{product.name}</div>
                                                    <div className="fw-bold product-name-shopping-list">{product.total_price} €</div>
                                                </div>
                                                <span className="badge text-bg-primary rounded-pill">{product.quantity}</span>
                                                <button
                                                    className="btn btn-danger btn-sm ms-2 remove-product"
                                                    onClick={() => removeShoppingListProduct(product.id)}
                                                >
                                                    Eliminar
                                                </button>
                                            </li>

                                        ))}
                                    </ol>
                                ) : (
                                    <span>Aún no has agregado ningún producto.</span>
                                )}
                            </Accordion.Body>
                        </Accordion.Item>
                    </Accordion>
                    {!!searchTerm && filteredResults.length > 0 ? (
                        filteredResults.map((filteredResult, filteredResultIndex) => (
                            <React.Fragment key={`search-result-list-${filteredResultIndex}`}>
                                <h2>{filteredResult.categoryName}</h2>
                                <Accordion defaultActiveKey={defaultActiveKeys} alwaysOpen>
                                    <Accordion.Item eventKey={`search-result-list-${filteredResultIndex}`} >
                                        <Accordion.Header>
                                            {filteredResult.subcategoryName}
                                        </Accordion.Header>
                                        <Accordion.Body>
                                            <ol
                                                className="list-group list-group-numbered"
                                                key={`product-list${filteredResult.subcategoryName}-${filteredResultIndex}`}
                                            >
                                                {filteredResult.products.map((product, productIndex) => (
                                                    <Card.Link
                                                        onClick={() => addShoppingListProduct(product.id)}
                                                        key={`product-${product.id}`}
                                                    >
                                                        <li
                                                            className='list-group-item d-flex justify-content-between align-items-start'
                                                            key={`product-${filteredResult.subcategoryName}-${filteredResultIndex}-${productIndex}`}
                                                        >
                                                            <img src={product.image} className="card-img-top" style={{ "width": "4rem" }} loading="lazy" />
                                                            <div className="ms-2 me-auto">
                                                                <div className="fw-bold">{product.name} ({product.price} €)</div>
                                                            </div>
                                                        </li>

                                                    </Card.Link>
                                                ))}
                                            </ol>
                                        </Accordion.Body>
                                    </Accordion.Item>
                                </Accordion>
                            </React.Fragment>

                        ))

                    ) : (
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
                    )}
                </Tab>
                <Tab eventKey="consum" title="Consum"></Tab>
            </Tabs>
        </React.Fragment>
    );
}

export default ShoppingListPage;
