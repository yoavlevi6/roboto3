$(document).ready(function() {
    $('#motorSlider').on('input', function() {
        let speed = $(this).val();
        $('#motorSpeedValue').text(speed);
        
        $.ajax({
            url: '/update_motor_speed',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({speed: speed}),
            success: function(response) {
                console.log('Motor speed updated:', response.motor_speed);
            }
        });
    });
});
