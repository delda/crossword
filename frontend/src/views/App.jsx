import React from 'react';
import TitleBar from './containers/TitleBar'
import ChooseDimensionsForm from "./containers/ChooseDimensionsForm";
import Crossword from "./containers/Crossword";
import './containers/style.scss';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isNew: true};
        this.setInput = this.setInput.bind(this);
        this.updateState = this.updateState.bind(this);
    }

    updateState(state) {
        this.setState(state);
    }

    setInput(key, value) {
        this.setState({key, value})
    }

    render() {
        const isNew = this.state.isNew;
        return (
            <div>
                <header>
                    <h1>isNew: {this.state.isNew ? 'Yes!' : 'No...'}</h1>
                    <h1>W: {this.state.width}, H: {this.state.height}</h1>
                    <TitleBar/>
                </header>
                <div id="body">
                    { isNew
                        ? <ChooseDimensionsForm isNew={this.state.isNew} onUpdateState={this.updateState} />
                        : <Crossword width={this.state.width} height={this.state.height} />
                    }
                </div>
            </div>
        );
    };
};

export default App;
