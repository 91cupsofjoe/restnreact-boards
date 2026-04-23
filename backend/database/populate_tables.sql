TRUNCATE TABLE posts, threads, users RESTART IDENTITY CASCADE;

INSERT INTO users (username, password)
VALUES ('joe', '101505'),
    ('adam', '01040113'),
    ('mike', '13091105'),
    ('ash', '011908'),
    ('joshua', '1015192101'),
    ('diego', '0409050715'),
    ('ryan', '18250114'),
    ('olivia', '151209220901'),
    ('bianca', '020901140301');

INSERT INTO threads (thread_title, thread_body, user_id)
VALUES
    (
        'How Is My Driving',
        'I just wanted to get a sense of how I am progressing!',
        1
    ),
	(
        'the big dinosaur',
        'dinosaurs are the coolest like my dad!',
        2
    ),
	(
        'The Phenomenology of Consciousness Pt. 3',
        'Transitioning from reading David Chalmers to thinkers such as
        Sebastian Watzl, we might be able to understand consciousness better
        from the multiple perspectives in theories of attention.', 5
    ),
	(
        'What Does a Modern-Day Journey in Dantes Inferno Look Like?',
        'This is a thread to offer possible interpretations of Dantes Inferno
        that might apply to contexts in our modern-day/contemporary society.',
        9
    );

INSERT INTO posts (post_body, thread_id, user_id)
VALUES
	(
        'Youre not doing too shabby, keep at it!',
        1,
        5
    ),
	(
        'Aww, thank you my son! <3',
        2,
        1
    ),
	(
        'Why are we looking at attention for theories about consciousness?
        I thought this was already debunked in The Digital Circus?',
        3,
        NULL
    );