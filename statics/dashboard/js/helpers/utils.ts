export const mergeObject = (
    object1: Record<string, unknown>,
    object2?: Record<string, unknown>,
): Record<string, unknown> => ({ ...object1, ...object2 });

export const isEmpty = (value: unknown | null): boolean => (
    value == null
    || (typeof value === 'object' && Object.keys(value).length === 0)
    || (typeof value === 'string' && value.trim().length === 0)
);

export const hasObjectProperty = (object: Record<string, unknown>, propertyName: string): boolean => (
    object && Object.prototype.hasOwnProperty.call(object, propertyName)
);

export const arePropsValidWithoutError = (
    props: {
        data: Record<string, unknown> | null,
        error: Record<string, unknown> | null
    }
): boolean => {
    const hasPropsDataProperty = hasObjectProperty(props, 'data');

    return !(isEmpty(props)) && ((hasPropsDataProperty && props.data && !(props.error)) || !hasPropsDataProperty);
};

export const defaultEmptyfunction = (): void => { /* Comment to avoid SonarQube */ };
