import React, { Component } from 'react'

class ChooseDimensionsForm extends Component {
    constructor(props) {
        super(props);
        this.state = { isNew: props.isNew, width: undefined, height: undefined }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    };

    handleChange = (event) => {
        this.setState({[event.target.name]: event.target.value});
    };

    handleSubmit = (event) => {
        event.stopPropagation();
        this.setState({isNew: false});
        this.props.onUpdateState(this.state);
    };

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <h2>CDF: is new? {this.props.isNew ? 'Yes!' : 'No...'}</h2>
                <h2>Width: {this.state.width}</h2>
                <h2>Height: {this.state.height}</h2>
                <label>
                    Width:
                    <input type="number" name="width" min="2" max="20" value={this.state.width} onChange={this.handleChange} />
                </label>
                <label>
                    Height:
                    <input type="number" name="height" min="2" max="20" value={this.state.height} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Avanti" onClick={this.handleSubmit} />
            </form>
        );
    };
}

export default ChooseDimensionsForm;
