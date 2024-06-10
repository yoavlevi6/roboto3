function updateCircle() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            const circle = document.getElementById('statusCircle');
            circle.style.backgroundColor = data.status;
        });
}

// בדיקת הסטטוס כל שנייה
setInterval(updateCircle, 1000);

// בדיקה ראשונית
updateCircle();
