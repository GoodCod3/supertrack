export type IAnyRecord = Record<string, any>; // eslint-disable-line @typescript-eslint/no-explicit-any

export type IApiError = {
    errorStatus: number,
    success: boolean,
    message?: string,
    error?: IAnyRecord
};