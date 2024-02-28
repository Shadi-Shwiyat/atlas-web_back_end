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
