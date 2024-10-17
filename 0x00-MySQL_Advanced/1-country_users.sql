-- Create Table Users Add Country
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(email)
)