// Testing suite to test for promises
const getPaymentTokenFromAPI = require('./6-payment_token');
const chai = require('chai');

const { expect } = chai;

describe('getPaymentTokenFromAPI', () => {
  it('resolve with the correct object when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
