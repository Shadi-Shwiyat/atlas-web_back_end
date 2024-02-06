-- Script creates users table if it
-- does not exist, sets columns to
-- id, email (unique), and name
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)