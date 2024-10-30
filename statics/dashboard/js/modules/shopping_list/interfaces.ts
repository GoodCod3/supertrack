export type Product = {
    id: string;
    name: string;
    image: string;
    price: number;
};

export type Subcategory = Product[];

export type Category = {
    [subcategoryName: string]: Subcategory,
};

export type MercadonaCategoryProducts = {
    [categoryName: string]: Category,
};

export type MercadonaShoppingListProduct = {
    id: string,
    image: string,
    name: string,
    price: number,
    quantity: number,
    total_price: number,
};

export type MercadonaShoppingList = {
    total: number,
    products: MercadonaShoppingListProduct[]
};


export type IMercadonaCategory = {
    name: string,
};

export type FilteredProductsResult = {
    subcategoryName: string;
    products: Product[];
}[];

export type SearchFilteredResult = {
    categoryName: string;
    subcategoryName: string;
    products: Product[];
};
export type IShoppingListState = {
    isProductsDisplayed: boolean,
    mercadonaProducts: MercadonaCategoryProducts,
    mercadonaShoppingList: string | null,
    parentCategorySelected: string | null,
    productCategorySelected: string | null,
    supermarketProductsSelected: string | null,
};
