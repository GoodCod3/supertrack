/* eslint-disable @typescript-eslint/no-explicit-any */
import axios, { AxiosError } from 'axios';

import type { IApiError } from '../interfaces/global';


const ENDPOINT_BASE_URL = process.env.API_ENDPOINT_URL || 'https://api.supertrack.es';
const API_VERSION = process.env.REACT_APP_BUDAPP_API_VERSION || 'api/v1';
const RESPONSE_FAIL = { success: false, errorStatus: 403 };

type IAxiosError = {
    data: IApiError,
    status: number,
};

const getCsrfToken = (): string | null => {
    const name = 'csrftoken';
    const cookieValue = document.cookie
        .split('; ')
        .find((row) => row.startsWith(name))
        ?.split('=')[1];

    return cookieValue || null;
};

const buildHeaders = (hasBodyImage?: boolean) => {
    const AXIOS_CONFIG = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRFToken': getCsrfToken() || ''
        } as Record<string, string>,
        withCredentials: true,
    };

    if (hasBodyImage) {
        AXIOS_CONFIG.headers['Content-Type'] = 'multipart/form-data';
    }

    return AXIOS_CONFIG;
};

const buildErrorResponse = (errorResponse?: IAxiosError): IApiError => {
    const errorStatus = errorResponse?.status;

    return {
        ...errorResponse?.data,
        success: errorResponse?.data?.success || false,
        message: errorResponse?.data?.message,
        errorStatus: errorStatus || errorResponse?.data?.errorStatus || 403,
    };
};


const get = async (url: string): Promise<any> => {
    try {
        const response = await axios.get(`${ENDPOINT_BASE_URL}/${url}`, buildHeaders());

        return response.data;
    } catch (error) {
        if (error instanceof AxiosError && error.response) {
            throw buildErrorResponse(error.response as IAxiosError);
        }

        return RESPONSE_FAIL;
    }
};

const post = async (url: string, body: Record<never, never>, hasBodyImage = false): Promise<any> => {
    // const axiosConfig = ignoreHeaders ? {} : buildHeaders();
    const axiosConfig = buildHeaders(hasBodyImage);
    try {
        const response = await axios.post(
            `${ENDPOINT_BASE_URL}/${url}`,
            body,
            axiosConfig);

        return response.data;
    } catch (error) {
        if (error instanceof AxiosError && error.response) {
            throw buildErrorResponse(error.response as IAxiosError);
        }

        return RESPONSE_FAIL;
    }
};

export default {
    get,
    post,
};
