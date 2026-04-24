import {useState} from "react";
import {createPost} from "../services/api";

function CreatePostForm({threadId, onPostCreated}) {
    const [body, setBody] = useState("");
    const [error, setError] = useState("");
    const testId = localStorage.getItem("userId");

    if (!testId) {
        setError("You must be logged in to post!");
        return;
    }

    async function handleSubmit(e) {
        e.preventDefault();

        if (!body.trim()) {
            setError("Post cannot be empty!");
            return;
        }

        try {
            setError("");

            await createPost({
                post_body: body,
                thread_id: Number(threadId),
                user_id: Number(testId)
            });

            setBody("");
            onPostCreated();
        } catch (err) {
            console.error(err);
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