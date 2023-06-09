DROP TABLE IF EXISTS guitars;
DROP TABLE IF EXISTS makers;

CREATE TABLE makers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    contact VARCHAR (255),
    tel VARCHAR (255),
    email VARCHAR (255),
    active BOOLEAN
);

CREATE TABLE guitars (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description VARCHAR (255),
    stock INT,
    min_stock INT,
    buy_price FLOAT,
    sell_price FLOAT,
    maker_id INT NOT NULL REFERENCES makers(id)
);
