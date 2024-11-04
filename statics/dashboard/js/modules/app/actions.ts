import {
    REDIRECT_TO,
} from './action-types';


interface IAction<P = unknown> {
    type:
    | typeof REDIRECT_TO
    payload?: Record<string, P>;
}

export const redirectTo = (url: string): IAction<string> => ({
    type: REDIRECT_TO,
    payload: { url },
});
