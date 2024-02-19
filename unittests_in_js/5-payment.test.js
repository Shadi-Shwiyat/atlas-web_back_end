// Test suite using spies from sinon

const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    consoleSpy.restore();
  });

  it('Logs correct message to console only once', () => {
    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnce).to.be.true;

    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('Logs correct message to console only once', () => {
    sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnce).to.be.true;

    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  });
});
