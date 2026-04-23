# This module is for routing POST / GET messages related to threads

from fastapi import APIRouter

from backend.database import crud as cd, schemas as sc
from backend.routers import util

threads_router = APIRouter()
thread_response_keys = [
        "thread_id",
        "thread_title",
        "thread_body",
        "user_id",
        "created_at"
]
thread_summary_response_keys = [
    "thread_id",
    "thread_title",
    "thread_body",
    "user_id",
    "username",
    "created_at"
]

# ============================= POST methods ==================================

# Create a new thread
@threads_router.post("/threads", response_model=sc.ThreadResponse)
def create_new_thread(
    thread_title: str,
    thread_body: str,
    user_id: int
):
    return util.create_new_entry(
        sc.ThreadCreateRequest(
            thread_title=thread_title,
            thread_body=thread_body,
            user_id=user_id
        ),
        thread_response_keys,
        sc.ThreadResponse,
        cd.create_thread,
        "thread"
    )

# ============================= DELETE methods ================================

# Delete a thread
@threads_router.delete("/threads/{thread_id}",
                response_model=sc.ThreadResponse)
def delete_thread(thread_id: int):
    return util.get_search_results(
        cd.delete_thread_query("thread_id"),
        [thread_id],
        thread_response_keys,
        sc.ThreadResponse,
        "thread",
        single_result=True
    )

# =============================== GET methods ==================================

# Fetch threads by thread id
@threads_router.get("/threads/thread-id/{thread_id}",
                response_model=list[sc.ThreadResponse])
def get_threads_by_thread_id(thread_id: int):
    return util.get_search_results(
        cd.thread_by_thread_id_query(),
        [thread_id],
        thread_response_keys,
        sc.ThreadResponse,
        "threads",
        single_result=False
    )

# Fetch threads by thread title
@threads_router.get("/threads/thread-title/{thread_title}",
                response_model=list[sc.ThreadSummaryResponse])
def get_threads_by_thread_title(thread_title: str):
    return util.get_search_results(
        cd.threads_by_thread_title_query(),
        [f"%{thread_title}%"],
        thread_summary_response_keys,
        sc.ThreadSummaryResponse,
        "threads",
        single_result=False
    )

# Fetch threads by username
@threads_router.get("/threads/by-user/{username}",
                response_model=list[sc.ThreadSummaryResponse])
def get_threads_by_username(username: str):
    return util.get_search_results(
        cd.threads_by_username_query(),
        [f"%{username}%"],
        thread_summary_response_keys,
        sc.ThreadSummaryResponse,
        "threads",
        single_result=False
    )

# Fetch threads by thread body (keyword)
@threads_router.get("/threads/keyword/{keyword}",
                response_model=list[sc.ThreadSummaryResponse])
def get_threads_by_keyword(keyword: str):
    return util.get_search_results(
        cd.threads_by_keyword_query(),
        [f"%{keyword}%"],
        thread_summary_response_keys,
        sc.ThreadSummaryResponse,
        "threads",
        single_result=False
    )

# ============================= Helper methods ================================


# =============================================================================