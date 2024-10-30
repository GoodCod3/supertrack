import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ListGroup from 'react-bootstrap/ListGroup';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

import type { MercadonaCategoryProducts } from '@src/modules/shopping_list/interfaces';


type IShoppingListCategories = {
    mercadonaProducts: MercadonaCategoryProducts,
};

const ShoppingListCategories = ({ mercadonaProducts }: IShoppingListCategories) => {
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
                                            <Card.Link href="#">{key}</Card.Link>
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
        </Container>
    );
}

export default ShoppingListCategories;
