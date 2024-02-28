import { create } from 'json-server';
import redis from 'redis';

const redisClient = redis.createClient({
    host: '127.0.0.1',
    port: 6379
});

redisClient.on('ready', () => {
    console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Delete Hash
function deleteHash() {
    redisClient.del('HolbertonSchools', (err, reply) => {
        if (err) {
            console.error(`Error deleting hash: ${err}`);
        }
    });
}

// Create Hash
function createHash() {
    redisClient.hset('HolbertonSchools', 'Portland', 50, (err, reply1) => {
        if (err) {
            console.error(`Error setting value for Portland: ${err}`);
        } else {
            redis.print(`Reply: ${reply1}`);

            redisClient.hset('HolbertonSchools', 'Seattle', 80, (err, reply2) => {
                if (err) {
                    console.error(`Error setting value for Seattle: ${err}`);
                } else {
                    redis.print(`Reply: ${reply2}`);

                    redisClient.hset('HolbertonSchools', 'New York', 20, (err, reply3) => {
                        if (err) {
                            console.error(`Error setting value for New York: ${err}`);
                        } else {
                            redis.print(`Reply: ${reply3}`);

                            redisClient.hset('HolbertonSchools', 'Bogota', 20, (err, reply4) => {
                                if (err) {
                                    console.error(`Error setting value for Bogota: ${err}`);
                                } else {
                                    redis.print(`Reply: ${reply4}`);

                                    redisClient.hset('HolbertonSchools', 'Cali', 40, (err, reply5) => {
                                        if (err) {
                                            console.error(`Error setting value for Cali: ${err}`);
                                        } else {
                                            redis.print(`Reply: ${reply5}`);

                                            redisClient.hset('HolbertonSchools', 'Paris', 2, (err, reply6) => {
                                                if (err) {
                                                    console.error(`Error setting value for Paris: ${err}`);
                                                } else {
                                                    redis.print(`Reply: ${reply6}`);
                                                }
                                            });
                                        }
                                    });
                                }
                            });
                        }
                    });
                }
            });
        }
    });
}

// Display Hash
function displayHash() {
    redisClient.hgetall('HolbertonSchools', (err, reply) => {
        if (err) {
            console.error(`Error getting hash values: ${err}`);
        } else {
            console.log(reply);
        }
    });
}

// Delete hash to have clean slate and be able to see reply 1 everytime program is run
deleteHash();
createHash();

setTimeout(displayHash, 300);