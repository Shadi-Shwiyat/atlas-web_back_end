// Connects to the redis server running locally
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

function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting value for ${schoolName}: ${err}`);
        } else {
            // console.log(`${schoolName}`);
            redis.print(`Reply: ${reply}`);
        }
    });
}

function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error getting value for ${schoolName}: ${err}`);
        } else {
            console.log(`${reply}`);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
