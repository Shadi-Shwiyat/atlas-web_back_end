// Instance of a simple express app for testing
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());

app.listen(7865, () => {
  console.log('API available on localhost port 7865')
});

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const cartID = req.params.id;

  if (isNaN(cartID)) {
    return res.status(404).send('Cart not found. Invalid cart ID.');
  }

  res.send(`Payment methods for cart ${cartID}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
});

app.post('/login', (req, res) => {
  const username = req.body.userName;

  res.send(`Welcome ${username}`);
});
