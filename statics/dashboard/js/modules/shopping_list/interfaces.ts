export type Product = {
    id: string;
    name: string;
    image: string;
    price: number;
};

export type Subcategory = Product[];

export type Category = {
    [subcategoryName: string]: Subcategory;
};

export type MercadonaCategoryProducts = {
    [categoryName: string]: Category;
};

export type IShoppingListState = {
    mercadonaProducts: MercadonaCategoryProducts,
    isProductsDisplayed: boolean,
    supermarketProductsSelected: string | null,
};
