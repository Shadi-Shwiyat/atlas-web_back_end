// Test suite to test an api running on express.js
const request = require('request');
const { expect } = require('chai');

describe('Express API', function () {
  it('request returns correct status codes and results', (done) => {
    request('http://localhost:7865', (err, res, body) => {
    if (err) {
      return done(err)
    };

      expect(res.statusCode).to.equal(200);

      expect(body).to.equal('Welcome to the payment system');

      done();
    });
  });
});