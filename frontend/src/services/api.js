/*
 * This service component keeps all backend communication in one place
 *  Data is fetched from FastAPI (backend), JSON parsed, and data returned
 * 
 * Consider adding later:
 *  export async function getPosts(thread_id) { ... } DONE!
 *  export async function createThread(data) { ... }
 *  export async function deleteThread(id) { ... }
 */

// Configure based on settings.env later
const API_URL = "http://127.0.0.1:8000";

// Function to fetch threads from the backend/database
export async function getThreads() {
    /*
     * This sends an HTTP GET request to the URL
     *  "${...}" inserts the variable, "/..."" is the endpoint
     * 
     * Need to use await here so that the code pauses until fetch() can return
     *  the response
     */
    const response = await fetch(`${API_URL}/threads`);
    if (!response.ok) {
        throw new Error("Failed to fetch threads!");
    }
    
    // response.json() returns a placeholder (Promise) that will eventually
    //  contain the data
    const data = await response.json();
    return data;
}

// Function to fetch threads by thread id
export async function getThreadByThreadId(threadId) {
    const response = await fetch(
        `${API_URL}/threads/thread-id/${threadId}`
    );

    if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to fetch thread by thread id:
            ${response.status} ${errorText}`);
    }

    const data = await response.json();
    return data;
}

// Function to fetch threads by username
export async function getThreadsByUsername(username) {
    const response = await fetch(
        `${API_URL}/threads/by-user/${encodeURIComponent(username)}`
    )

    if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Failed to fetch threads by username:
            ${response.status} ${errorText}`);
    }

    const data = await response.json();
    return data;
}

// Function to fetch posts by thread id
export async function getPostsByThreadId(threadId) {
    const response = await fetch(`${API_URL}/threads/${threadId}/posts`);

    if (!response.ok) {
        throw new Error("Failed to fetch posts!");
    }

    const data = await response.json();
    return data;
}

export async function createPost(postData) {
    const response = await fetch(`${API_URL}/posts`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(postData)
    });

    if (!response.ok) {
        const text = await response.text();
        console.error("Create post failed:", response.status, text);
        throw new Error("Failed to create post!");
    }

    const data = await response.json();
    return data;
}