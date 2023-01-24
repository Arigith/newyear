// import React, { useState, useEffect} from "react";

// function UserLogin() {
//     const [Username,setUsername]=useState("")
//     const [Password,setPassword]=useState("")
// }

export default function handleLogin(event) {
        event.preventDefault();
    
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
    
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username: username, password: password })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                return response.json();
            })
            .then(data => {
                if (data.access_token) {
                    // Store the access token in the browser's local storage or in a cookie
                    localStorage.setItem("access_token", data.access_token);
                    // Redirect the user to a protected page
                    window.location.href = "/dashboard";
                } else {
                    // Handle the error
                    alert("Invalid username or password");
                }
            })
            .catch(error => {
                // Handle the error
                console.error("Error:", error);
                alert("An error occurred. Please try again later.");
            });
    };