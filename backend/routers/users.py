# This module is for routing POST / GET messages related to users

from fastapi import APIRouter

from backend.database import crud as cd, schemas as sc
from backend.routers import util

users_router = APIRouter()
user_response_keys = [
    "user_id",
    "username",
    "created_at"
]
user_summary_response_keys = [
    "user_id",
    "username",
    "created_at"
]

# ============================= POST methods ==================================

# Create a new user
@users_router.post("/users", response_model=sc.UserResponse)
def create_new_user(us: sc.UserCreateRequest):
    """
    User create params:
        username: str,
        password: str
    """
    return util.create_new_entry(
        us,
        user_response_keys,
        sc.UserResponse,
        cd.create_user,
        "user"
    )

# ============================= DELETE methods ================================

# Delete a user
@users_router.delete("/users/{user_id}",
                response_model=sc.UserResponse)
def delete_user(user_id: int):
    return util.get_search_results(
        cd.delete_user_query("user_id"),
        [user_id],
        user_response_keys,
        sc.UserResponse,
        "user",
        single_result=True
    )

# =============================== GET methods ==================================

# Fetch all threads
@users_router.get("/users", response_model=list[sc.UserSummaryResponse])
def get_all_users():
    return util.get_search_results(
        cd.all_users_query(),
        [],
        user_summary_response_keys,
        sc.UserSummaryResponse,
        "users",
        single_result=False
    )

# Fetch user by user id
@users_router.get("/users/user-id/{user_id}", response_model=sc.UserResponse)
def get_user_by_user_id(user_id: int):
    return util.get_search_results(
        cd.user_by_user_id_query(),
        [user_id],
        user_response_keys,
        sc.UserResponse,
        "users",
        single_result=True
    )

# Fetch user by username
@users_router.get("/users/username/{username}",
                response_model=sc.UserSummaryResponse)
def get_user_by_username(username: str):
    return util.get_search_results(
        cd.user_by_username_query(),
        [f"%{username}%"],
        user_response_keys,
        sc.UserResponse,
        "users",
        single_result=True
    )

# Fetch users by thread title
@users_router.get("/threads/{thread_title}/users",
                response_model=list[sc.UserSummaryResponse])
def get_users_by_thread_title(thread_title: str):
    return util.get_search_results(
        cd.users_by_thread_title_query(),
        [f"%{thread_title}%"],
        user_summary_response_keys,
        sc.UserSummaryResponse,
        "users",
        single_result=False
    )

# =============================================================================