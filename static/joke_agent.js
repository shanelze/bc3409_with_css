function generateNewResponse() {

    console.log('Button clicked'); // Confirm the button click

    // Attempt to find and clear the initial response
    const initialResponse = document.getElementById('initialResponse');
    if (initialResponse) {
        console.log('Initial response found. Clearing it now.');
        initialResponse.innerHTML = ''; // Clear the initial joke
    } else {
        console.log('Initial response not found.');
    }

    // Clear the new response container
    const responseContainer = document.getElementById('responseContainer');
    responseContainer.innerHTML = '';

    fetch('/generate', { // The fetch() function is used to make a network request to the specified URL. Here, it’s making a request to the /generate endpoint on your server
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'generate_new_response' }) // Serialize the outgoing data
    })
    .then(response => response.json()) // Converts a JSON string received from the server into a JavaScript object.
    .then(data => {
        // Update the response in the DOM
        document.getElementById('responseContainer').innerHTML = `<h4>Reply:</h4><p>${data.r}</p>`; // Dynamically inserts the value of data.r into the string.
    })
    .catch(error => console.error('Error:', error)); // Handles any errors that occur during the fetch operation.
}

// Outgoing Request: Before sending data to the server, it must be serialized into a format (JSON string) that can be transmitted over HTTP. This is done with JSON.stringify().
// Incoming Response: When receiving data from the server, it arrives as a JSON string, which needs to be deserialized into a usable JavaScript object. This is done with response.json().
