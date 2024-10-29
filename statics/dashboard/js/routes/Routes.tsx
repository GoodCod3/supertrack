import React from 'react';
import { Router, Switch, Route } from 'react-router-dom';
import { History } from 'history';

import FullLoader from '@components/FullLoader';
import ShoppingListPage from '@components/ShoppingListPage';

import {
    URL_SHOPPING_LIST_PAGE
} from '@src/constants/urls';

type IAppRoutesProps = {
    history: History,
};


class AppRoutes extends React.Component<IAppRoutesProps> {
    render() {
        return (
            <>
                <Router history={this.props.history}>
                    <Switch>
                        <Route exact path={URL_SHOPPING_LIST_PAGE}>
                            <ShoppingListPage />
                        </Route>
                    </Switch>
                </Router>

            </>
        );
    }
}

export default AppRoutes;
