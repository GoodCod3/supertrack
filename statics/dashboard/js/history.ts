import { History, LocationState, createBrowserHistory, Location } from 'history';

let history: History;

export const getHistory = (): History => history;

export const historyListener = (_: Location | string, action: string): void => {
    // Use setTimeout to make sure this runs after React Router's own listener
    setTimeout(() => {
        // Keep default behavior of restoring scroll position when user:
        // - clicked back button
        // - clicked on a link that programmatically calls `history.goBack()`
        // - manually changed the URL in the address bar (here we might want
        //   to scroll to top, but we can't differentiate it from the others)
        if (action !== 'POP') {
            // In all other cases, scroll to top
            window.scrollTo(0, 0);
        }
    });
};

export const generateHistory = (): History<LocationState> => {
    history = createBrowserHistory();

    history.listen(historyListener);

    return history;
};

export const pushToHistory = (url: string): void => {
    const historyObj = getHistory();

    historyObj.push(url);
};
