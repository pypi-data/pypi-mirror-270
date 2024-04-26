bootstrap1 = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {
    box-sizing: border-box;
}
.row::after {
content: "";
clear: both;
display: block;
}
[class*="col-"] {
float: left;
padding: 15px;
}
html {
font-family: "Lucida Sans", sans-serif;
}
.header {
background-color: #9933cc;
color: #ffffff;
padding: 15px;
}
.menu ul {
list-style-type: none;
margin: 0;
padding: 0;
}
.menu li {
padding: 8px;
margin-bottom: 7px;
background-color: #33b5e5;
color: #ffffff;
box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
.menu li:hover {
background-color: #0099cc;
}
.aside {
background-color: #33b5e5;
padding: 15px;
color: #ffffff;
text-align: center;
font-size: 14px;
box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
.footer {
background-color: #0099cc;
color: #ffffff;
text-align: center;
font-size: 12px;
padding: 15px;
}
/* For desktop: */
.col-1 {width: 8.33%;}
.col-2 {width: 16.66%;}
.col-3 {width: 25%;}
.col-4 {width: 33.33%;}
.col-5 {width: 41.66%;}
.col-6 {width: 50%;}
.col-7 {width: 58.33%;}
.col-8 {width: 66.66%;}
.col-9 {width: 75%;}
.col-10 {width: 83.33%;}
.col-11 {width: 91.66%;}
.col-12 {width: 100%;}
@media only screen and (max-width: 768px) {
/* For mobile phones: */
[class*="col-"] {
width: 100%;
}
}
</style>
</head>
<body>
<div class="header">
<h1>Chania</h1>
</div>
<div class="row">
<div class="col-3 menu">
<ul>
<li>The Flight</li>
<li>The City</li>
<li>The Island</li>
<li>The Food</li>
</ul>
</div>
<div class="col-6">
<h1>The City</h1>
<p>Chania is the capital of the Chania region on the island of Crete. The city can be divided in two parts, the old town and the modern city.</p>
</div>
</body>
</html>
'''

bootstrap2 = '''
<html>
<head>
<title> Bootstrap Example </title>
<meta charset = "utf-8">
<meta name = "viewport" content = "width = device-width, initial-scale = 1">
<link rel = "stylesheet" href="https://maxdcn.bootstrapdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
<div class = "container-fluid">
<h1> Hello World !!! </h1>
<p> Resize browser window to see the effect </p>
<p> The columns will automatically stack on top of each other when the screen is less than 768 px wide </p>
<div class = "row">
<div class = "col-sm-4" style = "background-color: red">
(col-sm-4-1) </div>
<div class = "col-sm-4" style = "background-color: blue">
(col-sm-4-2) </div>
<div class = "col-sm-4" style = "background-color: green">
(col-sm-4-3) </div>
</div></div>
</body>
</html>

'''

bootstrap3 = '''
<html lang="en">
<head>
<title>Bootstrap Example</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
<div class="container mt-3">
<h2>Horizontal Direction</h2>
<p>Use .flex-row to make the flex items appear side by side (default):</p>
<div class="d-flex flex-row bg-secondary mb-3">
<div class="p-2 bg-info">Flex item 1</div>
<div class="p-2 bg-warning">Flex item 2</div>
<div class="p-2 bg-primary">Flex item 3</div>
</div>
<p>Use .flex-row-reverse to right-align the direction:</p>
<div class="d-flex flex-row-reverse bg-secondary">
<div class="p-2 bg-info">Flex item 1</div>
<div class="p-2 bg-warning">Flex item 2</div>
<div class="p-2 bg-primary">Flex item 3</div>
</div>
</div>
</body>
</html>
'''

node1 = '''
// Code Snippet 1
var http = require('http');

http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Hello World');
}).listen(8080);

// Code Snippet 2
var http = require('http');

http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  console.log("This example is different");
  console.log("The result is displayed on command line");
  res.end('Response sent successfully');
}).listen(8080);

'''

react1 = '''
import styled from 'styled-components';

const StyledButton = styled.button`
  border: 2px solid #4caf50;
  background-color: #4caf50;
  color: white;
  padding: 15px 32px;
  text-align: center;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  transition: 0.55s all ease-out;
`;

export default StyledButton;


import './App.css';
import StyledButton from './components/Button';

function App() {
  return (
    <div className="App">
      <StyledButton>Styled Button</StyledButton>
    </div>
  );
}

export default App;
'''


react2 = '''
import {useState, useEffect, useRef} from "react";

function App() {
    const [inputValue, setInputValue] = useState("");
    const count = useRef(0);

    useEffect(() => {
        count.current = count.current + 1;
    });

    return (
        <>
            <br />
            <input type="text" value={inputValue} onChange={(e) => {setInputValue(e.target.value)}} />
            <h1>Render Count: {count.current}</h1>
        </>
    );
}

export default App;

import {useState} from "react";

function FavCity() {
    const [city, setCity] = useState({
        continent: "Europe",
        countries: "France",
        city: "Paris"
    });

    const updateCity = () => {
        setCity(previousState => {
            return {...previousState, city: "Cannes"}
        });
    }

    return (
        <>
            <h1>{city.continent}</h1>
            <p>Favorite City {city.city} in Favorite Country {city.countries}</p>
            <button type="button" onClick={updateCity}>Cannes</button>
        </>
    );
}

export default FavCity;

import './App.css';
import State from './components/State';
import Ref from './components/Ref';

function App() {
  return (
    <div className="App">
      <State></State>
      <Ref></Ref>
    </div>
  );
}

export default App;
'''

todo = '''
import React, { useState } from 'react';
import './App.css';
import Header from './Header';
import TodoList from './TodoList';
import AddTodo from './AddTodo';

function App() {
  const [todoList, setTodoList] = useState([]);

  const addTodo = (task) => {
    const newTodoList = [...todoList, { id: Date.now(), task: task, complete: false }];
    setTodoList(newTodoList);
  };

  const handleToggle = (id) => {
    const mapped = todoList.map(task => {
      return task.id === id ? { ...task, complete: !task.complete } : { ...task };
    });
    setTodoList(mapped);
  };

  return (
    <div className="App">
      <Header />
      <TodoList todoList={todoList} handleToggle={handleToggle} />
      <div className="add-todo">
        <AddTodo addTodo={addTodo} />
      </div>
    </div>
  );
}

export default App;

import React, { useState } from 'react';

const AddTodo = ({ addTodo }) => {
  const [task, setTask] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!task) return;
    addTodo(task);
    setTask('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={task} onChange={e => setTask(e.target.value)} />
      <button>Add</button>
    </form>
  );
}

export default AddTodo;

import React from 'react';

const Header = () => {
  return (
    <header>
      <h1>To-Do List</h1>
    </header>
  );
}

export default Header;


import React from 'react';

const Todo = ({ todo, handleToggle }) => {
  const handleClick = (e) => {
    e.preventDefault();
    handleToggle(todo.id);
  };

  return (
    <div className={todo.complete ? "strike" : ""} onClick={handleClick}>
      {todo.task}
    </div>
  );
}

export default Todo;


import React from 'react';
import Todo from './Todo';

const TodoList = ({ todoList, handleToggle }) => {
  return (
    <div className="todo-list">
      {todoList.map(todo => (
        <Todo key={todo.id} todo={todo} handleToggle={handleToggle} />
      ))}
    </div>
  );
}

export default TodoList;
 

'''

eit_codes = {
    "bootstrap1.html": bootstrap1,
    "bootstrap2.html": bootstrap2,
    "bootstrap3.html": bootstrap3,
    "node1.js": node1,
    "react1.js": react1,
    "react2.js": react2,
    "todo.js": todo
}

def eitt_():
    for key, value in eit_codes.items():
        with open(key, "w") as f:
            f.write(value)