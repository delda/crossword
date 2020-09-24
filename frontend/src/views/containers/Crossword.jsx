import React, { Component } from 'react';
import ReactDom from 'react-dom';
import CrosswordCell from "./CrosswordCell";
import axios from 'axios';
import request from 'request';

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
                table.push(<CrosswordCell x={x} y={y} blank={false} val={x} />);
            }
        }
        return table;
    }

    updateTable = (data) => {
        let element;
        console.log(data.response);
        for (let x = 1; x <= this.state.width; x++) {
            for (let y = 1; y <= this.state.height; y++) {
                console.log('w'+x+'_y'+y);
                console.log(data.response[x-1][y-1]);
                document.getElementById('w'+x+'_y'+y).value = data.response[x-1][y-1];
            }
        }
    }

    fetchAPI = (params) => {
        const apiUrl = 'http://127.0.0.1/generate_crossword?data=' + params.data;
        fetch(apiUrl)
            .then(response => response.json())
            .then((data) => this.updateTable(data));
    };

    handleSubmit = (event) => {
        event.stopPropagation();
        var crossword = Array.from(Array(parseInt(this.state.width)), () => new Array(parseInt(this.state.height)));

        let element;
        for (let x = 1; x <= this.state.width; x++) {
            for (let y = 1; y <= this.state.height; y++) {
                element = document.getElementById('w'+x+'_y'+y);
                crossword[x-1][y-1] = element.classList.contains('crossword-board__item--blank')
                    ? 1
                    : 0;
            }
        }
        let result = this.fetchAPI({'data': JSON.stringify(crossword)});
    }

    render = () => {
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
            <input type="submit" value="Avanti" onClick={this.handleSubmit.bind(this)} />
        </>);
    }
}


export default Crossword;