# This module provides SQL statements for database operations

from backend.database import database as db, schemas as sc

# ============================== PRESET FIELDS ================================

USER_FIELDS = """
    user_id,
    username,
    created_at
"""

USER_RESPONSE_FIELDS = """
    u.user_id AS user_id,
    u.username AS username,
    u.created_at AS created_at
"""

USER_SUMMARY_RESPONSE_FIELDS = USER_RESPONSE_FIELDS

THREAD_FIELDS = """
    thread_id,
    thread_title,
    thread_body,
    user_id,
    created_at
"""

THREAD_RESPONSE_FIELDS = """
    t.thread_id AS thread_id,
    t.thread_title AS thread_title,
    t.thread_body AS thread_body,
    t.user_id AS user_id,
    t.created_at AS created_at
"""

THREAD_SUMMARY_RESPONSE_FIELDS = """
    t.thread_id AS thread_id,
    t.thread_title AS thread_title,
    t.thread_body AS thread_body,
    t.user_id AS user_id,
    COALESCE (u.username, '[deleted]') AS username,
    t.created_at AS created_at
"""

POST_FIELDS = """
    post_id,
    post_body,
    thread_id,
    parent_post_id,
    user_id,
    created_at
"""

POST_RESPONSE_FIELDS = """
    p.post_id AS post_id,
    p.post_body AS post_body,
    p.thread_id AS thread_id ,
    p.parent_post_id AS parent_post_id,
    p.user_id AS user_id,
    p.created_at AS created_at
"""

POST_SUMMARY_RESPONSE_FIELDS = """
    p.post_id AS post_id,
    p.post_body AS post_body,
    p.thread_id AS thread_id ,
    t.thread_title AS thread_title,
    p.parent_post_id AS parent_post_id,
    p.user_id AS user_id,
    COALESCE (u.username, '[deleted]') AS username,
    p.created_at AS created_at
"""
    
# ========================== CREATE OPERATIONS ================================

"""
For these operations and not using PostgreSQL (e.g. MySQL), there are 3 steps:
    (1) send the query for inserting entries, (2) get the id of the inserted
    entry, and (3) fetch the full entry/row. PostgreSQL allows this to happen
    in one step via the cursor().fetchone() method.
"""

# Create a new user
def create_user(
    conn,
    us: sc.UserCreateRequest
):
    username = us.username
    password = us.password

    query = f"""
        INSERT INTO users (username, password)
        VALUES (%s, %s)
        RETURNING {USER_FIELDS}
    """
    return db.fetch_one_result(conn, query, (username, password))

# Create a new thread
def create_thread(
    conn,
    ts: sc.ThreadCreateRequest
):
    thread_title = ts.thread_title
    thread_body = ts.thread_body
    user_id = ts.user_id

    query = f"""
        INSERT INTO threads (thread_title, thread_body, user_id)
        VALUES (%s, %s, %s)
        RETURNING {THREAD_FIELDS}
    """
    return db.fetch_one_result(conn, query,
                    (thread_title, thread_body, user_id))

# Create a new post
def create_post(
    conn,
    ps: sc.PostCreateRequest
):
    post_body = ps.post_body
    thread_id = ps.thread_id
    parent_post_id = ps.parent_post_id
    user_id = ps.user_id

    query = f"""
        INSERT INTO posts (post_body, thread_id, parent_post_id, user_id)
        VALUES (%s, %s, %s, %s)
        RETURNING {POST_FIELDS}
    """
    return db.fetch_one_result(conn, query,
                    (post_body, thread_id, parent_post_id, user_id))

# ============================ DELETE OPERATIONS ==============================

ALLOWED_USER_KEYS = {"user_id"}
ALLOWED_THREAD_KEYS = {"thread_id"}
ALLOWED_POST_KEYS = {"post_id", "user_id"}

def delete_user_query(key: str):
    if key not in ALLOWED_USER_KEYS:
        raise ValueError("Invalid user key!")
    return f"""
        DELETE FROM users u
        WHERE {key} = %s
        RETURNING {USER_FIELDS}
    """

def delete_thread_query(key: str):
    if key not in ALLOWED_THREAD_KEYS:
        raise ValueError("Invalid thread key!")
    return f"""
        DELETE FROM threads t
        WHERE {key} = %s
        RETURNING {THREAD_FIELDS}
    """

def delete_post_query(key: str):
    if key not in ALLOWED_POST_KEYS:
        raise ValueError("Invalid post key!")
    return f"""
        DELETE FROM posts p
        WHERE {key} = %s
        RETURNING {POST_FIELDS}
    """

# ============================= FETCH OPERATIONS ==============================

USER_RESPONSE_FIELDS = """
    u.user_id,
    u.username,
    u.created_at
"""

USER_SUMMARY_RESPONSE_FIELDS = USER_RESPONSE_FIELDS

THREAD_SUMMARY_RESPONSE_FIELDS = """
    t.thread_id,
    t.thread_title,
    t.thread_body,
    t.user_id,
    u.username,
    t.created_at
"""

POST_SUMMARY_RESPONSE_FIELDS = """
    p.post_id,
    p.post_body,
    t.thread_id,
    t.thread_title,
    p.parent_post_id,
    p.user_id,
    u.username,
    p.created_at AS post_time
"""

# ---------------------- users ------------------------

# Lookup for user based on user id
def user_by_user_id_query():
    return f"""
        SELECT {USER_RESPONSE_FIELDS}
        FROM users u
        WHERE u.user_id = %s
    """

def user_by_username_query():
    return f"""
        SELECT {USER_SUMMARY_RESPONSE_FIELDS}
        FROM users u
        WHERE u.username ILIKE %s
    """

# Lookup for users based on thread title
def users_by_thread_title_query():
    return f"""
        WITH matched_threads AS (
            SELECT thread_id, user_id
            FROM threads
            WHERE thread_title ILIKE %s
        )
        SELECT * FROM (
            SELECT {USER_SUMMARY_RESPONSE_FIELDS}
            FROM users u
            JOIN posts p ON p.user_id = u.user_id
            JOIN matched_threads mt ON mt.thread_id = p.thread_id

            UNION

            SELECT {USER_SUMMARY_RESPONSE_FIELDS}
            FROM users u
            JOIN matched_threads mt ON mt.user_id = u.user_id
        ) AS matched_users
        ORDER BY username ASC
    """
    # username is an alias of u.username

# ---------------------- threads ------------------------

# Lookup for thread based on thread id
def thread_by_thread_id_query():
    return """
        SELECT
            t.*
        FROM threads t
        WHERE t.thread_id = %s
    """

# Lookup for threads based on thread title
def threads_by_thread_title_query():
    return f"""
        SELECT {THREAD_SUMMARY_RESPONSE_FIELDS}
        FROM threads t
        LEFT JOIN users u ON t.user_id = u.user_id
        WHERE t.thread_title ILIKE %s
        ORDER BY t.created_at DESC
    """

# Lookup for threads based on username
def threads_by_username_query():
    return f"""
        SELECT {THREAD_SUMMARY_RESPONSE_FIELDS}
        FROM threads t
        JOIN users u ON t.user_id = u.user_id
        WHERE u.username ILIKE %s
        ORDER BY t.created_at DESC
    """

# Lookup for threads based on thread body
def threads_by_keyword_query():
    return f"""
        SELECT {THREAD_SUMMARY_RESPONSE_FIELDS}
        FROM threads t
        LEFT JOIN users u ON t.user_id = u.user_id
        WHERE t.thread_body ILIKE %s
        ORDER BY t.created_at DESC
    """

# ---------------------- posts ------------------------

# Lookup for post based on post id
def post_by_post_id_query():
    return """
        SELECT
            p.*
        FROM posts p
        WHERE p.post_id = %s
    """

### DO NOT USE THESE FOR NOW, CURRENTLY USED FOR REFERENCE ###
# Lookup for posts based on username
def posts_by_username_query():
    return f"""
        SELECT {POST_SUMMARY_RESPONSE_FIELDS}
        FROM posts p
        JOIN threads t ON p.thread_id = t.thread_id
        JOIN users u ON p.user_id = u.user_id
        WHERE u.username ILIKE %s
        ORDER BY p.created_at DESC
    """

# Lookup for posts based on thread titles
def posts_by_thread_title_query():
    return f"""
        SELECT {POST_SUMMARY_RESPONSE_FIELDS}
        FROM posts p
        JOIN threads t ON p.thread_id = t.thread_id
        LEFT JOIN users u ON p.user_id = u.user_id
        WHERE t.thread_title ILIKE %s
        ORDER BY p.created_at DESC
    """

# Lookup for posts based on post bodies (texts)
def posts_by_keyword_query():
    return f"""
        SELECT {POST_SUMMARY_RESPONSE_FIELDS}
        FROM posts p
        JOIN threads t ON p.thread_id = t.thread_id
        LEFT JOIN users u ON p.user_id = u.user_id
        WHERE p.post_body ILIKE %s
        ORDER BY p.created_at DESC
    """
    
# =============================================================================