import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import App from './App';
import Anagram from './views/Anagrams'
import ColorTable from './components/ColorTable'
import renderer from 'react-test-renderer'

test('test renders title', () => {
  const { getByText } = render(<Anagram />);
  const linkElement = getByText("Anagram Checker");
  expect(linkElement).toBeInTheDocument();
});

test("renders the input box correctly", ()=>{
  const { getByText } = render(<Anagram />);
  const linkElement = getByText("Any phrase");
  expect(linkElement).toBeInTheDocument();
});

test("renders the checker button correctly", ()=>{
  const { getByText } = render(<Anagram />);
  const buttonElement = getByText("Check!");
  expect(buttonElement).toBeInTheDocument();
});

test("test snapshot of Aangram page", () => {
  const tree = renderer.create(<Anagram/>).toJSON();
  expect(tree).toMatchSnapshot();
})

test("test renders the table component correctly", ()=>{
  const headingDict = {
    word1: "Word 1",
    word2: "Word 2",
    count: "Requested Count"
  }
  const popularAnagramsList = [{word1: 'post', word2: 'stop', count:1}]
  const { getByText } = render(<ColorTable headingDict={headingDict} popularAnagramsList={popularAnagramsList} />);
  const tableElement = getByText("Word 1");
  expect(tableElement).toBeInTheDocument();
  expect(getByText("post")).toBeInTheDocument();
  expect(getByText("Requested Count")).toBeInTheDocument();
});


