// Test suite using spies from sinon

const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
  it('calls Utils.calculateNumber with correct arguments', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;

    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    spy.restore();
  });

  it('Utils.calculateNumber is stubbed correctly', () => {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.returns(10);

    const consoleSpy = sinon.spy(console, 'log');
    
    sendPaymentRequestToApi(100, 20);

    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    consoleSpy.restore();
  });

  it('Logs correct message to console only once', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnce).to.be.true;

    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    spy.restore();
    consoleSpy.restore();
  });

  it('Logs correct message to console only once', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnce).to.be.true;

    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;

    spy.restore();
    consoleSpy.restore();
  });
});
