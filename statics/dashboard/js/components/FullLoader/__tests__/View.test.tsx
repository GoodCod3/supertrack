/* eslint-disable @typescript-eslint/await-thenable */
import React from 'react';
import { render } from '@testing-library/react';

import View from '../View';


describe('Components -> Fullloader', () => {
    test('Loader is rendered', () => {
        const { container } = render(<View />);

        expect(container.getElementsByClassName('blockUI').length).toBe(3);
        expect(container.getElementsByClassName('blockUI blockOverlay').length).toBe(1);
    });
});

