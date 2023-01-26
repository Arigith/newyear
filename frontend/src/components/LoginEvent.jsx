import React, { useState } from "react";

export default function LoginSetup() {
    const {email, setEmail}=useState(null);
    const {password, setPassword}=useState(null);

    // const handleEmailInput = (event) => {setEmail(event.target.email[0])};
    // const handlePasswordInput = (event) => {setPassword(event.target.password[0])};

    function handleLogin(event) {
        event.preventDefault();
    
        // var email = document.getElementById('email').value;
        // var password = document.getElementById('password').value;
        fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: email, password: password })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('HTTP error ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                if (data.access_token) {
                    // Store the access token in the browser's local storage or in a cookie
                    localStorage.setItem('access_token', data.access_token);
                    // Redirect the user to a protected page
                    window.location.href = 'http://localhost:3000/worklog';
                } else {
                    // Handle the error
                    alert('Invalid username or password');
                }
            })
            .catch(error => {
                // Handle the error
                console.error('Error:', error);
                alert('An error occurred. Please try again later.');
            });
    };

    return (
        <form onSubmit={handleLogin}>
            <input type='text' id='email' placeholder='email' required='required' />
            {/* <input type='text' id='email' placeholder='email' required='required' onChange={handleEmailInput} /> */}
            <input type='password' id='password' placeholder='Password' required='required' />
            {/* <input type='password' id='password' placeholder='Password' required='required' onChange={handlePasswordInput} /> */}
            <button type='submit' className='btn btn-primary btn-block btn-large'>Let me in.</button>
        </form>
    )
}