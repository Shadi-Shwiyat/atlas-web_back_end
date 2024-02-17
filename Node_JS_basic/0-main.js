import { expect } from 'chai';
import sinon from 'sinon'; 

import displayMessage from './0-console.js';

describe('displayMessage', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('logs to the console the right messages', () => {
    displayMessage('Hello Holberton School!');
    displayMessage('We are going to learn Node JS today');

    expect(consoleSpy.calledWith('Hello Holberton School!')).to.be.true;
    expect(consoleSpy.calledWith('We are going to learn Node JS today')).to.be.true;
  });
});