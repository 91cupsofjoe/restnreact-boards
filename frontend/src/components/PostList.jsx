// This component receives the array of posts and displays them one at a time

// Here we take in posts as a prop object
function PostList({posts}) {
    return (
        /*
         * This function follows the same format as ThreadList.ThreadList():
         *  (1) Check the length of the posts array, and
         *  (2) Map each post in the array to a rendered post
         *  For the each post, post the username and date the post was created
         */
        <div>
            {posts.length === 0 ? (
                <p>No posts found!</p>
            ) : (
                posts.map((post) => (
                    <div
                        key={post.post_id}
                        style={{
                            border: "1px solid #ccc",
                            padding: "12px",
                            marginBottom: "12px",
                            borderRadius: "8px"
                        }}
                    >
                        <p>{post.post_body}</p>
                        <small>
                            Posted by: {post.username} |
                            {new Date(post.created_at).toLocaleString(undefined, {
                                dateStyle: "medium",
                                timeStyle: "short"
                            })}
                        </small>
                    </div>
                )) 
            )}
        </div>
    );
}

// Don't forget to allow other components to import this one!
export default PostList;