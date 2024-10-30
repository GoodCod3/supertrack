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
    Product,
} from '@src/modules/shopping_list/interfaces';


type IShoppingListCategories = {
    addShoppingListProduct: (productId: string) => void,
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
};

type FilteredProductsResult = {
    subcategoryName: string;
    products: Product[];
}[];

const SUPERMARKET_NAME = 'mercadona';
const getProductsBySelection = (
    products: MercadonaCategoryProducts,
    categoryName: string,
    subcategoryName?: string | null
): FilteredProductsResult => {
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
}: IShoppingListCategories) => {
    let filteredProducts: FilteredProductsResult = [];
    if (isProductsDisplayed && parentCategorySelected) {
        filteredProducts = getProductsBySelection(mercadonaProducts, parentCategorySelected, productCategorySelected);
        console.log(filteredProducts);
    }

    const entries = Object.entries(mercadonaProducts);
    const rows = [];
    for (let i = 0; i < entries.length; i += 2) {
        rows.push(entries.slice(i, i + 2));
    }

    return (
        <Container>
            {rows.map((row, rowIndex) => (
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
            ))}
            <Offcanvas show={isProductsDisplayed} onHide={closeSupermarketProducts} backdrop="static" responsive="lg">
                <Offcanvas.Header closeButton>
                    <Offcanvas.Title>{parentCategorySelected}</Offcanvas.Title>
                </Offcanvas.Header>
                {productCategorySelected && (
                    <Offcanvas.Header >
                        <Offcanvas.Title>{productCategorySelected}</Offcanvas.Title>
                    </Offcanvas.Header>

                )}
                <Offcanvas.Body>
                    Haz click en un producto para añadirlo a la lista
                    <Accordion defaultActiveKey="0">
                        {filteredProducts.length > 0 && (
                            filteredProducts.map((subCategory, index) => (
                                <Accordion.Item eventKey={`${index}`}>
                                    <Accordion.Header>{subCategory.subcategoryName}</Accordion.Header>
                                    <Accordion.Body>
                                        <ol id="product-info" className="list-group list-group-numbered">
                                            {subCategory.products.map((product, productIndex) => (
                                                <Card.Link onClick={() => addShoppingListProduct(product.id)}>
                                                    <li
                                                        className='list-group-item d-flex justify-content-between align-items-start'
                                                        key={`product-${productIndex}`}
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
                            ))
                        )}
                    </Accordion>
                </Offcanvas.Body>
            </Offcanvas>
        </Container>
    );
}

export default ShoppingListCategories;
