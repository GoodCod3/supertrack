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
    displaySupermarketProducts: (supermarketSelected: string) => void,
};

const ShoppingListCategories = ({
    mercadonaProducts,
    displaySupermarketProducts,
}: IShoppingListCategories) => {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const entries = Object.entries(mercadonaProducts);
    const rows = [];
    for (let i = 0; i < entries.length; i += 2) {
        rows.push(entries.slice(i, i + 2));
    }

    rows.map((row, rowIndex) => {
        row.map(([key, value], colIndex) => {
            const entries = Object.keys(value);
            console.log(entries);
        });
    });

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
                                            <Card.Link onClick={() => displaySupermarketProducts(key)}>{key}</Card.Link>
                                        </Card.Title>
                                    </Card.Body>
                                    <ListGroup className="list-group-flush subcategory-list" style={{ fontSize: '0.8rem', textAlign: 'center' }}>
                                        {subCategories.map((categoryName, index) => (
                                            <ListGroup.Item>
                                                <Card.Link href="#">{categoryName}</Card.Link>
                                            </ListGroup.Item>
                                        ))}
                                    </ListGroup>
                                </Card>
                            </Col>
                        );
                    })}
                </Row>
            ))}
            <Offcanvas show={show} onHide={handleClose} backdrop="static" responsive="lg">
                <Offcanvas.Header closeButton>
                    <Offcanvas.Title>Offcanvas</Offcanvas.Title>
                </Offcanvas.Header>
                <Offcanvas.Body>
                    I will not close if you click outside of me.
                </Offcanvas.Body>
            </Offcanvas>
        </Container>
    );
}

export default ShoppingListCategories;
