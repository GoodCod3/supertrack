import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ListGroup from 'react-bootstrap/ListGroup';
import Col from 'react-bootstrap/Col';
import Accordion from 'react-bootstrap/Accordion';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Offcanvas from 'react-bootstrap/Offcanvas';

import type {
    MercadonaCategoryProducts,
    MercadonaFilteredProductsResult,
    MercadonaShoppingList,
    MercadonaSearchFilteredResult,
} from '@src/modules/shopping_list/interfaces';


type IShoppingListCategories = {
    addShoppingListProduct: (productId: string, supermarket: string) => void,
    findLowestShoppingList: (supermarket: string) => void,
    mercadonaProducts: MercadonaCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string,
    parentCategorySelected: string,
    productCategorySelected?: string | null,
    closeSupermarketProducts: () => void,
    displaySupermarketProducts: (
        supermarketSelected: string,
        parentCategorySelected: string,
        productCategorySelected?: string | null,
    ) => void,
    searchTerm: string,
    mercadonaShoppingList: MercadonaShoppingList,
    removeShoppingListProduct: (productId: string, supermarket: string) => void,
    filteredResults: MercadonaSearchFilteredResult[],
};

const SUPERMARKET_NAME = 'mercadona';
const getProductsBySelection = (
    products: MercadonaCategoryProducts,
    categoryName: string,
    subcategoryName?: string | null
): MercadonaFilteredProductsResult => {
    if (subcategoryName) {
        return [
            {
                subcategoryName,
                products: products[categoryName][subcategoryName],
            },
        ];
    }

    return Object.entries(products[categoryName]).map(([subcatName, subcatProducts]) => ({
        subcategoryName: subcatName,
        products: subcatProducts,
    }));
};

const ShoppingListCategories = ({
    addShoppingListProduct,
    closeSupermarketProducts,
    displaySupermarketProducts,
    isProductsDisplayed,
    mercadonaProducts,
    parentCategorySelected,
    productCategorySelected,
    supermarketProductsSelected,
    searchTerm,
    mercadonaShoppingList,
    removeShoppingListProduct,
    filteredResults,
    findLowestShoppingList,
}: IShoppingListCategories) => {
    let filteredProducts: MercadonaFilteredProductsResult = [];
    if (isProductsDisplayed && parentCategorySelected && supermarketProductsSelected === SUPERMARKET_NAME) {
        filteredProducts = getProductsBySelection(mercadonaProducts, parentCategorySelected, productCategorySelected);
    }

    const entries = Object.entries(mercadonaProducts);
    const rows = [];
    for (let i = 0; i < entries.length; i += 2) {
        rows.push(entries.slice(i, i + 2));
    }
    const defaultActiveKeys = filteredResults.map((_, index) => `search-result-list-${index}`);
    return (
        <Container>
            {supermarketProductsSelected === SUPERMARKET_NAME && (
                <Offcanvas show={isProductsDisplayed} onHide={closeSupermarketProducts}>
                    <Offcanvas.Header closeButton>
                        <Offcanvas.Title>{parentCategorySelected}</Offcanvas.Title>
                    </Offcanvas.Header>
                    <Offcanvas.Body className='offcanvas-mercadona'>
                        Haz click en un producto para añadirlo a la lista
                        <Accordion defaultActiveKey='offcanvas-0'>
                            {filteredProducts.length > 0 && (
                                filteredProducts.map((subCategory, index) => (
                                    <React.Fragment key={`product-info-${subCategory.subcategoryName}-${index}`}>
                                        <Accordion.Item eventKey={`offcanvas-${index}`}>
                                            <Accordion.Header>{subCategory.subcategoryName}</Accordion.Header>
                                            <Accordion.Body>
                                                <ol id="product-info" className="list-group list-group-numbered">
                                                    {subCategory.products.map((product) => (
                                                        <Card.Link
                                                            key={`product-link-${product.id}`}
                                                            onClick={() => addShoppingListProduct(product.id, SUPERMARKET_NAME)}
                                                        >
                                                            <li
                                                                className='list-group-item d-flex justify-content-between align-items-start'
                                                                key={`product-${product.id}`}
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
                                    </React.Fragment>
                                ))
                            )}
                        </Accordion>
                    </Offcanvas.Body>
                </Offcanvas>
            )}
            <Accordion defaultActiveKey="shopping-list" >
                <Accordion.Item eventKey='shopping-list'>
                    <Accordion.Header>
                        Mi lista de la compra
                        {mercadonaShoppingList?.products?.length > 0 && (
                            <span> (Total: {mercadonaShoppingList.total} €)</span>
                        )}
                    </Accordion.Header>
                    <Accordion.Body>
                        {mercadonaShoppingList?.products?.length > 0 ? (
                            <>
                                <Button
                                    variant="success"
                                    onClick={() => findLowestShoppingList(SUPERMARKET_NAME)}
                                >
                                    Buscar precio más barato
                                </Button>

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
                                                onClick={() => removeShoppingListProduct(product.id, SUPERMARKET_NAME)}
                                            >
                                                Eliminar
                                            </button>
                                        </li>

                                    ))}
                                </ol>
                            </>
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
                                                onClick={() => addShoppingListProduct(product.id, SUPERMARKET_NAME)}
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
                rows.map((row, rowIndex) => (
                    <Row key={rowIndex}>
                        {row.map(([key, value], colIndex) => {
                            const subCategories = Object.keys(value);
                            return (
                                <Col xs={6} key={colIndex} className='equal-height-card'>
                                    <Card >
                                        <Card.Img variant="top" src="holder.js/100px180?text=Image cap" />
                                        <Card.Body>
                                            <Card.Title className='category-title category-name'>
                                                <Card.Link
                                                    onClick={() => displaySupermarketProducts(SUPERMARKET_NAME, key)}>
                                                    {key}
                                                </Card.Link>
                                            </Card.Title>
                                        </Card.Body>
                                        <ListGroup className="list-group-flush subcategory-list" style={{ fontSize: '0.8rem', textAlign: 'center' }}>
                                            {subCategories.map((categoryName, index) => (
                                                <ListGroup.Item key={`subcategories-${index}`}>
                                                    <Card.Link
                                                        onClick={() => displaySupermarketProducts(SUPERMARKET_NAME, key, categoryName)}>
                                                        {categoryName}
                                                    </Card.Link>
                                                </ListGroup.Item>
                                            ))}
                                        </ListGroup>
                                    </Card>
                                </Col>
                            );
                        })}
                    </Row>
                ))
            )}
        </Container>

    );
}

export default ShoppingListCategories;
