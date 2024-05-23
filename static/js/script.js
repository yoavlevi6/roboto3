function updateCircle() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            const circle = document.getElementById('statusCircle');
            circle.style.backgroundColor = data.status;
        });
}

// Check status every second
setInterval(updateCircle, 1000);

// Initial check
updateCircle();
