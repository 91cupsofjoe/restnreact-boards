SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'forum_db'
  AND pid <> pg_backend_pid();

DROP DATABASE IF EXISTS forum_db;
CREATE DATABASE forum_db;