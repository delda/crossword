import React, { Component } from 'react'

class CrosswordCell extends Component {
    constructor(props) {
        super(props);
        this.state = { x: props.x, y: props.y, blank: false }
    }

    changeBlankState = (event) => {
        this.setState({'blank': !this.state.blank});
    }

    render() {
        return (
            <input
                className = { this.state.blank ? 'crossword-board__item--blank' : 'crossword-board__item' }
                type="text" minLength="0" maxLength="0" onClick={ this.changeBlankState } />
        );
    }
}

export default CrosswordCell;