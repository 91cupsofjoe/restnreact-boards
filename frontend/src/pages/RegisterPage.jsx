function RegisterPage() {

    function handleSubmit(e) {
        e.preventDefault();
        alert("Mock registration complete!")
    }

    return (
        <div>
            <h1>Register</h1>

            <p>This is a placeholder Register page</p>

            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <br />
                    <input type="text" placeholder="Enter username" />
                </div>

                <br />

                <div>
                    <label>Password:</label>
                    <br />
                    <input type="password" placeholder="Enter password" />
                </div>

                <br />

                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default RegisterPage;