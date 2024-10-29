/* eslint-disable @typescript-eslint/no-unsafe-call */
import React from 'react';

type IProviderAppProps = Record<never, never>;

class ProviderApp extends React.Component {

    // constructor(props: IProviderAppProps) {
    //     super(props);

    //     this.store = configureStore();
    //     this.store.runSaga(rootSagas);

    //     this.history = generateHistory();
    // }

    render(): React.ReactElement {
        return <h1>Hi</h1>;
    }
}


export default ProviderApp;
