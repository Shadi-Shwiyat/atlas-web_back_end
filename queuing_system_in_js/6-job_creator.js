// Creating a job creator and a queue using kue
const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '9182104148',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Error creating job:', err);
    process.exit(1);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
  process.exit(0);
});

job.on('failed', () => {
  console.log('Notification job failed');
  process.exit(1);
});
