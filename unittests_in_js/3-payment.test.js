// Test suite using spies from sinon

const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payments');

const { expect } = chai;
const sandbox = sinon.createSandbox();

describe('sendPaymentRequestToApi', () => {
  afterEach(() => {
    sandbox.restore();
  });

  it('calls Utils.calculateNumber with correct arguments', () => {

    const calculateNumberSpy = sandbox.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(calculateNumberSpy.calledOnce).to.be.true;

    expect(calculateNumberSpy.calledWithExactly('SUM', 100, 20)).to.be.true;
  });
});
