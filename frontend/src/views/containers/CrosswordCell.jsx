import React, { Component } from 'react'

class CrosswordCell extends Component {
    constructor(props) {
        super(props);
        this.state = { x: props.x, y: props.y, blank: props.blank, val: props.val }
    }

    changeBlankState = (event) => {
        this.setState({'blank': !this.state.blank});
    }

    render() {
        const id = 'w'+this.state.x+'_y'+this.state.y;
        return (
            <input
                id = { id }
                className = { this.state.blank ? 'crossword-board__item--blank' : 'crossword-board__item' }
                type="text" minLength="0" maxLength="0" onClick= { this.changeBlankState }
                val = { this.state.val }
            />
        );
    }
}

export default CrosswordCell;