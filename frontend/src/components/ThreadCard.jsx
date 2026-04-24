// ThreadList imports this component

// The argument passed in here is a destructured props object
function ThreadCard({thread, onSelectThread}) {
    return (
        /*
         * With style={{}}, the outer curly braces switch from JSX/HTML mode to
         *  Javascript, and the inner curly braces contain the actual Javascript
         *  value being passed in (which contains CSS-like properties)
         * 
         * border: pixel_thickness line_type color
         * padding: space added inside the border
         * marginBottom: space added below the card
         * borderRadius: roundness of the card's corners
         *  0px = sharp while 20px is very round
         * cursor: type of cursor, pointer = "clickable hand"
         * 
         * <h3> ... </h3> This makes the header bigger than normal text
         * <small> ... </small> This makes text smaller than paragraph text
         *  Include "[deleted]" for null usernames (similar to Reddit)
         */
        <Link
            to={'/threads/${thread.thread_id'}
            style={{
                textDecoration: "none",
                color: "inherit"
            }}
        >
            <div
                style={{
                    border: "1px solid #ccc",
                    padding: "12px",
                    marginBottom: "12px",
                    borderRadius: "8px",
                    cursor: "pointer"
                }}
            >   
                <h3>{thread.title}</h3>
                <p>{thread.body}</p>
                <small>
                    Posted by: {thread.username || "[deleted]"}
                </small>
            </div>
        </Link>
    );
}

export default ThreadCard;