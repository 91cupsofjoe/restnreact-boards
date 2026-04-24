// One import from React and two from our other components

import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import PostList from "../components/PostList";
import CreatePostForm from "../components/CreatePostForm";
import {getPostsByThreadId, getThreadByThreadId} from "../services/api";

function ThreadDetailPage() {
    const {threadId} = useParams();
    
    const [thread, setThread] = useState(null);
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function loadThreadAndPosts() {
        try {
            setLoading(true);
            setError("");

            const threadData = await getThreadByThreadId(threadId);
            const postsData = await getPostsByThreadId(threadId);

            setThread(threadData[0]);
            setPosts(postsData);
            
        } catch (err) {
            setError("Failed to load thread!");
            console.error(err);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadThreadAndPosts();
    }, [threadId]);

    if (loading) {
        return <p>Loading thread...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!thread) {
        return <p>Thread not found!</p>;
    }

    return (
        <div>
            <h1>{thread.thread_title}</h1>
            <p>{thread.thread_body}</p>
            <small>Posted By: {thread.username}</small>

            <h2>Posts</h2>
            
            <CreatePostForm
                threadId={threadId}
                onPostCreated={loadThreadAndPosts}
            />

            <PostList posts={posts} />
        </div>
    );
}

export default ThreadDetailPage;