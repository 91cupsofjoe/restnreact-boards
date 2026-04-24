/* 
 * This React component displays a list of threads
 *
 * ThreadList = the whole list
 * ThreadCard = the thread that's rendered on screen
 */

// Look for the ThreadCard component (class) in the same directory
//  and import its default (no need to specify ".jsx" at the end of the name)
import ThreadCard from "./ThreadCard";

export function ThreadList({threads, onSelectThread}) {
    /*
     * {threads, onSelectThread} is a destructuring of a "prop" object for
     *  easier access of its members (props.threads and props.onSelectThread)
     * 
     * threads = the array of thread data (JSON array)
     * onSelectThread = a function to run when a thread is clicked on
     */
    return (
        /*
         * We're returning a UI here
         *
         * <div></div> is just a generic container/outer wrapper
         *  (React component needs to return this outer wrapper around content)
         * 
         * threads.length === 0 checks to see if threads array length is BOTH
         *  an integer and equal to 0 (hence "===" as opposed to "==")
         *  This check uses a ternary operator ->
         *      condition ? do_if_true : do_if_false
         * 
         * <p>No threads found!</p> Displays the text in a rendered paragraph
         * 
         * threads.map((thread)) => (<ThreadCard ... />) Loops through threads
         *  and turns each element into a React object (ThreadCard)
         * 
         * "thread", some thread data, and "onSelectThread", a function, are
         *  passed down from ThreadList to ThreadCard
         *  This makes it so the parent (ThreadList) controls the component
         *      logic, while the child (ThreadCard) controls the UI look +
         *      events. This means that data does down while actions go up,
         *      which is a good React + general architectural pattern to apply
         */
        <div>
            {threads.length === 0 ? (
                <p>No threads found!</p>
            ) : (
                threads.map((thread) => (
                    <ThreadCard
                        key={thread.thread_id}
                        thread={thread}
                    />
                ))
            )}
        </div>
    );
}

// Make ThreadList component available for other components to import
export default ThreadList;