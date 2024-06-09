// קוד לחיישן מגנט
function handleMagnetSensorEvent(event) {
    const magnetStatus = event.data;

    if (magnetStatus === 'detected') {
        document.getElementById('magnetSensorStatus').style.color = 'green';
        document.getElementById('magnetSensorStatus').innerText = 'מגנט זוהה';
    } else {
        document.getElementById('magnetSensorStatus').style.color = 'black';
        document.getElementById('magnetSensorStatus').innerText = 'לא זוהה מגנט';
    }
}

// קוד לחיישן אולטרהסוניק
function handleUltrasonicSensorEvent(event) {
    const distance = event.data;

    if (distance < 25) {
        document.getElementById('ultrasonicSensorStatus').style.color = 'green';
        document.getElementById('ultrasonicSensorStatus').innerText = 'מצטבר במרחק קרוב מדי';
    } else {
        document.getElementById('ultrasonicSensorStatus').style.color = 'black';
        document.getElementById('ultrasonicSensorStatus').innerText = 'אין מצטבר במרחק קרוב';
    }
}

// ספריה לתקשורת בין ESP לדפדפן
const eventSource = new EventSource('/events');

// לקרוא תגובות מהשרת עבור כל חיישן
eventSource.addEventListener('magnetSensor', handleMagnetSensorEvent);
eventSource.addEventListener('ultrasonicSensor', handleUltrasonicSensorEvent);
