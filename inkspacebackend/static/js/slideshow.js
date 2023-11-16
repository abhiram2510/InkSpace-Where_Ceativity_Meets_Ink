// static/js/slideshow.js
$(document).ready(function() {
    var images = [
        "{% static 'images/background1.jpg' %}",
        "{% static 'images/background2.jpg' %}",
        "{% static 'images/tm-bg-slide-3.jpg' %}"
    ];

    var container = $('#slideshow-container');

    // Dynamically add image elements to the slideshow container
    for (var i = 0; i < images.length; i++) {
        var img = $('<div class="slide"></div>');
        img.css('background-image', 'url(' + images[i] + ')');
        container.append(img);
    }
});
