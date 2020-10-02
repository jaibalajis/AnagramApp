import React from 'react';
import { render } from '@testing-library/react';
import App from './App';
import Anagram from './views/Anagrams'
import * as ReactDOM from "react-dom";

test('renders learn react link', () => {
  const { getByText } = render(<Anagram />);
  const linkElement = getByText("Anagram Check");
  expect(linkElement).toBeInTheDocument();
});

test("renders the input box correctly", ()=>{
  const { getByText } = render(<Anagram />);
  const linkElement = getByText("Any phrase");
  expect(linkElement).toBeInTheDocument();
});
