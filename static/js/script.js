document.getElementById('toggleButton').addEventListener('click', function() {
    fetch('/update', { method: 'POST' });

    var circle = document.getElementById('statusCircle');
    circle.style.backgroundColor = 'green';

    setTimeout(function() {
        circle.style.backgroundColor = 'red';
    }, 10000); // 10 seconds
});

function updateCircle() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            const circle = document.getElementById('statusCircle');
            circle.style.backgroundColor = data.status === 'green' ? 'green' : 'red';
        });
}

// Check status every second
setInterval(updateCircle, 1000);

// Initial check
updateCircle();
