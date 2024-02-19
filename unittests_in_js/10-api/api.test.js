// Test suite to test an api running on express.js
const request = require('request');
const { expect } = require('chai');

describe('Route (/)', function () {
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

describe('Route (/cart/:id)', function () {
  it('returns correct status code/result when id is a #', function (done) {
    request('http://localhost:7865/cart/333', function (err, res, body) {
      if (err) {
        return done(err)
      };

      expect(res.statusCode).to.equal(200);

      expect(body).to.equal(`Payment methods for cart 333`);

      done();
    });
  });

  it('returns correct status code/result when id is NOT a # (404)', function (done) {
    request('http://localhost:7865/cart/test', function (err, res, body) {
      if (err) {
        return done(err)
      };

      expect(res.statusCode).to.equal(404);

      done();
    });
  });
});

describe('Route (/login)', function () {
  it('request correctly logs in user', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: true,
      body: {
        "userName": "Betty"
      }
    }

    request(options, (err, res, body) => {
      if (err) {
        return done(err)
      };

      expect(res.statusCode).to.equal(200);

      expect(body).to.equal('Welcome Betty');

      done();
    });
  });
});

describe('Route (/available_payments)', function () {
  it('request correctly displays available payments', (done) => {
    request('http://localhost:7865/available_payments', (err, res, body) => {
      if (err) {
        return done(err)
      };

      expect(res.statusCode).to.equal(200);

      expect(JSON.parse(body)).to.deep.equal({
        payment_methods:{
          credit_cards:true,
          paypal:false
        }
      });

      done();
    });
  });
});
