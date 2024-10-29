/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
import { connect } from 'react-redux';
import { History } from 'history';

import type ICommonRecord from '@src/interfaces/commonRecord';
import RouteComponent from './Routes';

type ActionProps = {
    redirectTo: (url: string) => void
    checkAuthtoken: () => void,
    cleanGlobalErrorMessage: () => void,
};

type OwnProps = {
    history: History,
};

export const mapStateToProps = (state: any): ICommonRecord => ({ // eslint-disable-line @typescript-eslint/no-explicit-any
});

export const mapActionsToProps = {
};

export default connect<ICommonRecord, ActionProps, OwnProps>(
    mapStateToProps,
    mapActionsToProps,
)(RouteComponent);
