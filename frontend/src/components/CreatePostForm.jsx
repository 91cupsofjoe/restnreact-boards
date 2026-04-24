import {useState} from "react";
import {createPost} from "../services/api";

function CreatePostForm({threadId, onPostCreated}) {
    const [body, setBody] = useState("");
    const [error, setError] = useState("");

    async function handleSubmit(e) {
        e.preventDefault();

        if (!body.trim()) {
            setError("Post cannot be empty!");
            return;
        }

        try {
            setError("");

            await createPost({
                body: body,
                thread_id: Number(threadId),
                parent_post_id: null,
                user_id: 1
            });

            setBody("");
            onPostCreated();
        } catch (err) {
            setError("Failed to create post!");
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <h3>Create Post</h3>

            <textarea
                value={body}
                onChange={(e) => setBody(e.target.value)}
                placeholder="Write your post..."
            />

            <br />

            <button type="submit">Post</button>

            {error && <p>{error}</p>}
        </form>
    );
}

export default CreatePostForm;