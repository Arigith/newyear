export default function CreateUserWorklog() {
    function createWorklog(event) {
        event.preventDefault();

        var title = document.getElementById("title").value;
        var info = document.getElementById("info").value;
        // var access_token = localStorage.getItem("access_token");

        fetch("http://127.0.0.1:8000/worklog/create", {
            method: "POST",
            // headers: {
            //     "Content-Type": "application/json",
            //     "Authorization": "Bearer " + access_token
            // },
            body: JSON.stringify({ worklog_title: title, worklog_info: info })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                return response.json();
            })
            .then(data => {
                // Handle the success response
                console.log("Worklog created successfully:", data);
                alert("Worklog created successfully!");
            })
            .catch(error => {
                // Handle the error
                console.error("Error:", error);
                alert("An error occurred. Please try again later.");
            });
    }

    return (
        <form onSubmit={createWorklog}>
            <label htmlFor="title">Title:</label>
            <input type="text" id="title" required="required" />
            <label htmlFor="info">Info:</label>
            <textarea id="info" required="required"></textarea>
            <button type="submit" className="btn btn-primary btn-block btn-large">Create</button>
        </form>
    )
}