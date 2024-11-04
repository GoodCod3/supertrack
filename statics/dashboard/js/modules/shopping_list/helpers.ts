type CategoryProducts = Record<string, Record<string, { name: string }[]>>;

type FilteredResult<T> = {
    categoryName: string;
    subcategoryName: string;
    products: T[];
};

export const filterResults = <T extends { name: string }>(
    searchTerm: string,
    products: CategoryProducts
): FilteredResult<T>[] => {
    const lowerCasedTerm = searchTerm.toLowerCase();
    const results: FilteredResult<T>[] = [];

    Object.entries(products).forEach(([categoryName, subcategories]) => {
        const categoryMatch = categoryName.toLowerCase().includes(lowerCasedTerm);

        Object.entries(subcategories).forEach(([subcategoryName, productList]) => {
            const subcategoryMatch = subcategoryName.toLowerCase().includes(lowerCasedTerm);

            const matchingProducts = productList.filter((product) =>
                product.name.toLowerCase().includes(lowerCasedTerm)
            ) as T[];

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