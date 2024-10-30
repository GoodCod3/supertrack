import React, { useEffect } from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';

import type {
    MercadonaCategoryProducts,
    MercadonaShoppingList,
} from '@src/modules/shopping_list/interfaces';
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
    mercadonaShoppingList: MercadonaShoppingList,
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
    mercadonaShoppingList,
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
                                        <div className="ms-2 me-auto ">
                                            <div className="product-name-shopping-list">{product.name}</div>
                                            <div className="fw-bold product-name-shopping-list">{product.total_price} €</div>
                                        </div>
                                        <span className="badge text-bg-primary rounded-pill">{product.quantity}</span>
                                        <button className="btn btn-danger btn-sm ms-2 remove-product" data-id="{{product.id}}">Eliminar</button>
                                    </li>

                                ))}
                            </ol>
                        ) : (
                            <span>Aún no has agregado ningún producto.</span>
                        )}
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
