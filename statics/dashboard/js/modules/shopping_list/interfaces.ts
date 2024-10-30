export type MercadonaProduct = {
    id: string;
    name: string;
    image: string;
    price: number;
};

export type Subcategory = MercadonaProduct[];

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

export type MercadonaFilteredProductsResult = {
    subcategoryName: string;
    products: MercadonaProduct[];
}[];

export type MercadonaSearchFilteredResult = {
    categoryName: string;
    subcategoryName: string;
    products: MercadonaProduct[];
};

// Consum
export type ConsumProduct = {
    id: string;
    name: string;
    image: string;
    price: number;
};

export type ConsumSubcategory = MercadonaProduct[];

export type ConsumCategory = {
    [subcategoryName: string]: ConsumSubcategory,
};

export type IConsumCategoryProducts = {
    [categoryName: string]: ConsumCategory,
};

export type IConsumSearchFilteredResult = {
    categoryName: string;
    subcategoryName: string;
    products: ConsumProduct[];
};

export type ConsumShoppingListProduct = {
    id: string,
    image: string,
    name: string,
    price: number,
    quantity: number,
    total_price: number,
};

export type ConsumShoppingList = {
    total: number,
    products: ConsumShoppingListProduct[]
};


export type IShoppingListState = {
    isProductsDisplayed: boolean,
    mercadonaProducts: MercadonaCategoryProducts,
    consumProducts: IConsumCategoryProducts,
    mercadonaShoppingList: MercadonaShoppingList | null,
    consumShoppingList: ConsumShoppingList | null,
    parentCategorySelected: string | null,
    productCategorySelected: string | null,
    supermarketProductsSelected: string | null,
};
