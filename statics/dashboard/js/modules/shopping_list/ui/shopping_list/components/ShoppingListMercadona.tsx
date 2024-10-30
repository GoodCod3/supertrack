import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ListGroup from 'react-bootstrap/ListGroup';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Offcanvas from 'react-bootstrap/Offcanvas';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';


type IShoppingListCategories = {
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

const SUPERMARKET_NAME = 'mercadona';

const ShoppingListCategories = ({
    closeSupermarketProducts,
    displaySupermarketProducts,
    isProductsDisplayed,
    mercadonaProducts,
    parentCategorySelected,
    productCategorySelected,
    supermarketProductsSelected,
}: IShoppingListCategories) => {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);

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
                                <Card style={{ width: '8rem' }}>
                                    <Card.Img variant="top" src="holder.js/100px180?text=Image cap" />
                                    <Card.Body>
                                        <Card.Title className='category-title'>
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
                    I will not close if you click outside of me.
                </Offcanvas.Body>
            </Offcanvas>
        </Container>
    );
}

export default ShoppingListCategories;
