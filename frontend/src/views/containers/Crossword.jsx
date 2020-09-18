import React, { Component } from 'react'
import CrosswordCell from "./CrosswordCell";

class Crossword extends Component {
    constructor(props) {
        super(props);
        this.state = props;
    }

    createLabels = () => {
        let table = [];
        let x = 1;
        table.push(<span id={`"label-${x}"`} ><span className="crossword-board__item-label-text">{`${x}`}</span></span>);
        return table;
    }

    createTable = () => {
        let table = [];

        for (let x = 1; x <= this.state.width; x++) {
            for (let y = 1; y <= this.state.height; y++) {
                table.push(<CrosswordCell x={x} y={y} blank={false} />);
            }
        }
        return table;
    }

    handleSubmit(event) {
        event.stopPropagation();
    }

    render() {
        if (this.props.isNew) {
            return '';
        }
        const size = 50;
        const board_style = {
            width: size * this.state.height,
            height: size * this.state.width,
            'grid-template': "repeat("+this.state.width+", "+(100/this.state.width)+"%) / repeat("+this.state.height+", "+(100/this.state.height)+"%)",
        }
        return (<>
            <h3>Crossword</h3>
            <div className="crossword-board-container">
                <div className="crossword-board" style={board_style} >
                    {this.createTable()}
                    <div className="crossword-board crossword-board--labels">
                        {this.createLabels()}
                    </div>
                </div>
            </div>
            <input type="submit" value="Avanti" onClick={this.handleSubmit} />
        </>);
    }
}
export default Crossword;