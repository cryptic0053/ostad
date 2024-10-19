-- Active: 1728314377960@@127.0.0.1@3306@apple_shop

CREATE TABLE users(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR (50) NOT NULL,
    mobile VARCHAR(50) NOT NULL,
    password VARCHAR(500) NOT NULL,
    otp VARCHAR(10) NOT NULL DEFAULT '0',
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)



--- পাত্রী(FOREIGN KEY) সুমাইয়ার(user_id) বিয়ে হবে(REFERENCES) গাইবান্ধার(users) রাব্বিলের(id) সাথে    
--- মরলে ২জন একসাথে (ON DELETE RESTRICT) , বাঁচলে ২জন একসাথে (ON UPDATE CASCADE)  
CREATE TABLE categories(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)





CREATE TABLE products(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL,
    price varchar(50) NOT NULL,
    unit varchar(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    category_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`category_id`) REFERENCES categories(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)





CREATE TABLE customers(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL,
    mobile varchar(100) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)



CREATE TABLE invoices(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    total varchar(50) NOT NULL,
    discount varchar(50) NOT NULL,
    vat varchar(50) NOT NULL,
    payable varchar(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`customer_id`) REFERENCES customers(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)








CREATE TABLE invoice_products(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    qty varchar(50) NOT NULL,
    sale_price varchar(50) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    product_id BIGINT UNSIGNED NOT NULL,
    invoice_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`product_id`) REFERENCES products(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`invoice_id`) REFERENCES invoices(`id`)  ON DELETE RESTRICT ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
    updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)