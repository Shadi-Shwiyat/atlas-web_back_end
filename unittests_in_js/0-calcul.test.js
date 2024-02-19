// Script test functionality of
//  0-calcul function

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('returns a sum', () => {
    const result = calculateNumber(1, 3);
    assert.equal(result, 4);
  });

  it('rounds first number', () => {
    const result = calculateNumber(1.2, 3);
    assert.equal(result, 4);
  });

  it('rounds second number', () => {
    const result = calculateNumber(1, 3.7);
    assert.equal(result, 5);
  });

  it('rounds both numbers', () => {
    const result = calculateNumber(1.2, 3.7);
    assert.equal(result, 5);
  });

  it('rounds a number up when .5', () => {
    const result = calculateNumber(1.5, 3.7);
    assert.equal(result, 6);
  });
});
