
$(window).load(function(){
    $('.preloader').delay(1000).fadeOut("slow");  
});


$(function(){
    jQuery(document).ready(function() {
		$('body').backstretch([
	 		 "{% static '/images/background1.jpg' %}", 
	 		 "{% static '/images/background2.jpg' %}",
			 "{% static '/images/tm-bg-slide-3.jpg' %}"
	 			], 	{duration: 3200, fade: 1300});
		});
})