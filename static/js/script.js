document.getElementById('toggleButton').addEventListener('click', function() {
    fetch('/update', { method: 'POST' });

    var circle = document.getElementById('statusCircle');
    circle.style.backgroundColor = 'green';

    setTimeout(function() {
        circle.style.backgroundColor = 'red';
    }, 10000); // 10 seconds
});

function updateCircles() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            const statusCircle = document.getElementById('statusCircle');
            const ultrasonicCircle = document.getElementById('ultrasonicCircle');
            statusCircle.style.backgroundColor = data.button_status === 'green' ? 'green' : 'red';
            ultrasonicCircle.style.backgroundColor = data.ultrasonic_status === 'green' ? 'green' : 'red';
        });
}

// Check status every second
setInterval(updateCircles, 1000);

// Initial check
updateCircles();
