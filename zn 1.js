

function sendData() {
    const data = document.getElementById("dataInput").value;
    fetch('http://localhost:8000/send_to_telegram', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify({data: data})
    })
    .then(response => response.json())
    .then(data => {
    console.log(data);
    alert("Data sent to Telegram!");
    })
    .catch(error => {
    console.error('Error:', error);
    alert("Error sending data to Telegram");
    });
    }
    