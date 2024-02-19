// Test suite using spies from sinon

const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payments');

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
  const spy = sinon.spy(Utils, 'calculateNumber');

  afterEach(() => {
    spy.restore();
  });

  it('calls Utils.calculateNumber with correct arguments', () => {

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;

    expect(spy.calledWithExactly('SUM', 100, 20)).to.be.true;
  });
});
