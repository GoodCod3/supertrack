import React from 'react';

type IFullLoaderProps = {
    type?: string,
    id?:string,
};

const FullLoader = ({ type = 'full', id }: IFullLoaderProps) => (
    <div data-testid={`Fullloader__container_${type}`} id={`${id ? id : ''}`}>
        <div className="blockUI" style={{ 'display': 'none' }}></div>
        {type === 'full' ? (
            <>
                <div className="blockUI blockOverlay" style={{ 'zIndex': 1000, 'border': 'none', 'margin': '0px', 'padding': '0px', 'width': '100%', 'height': '100%', 'top': '0px', 'left': '0px', 'backgroundColor': 'rgb(255, 255, 255)', 'opacity': '0.666873', 'cursor': 'default', 'position': `${type === 'full' ? 'fixed' : 'absolute'}` }}></div>
                <div className="blockUI blockMsg blockPage" style={{ 'zIndex': 1011, 'position': 'fixed', 'padding': '0px', 'margin': '0px', 'width': '30%', 'top': '40%', 'left': '35%', 'textAlign': 'center', 'color': 'rgb(0, 0, 0)', 'border': '0px', 'backgroundColor': 'transparent', 'cursor': 'default', 'opacity': '0.593691' }}>
                    <div className="spinner-border text-primary" role="status"></div>
                </div>
            </>
        ) : (
            <>
                <div className="blockUI blockOverlay" style={{zIndex: 1000,border: 'none',margin: '0px',padding: '0px',width: '100%',height: '100%',top: '0px',left: '0px',backgroundColor: 'rgb(0, 0, 0)',opacity: 0.6,cursor: 'wait',position: 'absolute'}}></div>
                <div className="blockUI blockMsg blockElement" style={{'zIndex': '1011', 'display': 'none', 'position': 'absolute', 'left': '885px', 'top': '99.5px'}}></div>
            </>
        )}
    </div>

);

export default FullLoader;
