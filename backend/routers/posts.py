# This module is for routing POST / GET messages related to posts

from fastapi import APIRouter

from backend.database import crud as cd, schemas as sc
from backend.routers import util
from typing import Optional

posts_router = APIRouter()
post_response_keys = [
    "post_id",
    "post_body",
    "thread_id",
    "parent_post_id",
    "user_id",
    "created_at"
]
post_summary_response_keys = [
    "post_id",
    "post_body",
    "thread_id",
    "thread_title",
    "parent_post_id",
    "user_id",
    "username",
    "created_at"
]

# ============================= POST methods ==================================

# Create a new post
@posts_router.post("/posts",
                response_model=sc.PostResponse)
def create_new_post(
    post_body: str,
    thread_id: int,
    user_id: int,
    parent_post_id: Optional[int] = None,
):
    return util.create_new_entry(
        sc.PostCreateRequest(
            post_body=post_body,
            thread_id=thread_id,
            parent_post_id=parent_post_id,
            user_id=user_id
        ),
        post_response_keys,
        sc.PostResponse,
        cd.create_post,
        "post"
    )

# ============================= DELETE methods ================================

# Delete a post by post id
@posts_router.delete("/posts/{post_id}", response_model=sc.PostResponse)
def delete_post(post_id: int):
    return util.get_search_results(
        cd.delete_post_query("post_id"),
        [post_id],
        post_response_keys,
        sc.PostResponse,
        "post",
        single_result=True
    )

# Delete posts by user id
@posts_router.delete("/users/{user_id}/posts",
                response_model=list[sc.PostResponse])
def delete_posts_by_user(user_id: int):
    return util.get_search_results(
        cd.delete_post_query("user_id"),
        [user_id],
        post_response_keys,
        sc.PostResponse,
        "post",
        single_result=False
    )

# =============================== GET methods ==================================

# Fetch post by post id
@posts_router.get("/posts/post-id/{post_id}", response_model=list[sc.PostResponse])
def get_post_by_post_id(post_id: int):
    return util.get_search_results(
        cd.post_by_post_id_query(),
        [post_id],
        post_response_keys,
        sc.PostResponse,
        "posts",
        single_result=False
    )

# Fetch posts by username
@posts_router.get("/posts/by-user/{username}",
                response_model=list[sc.PostSummaryResponse])
def get_posts_by_username(username: str):
    return util.get_search_results(
        cd.posts_by_username_query(),
        [f"%{username}%"],
        post_summary_response_keys,
        sc.PostSummaryResponse,
        "posts",
        single_result=False
    )

# Fetch posts by thread title
@posts_router.get("/posts/in-thread/{thread_title}",
                response_model=list[sc.PostSummaryResponse])
def get_posts_by_thread_title(thread_title: str):
    return util.get_search_results(
        cd.posts_by_thread_title_query(),
        [f"%{thread_title}%"],
        post_summary_response_keys,
        sc.PostSummaryResponse,
        "posts",
        single_result=False
    )

# Fetch posts by post body (keyword)
@posts_router.get("/posts/keyword/{keyword}",
                response_model=list[sc.PostSummaryResponse])
def get_posts_by_keyword(keyword: str):
    return util.get_search_results(
        cd.posts_by_keyword_query(),
        [f"%{keyword}%"],
        post_summary_response_keys,
        sc.PostSummaryResponse,
        "posts",
        single_result=False
    )