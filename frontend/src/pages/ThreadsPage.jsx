/*
 * This is a page component fetches data from the backend,
 *  stores the data in a React state,
 *  handles loading and error conditions,
 *  and passes the data into ThreadList
 * 
 * ThreadsPage = owns the thread data and behavior
 * ThreadList = organizes the list
 * ThreadCard = displays each item and triggers clicks
 */

/*
 * The imports:
 *  (1) First import is for two React tools ("react" exports) called hooks
 *      useState = Lets a component store changing values
 *      useEffect = Lets a component run code at certain points, like when
 *          a page loads initially
 * (2) Second import is for the ThreadList component
 * (3) Third import is from our api.js in services
 */
import {useEffect, useState} from "react";
import {ThreadList} from "../components/ThreadList";
import {getThreads} from "../services/api";

// First create the "ThreadsPage" page component
function ThreadsPage() {

    /*
     * useState([]) creates a state variable (initially empty) to store threads
     *  Here, threads (current state value) and setThreads (function used to
     *  update threads) are a common pair 
     */
    const [threads, setThreads] = useState([]);
    /*
     * useState() here is for a loading flag
     *  Keep the page in the "loading" state until it finishes (then loading
     *  becomes "false")
     */
    const [loading, setLoading] = useState(true);
    /*
     * useState() here is for storing error messages
     *  Starts off as empty string, will become an API-specific error message
     */ 
    const [error, setError] = useState("");
    /*
     * useEffect(() => {}) starts a React effect, which allows for the code
     *  after the page renders, after which the page loads threads
     */
    useEffect(() => {
        /*
         * loadThreads() is an asynchronous function that catches errors
         *  via "await ..." = Pause here until getThreads() finishes
         */
        async function loadThreads() {
            try {
                const data = await getThreads();
                // This will re-render the page component with the new data
                //  which is stored in the state
                setThreads(data);
            } catch (err) {
                console.error("loadThreads error:", err)
                // This will set an error message in the state
                // setError("Failed to load threads!");
                setError(err.message);
            // Regardless of error or not, stop page loading
            } finally {
                setLoading(false);
            }
        }

        // Runs the asynchronious function defined above
        loadThreads();
    // The empty [] here is a dependency array, which tells the component to
    //  run the effect useEffect() only once (initial rendering)
    }, []);

    /*
     * This function gets passed down to ThreadList and ThreadCard for the
     *  loaded thread page
     *  Just logs the thread to console for now
     */
    function handleSelectThread(thread) {
        console.log("Selected thread:", thread);
    }

    if (loading) {
        return <p>Loading threads...</p>
    }

    if (error) {
        return <p>{error}</p>
    }

    /*
     * Upon successful loading (no longer loading), render this
     * Both the current threads state (threads) and the handle function
     *  (handleSelectThread) are passed to ThreadList (the list component),
     *  which then passes these down to ThreadCard (the child component)
     */
    return (
        <div>
            <h1>Forum Threads</h1>
            <ThreadList
                threads={threads}
                onSelectThread={handleSelectThread}
            />
        </div>
    );
}

export default ThreadsPage;