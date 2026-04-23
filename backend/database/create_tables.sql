-- users
CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW()
);

-- threads
CREATE TABLE IF NOT EXISTS threads (
	thread_id SERIAL PRIMARY KEY,
	thread_title TEXT NOT NULL,
	thread_body TEXT NOT NULL,
	user_id INT,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- posts
CREATE TABLE IF NOT EXISTS posts (
	post_id SERIAL PRIMARY KEY,
	post_body TEXT NOT NULL,
	thread_id INT NOT NULL,
	parent_post_id INT,
	user_id INT,
	created_at TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (thread_id) REFERENCES threads(thread_id) ON DELETE CASCADE,
	FOREIGN KEY (parent_post_id) REFERENCES posts(post_id) ON DELETE SET NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);