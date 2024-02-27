try {
  fetch('/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: "Your chat message here"
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Code to handle the response, update the chat UI
    })
    .catch((error) => {
      console.error('Error:', error);
    });
} catch (error) {
  console.error('Error:', error);
}
  