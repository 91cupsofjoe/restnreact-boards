// One import from React and two from our other components

import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import PostList from "../components/PostList";
import CreatePostForm from "../components/CreatePostForm";
import {getPostsByThreadId} from "../services/api";

function ThreadDetailPage({thread}) {
    const {threadId} = useParams();
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function loadPosts() {
        try {
            setLoading(true);
            setError("");
            const data = await getPostsByThreadId(thread.thread_id);
            setPosts(data);
        } catch (err) {
            setError("Failed to load posts!")
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadPosts();
    }, [thread.thread_id]);

    if (loading) {
        return <p>Loading posts...</p>;
    }

    if (error) {
        return <p>{error}</p>
    }

    return (
        <div>
            <h1>Thread Posts</h1>
            <p>{thread.body}</p>
            
            <CreatePostForm
                threadId={threadId}
                onPostCreated={loadPosts}
            />

            <PostList posts={posts} />
        </div>
    );
}

export default ThreadDetailPage;