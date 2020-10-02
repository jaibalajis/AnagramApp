import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Anagrams from './views/Anagrams'


function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/anagrams">
          <Anagrams/>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
