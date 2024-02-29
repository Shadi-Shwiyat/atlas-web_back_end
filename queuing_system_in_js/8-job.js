// Script creates jobs from passed in list
// and queue object

function createPushNotificationsJobs(jobs, queue){
    if (!Array.isArray(jobs)) {
        return (new Error('Jobs is not an array'));
    }

    for (const jobData of jobs) {
        const job = queue.create('push_notification_code_3', jobData);

        job.save((err) => {
          if (err) {
            console.error(`Error creating job: ${err}`);
          } else {
            console.log(`Notification job created: ${job.id}`);
          }
        });

        job.on('complete', () => {
          console.log(`Notification job #${job.id} completed`);
        });
    
        job.on('failed', (err) => {
          console.log(`Notification job #${job.id} failed: ${err}`);
        });
    
        job.on('progress', (progress) => {
          console.log(`Notification job #${job.id} ${progress}% complete`);
        });
    }
}

module.exports = createPushNotificationsJobs;
