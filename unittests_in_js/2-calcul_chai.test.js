// Script test functionality of
//  0-calcul function

const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

const { expect } = chai;

describe('calculateNumber', () => {
  it('returns a sum', () => {
    const result = calculateNumber('SUM', 1, 3);
    expect(result).to.equal(4);
  });

  it('rounds first number', () => {
    const result = calculateNumber('SUM', 1.2, 3);
    expect(result).to.equal(4);
  });

  it('rounds second number', () => {
    const result = calculateNumber('SUM', 1, 3.3);
    expect(result).to.equal(4);
  });

  it('rounds both numbers', () => {
    const result = calculateNumber('SUM', 1.2, 3.7);
    expect(result).to.equal(5);
  });

  it('rounds a number up when .5', () => {
    const result = calculateNumber('SUM', 1.5, 3.7);
    expect(result).to.equal(6);
  });

  it('returns a difference', () => {
    const result = calculateNumber('SUBTRACT', 1.4, 4.5);
    expect(result).to.equal(-4);
  });

  it('returns a quotient', () => {
    const result = calculateNumber('DIVIDE', 1.4, 4.5);
    expect(result).to.equal(0.2);
  });

  it('returns an error when dividing by 0', () => {
    const result = calculateNumber('DIVIDE', 1.4, 0);
    expect(result).to.equal('Error');
  });
});
