// import React, { useState } from "react";

// const Loginapp = () => {

//     const [email, setEmail]=useState('');
//     const [password, setPassword]=useState('');

//     const setEmailNow = (event) => setEmail(event.target.value)
//     const setPasswordNow = (event) => setPassword(event.target.value)

//     const handleLogin = (event) => {
//         event.preventDefault();
//         console.log(email, password);
//         setEmail('');
//         setPassword('');

//         fetch('http://127.0.0.1:8000/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ username: email, password: password })
//         })
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error('HTTP error ' + response.status);
//                 }
//                 return response.json();
//             })
//             .then(data => {
//                 if (data.access_token) {
//                     // Store the access token in the browser's local storage or in a cookie
//                     localStorage.setItem('access_token', data.access_token);
//                     // Redirect the user to a protected page
//                     window.location.href = 'http://localhost:3000/worklog';
//                 } else {
//                     // Handle the error
//                     alert('Invalid username or password');
//                 }
//             })
//             .catch(error => {
//                 // Handle the error
//                 console.error('Error:', error);
//                 alert('An error occurred. Please try again later.');
//             });
//     };

//     return(
//             <form onSubmit={handleLogin}>
//                 <label htmlFor='email'>Username:</label>
//                 <input type='text' id='email' 
//                 // ref={userRef} 
//                 autoComplete='off' onChange={setEmailNow} value={email} required='required' />
//                 <label htmlFor='password'>Password:</label>
//                 <input type='password' id='password' onChange={setPasswordNow} value={password} required='required' />
//                 <button type='submit' className='btn btn-primary btn-block btn-large'>Let me in.</button>
//             </form>
//     )
// }

// export default Loginapp;

const CreateWorklogs = () => {
    function createWorklog(event) {
        event.preventDefault();

        var title=document.getElementById('title').value;
        var info=document.getElementById('info').value;
        var access_token=localStorage.getItem('access_token');

        fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer' + access_token
            },
            body: JSON.stringify({worklog_title: title, worlklog_info: info})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('HTTP Error ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log('Worklog created successfully:', data);
            alert('Worklog created successfully!');
        })
        .catch(error => {
            console.error('Error', error);
            alert('An error occurred. Please try again later.')
        });
    }
    return (
        <form onSubmit={createWorklog}>
            <label htmlFor='title'>Title</label>
            <input type='text' id='title' required='required' />
            <label htmlFor='info'>Info</label>
            <textarea id='info' required='required' />
            <button type='submit' className='btn btn-primary btn-block btn-large'>Create</button>
        </form>
    )
}

export default CreateWorklogs;