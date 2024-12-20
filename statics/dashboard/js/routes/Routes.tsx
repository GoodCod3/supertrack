import React from 'react';
import { Router, Switch, Route } from 'react-router-dom';
import { History } from 'history';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import ShoppingListPage from '@src/modules/shopping_list/ui/shopping_list';

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
                <ToastContainer limit={3} autoClose={800}/>
            </>
        );
    }
}

export default AppRoutes;
