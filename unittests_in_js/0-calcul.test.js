// Script test functionality of
//  0-calcul function

const assert = require('assert')
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Returns a sum', function() {
    const result = calculateNumber(1, 3);
    assert.equal(result, 4);
  });

  it('Rounds second number', function() {
    const result = calculateNumber(1, 3.7);
    assert.equal(result, 5);
  });

  it('Rounds both numbers', function() {
    const result = calculateNumber(1.2, 3.7);
    assert.equal(result, 5);
  });

  it('Rounds a number up when .5', function() {
    const result = calculateNumber(1.5, 3.7);
    assert.equal(result, 6);
  });
});