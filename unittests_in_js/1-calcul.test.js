// Script test functionality of
//  0-calcul function

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('returns a sum', () => {
    const result = calculateNumber('SUM', 1, 3);
    assert.equal(result, 4);
  });

  it('rounds first number', () => {
    const result = calculateNumber('SUM', 1.2, 3);
    assert.equal(result, 4);
  });

  it('rounds second number', () => {
    const result = calculateNumber('SUM', 1, 3.3);
    assert.equal(result, 4);
  });

  it('rounds both numbers', () => {
    const result = calculateNumber('SUM', 1.2, 3.7);
    assert.equal(result, 5);
  });

  it('rounds a number up when .5', () => {
    const result = calculateNumber('SUM', 1.5, 3.7);
    assert.equal(result, 6);
  });

  it('returns a difference', () => {
    const result = calculateNumber('SUBTRACT', 1.4, 4.5);
    assert.equal(result, -4);
  });

  it('returns a quotient', () => {
    const result = calculateNumber('DIVIDE', 1.4, 4.5);
    assert.equal(result, 0.2);
  });

  it('returns a error when dividing by 0', () => {
    const result = calculateNumber('DIVIDE', 1.4, 0);
    assert.equal(result, 'Error');
  });
});
