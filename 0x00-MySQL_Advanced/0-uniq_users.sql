-- creates a table users with id, email and name and id as primary key
CREATE TABLE IF NOT EXISTS  users(
	id NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY(id)
	);
