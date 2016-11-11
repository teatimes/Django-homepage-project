
var $window = $(window),
		$stickyEl = $('.myStickyEl'),
		elTop = $stickyEl.offset().top;
		console.log("ElTop: " + elTop);

$window.scroll(function() {
	$stickyEl.toggleClass('mySticky', $window.scrollTop() > elTop);
	console.log("ElTop: " + elTop);
})


/* To the top button */
$(document).ready(function(){
	
	console.log("To top: ", $(this).scrollTop());

	var scrollButton = document.getElementsByClassName("scrollToTop")[0];

	//Check to see if the window is top if not then display button
	$(window).scroll(function(){
		//console.log("To top: ", $(this).scrollTop());
		if ($(this).scrollTop() > 100) {
			scrollButton.classList.add("show");
			scrollButton.classList.remove("hide");
		} else {
			scrollButton.classList.add("hide");
			scrollButton.classList.remove("show");
		}
	});

	//Click event to scroll to top
	$('.scrollToTop').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});

});

/**
 * Check a href for an anchor. If exists, and in document, scroll to it.
 * If href argument ommited, assumes context (this) is HTML Element,
 * which will be the case when invoked by jQuery after an event
 */
function scroll_if_anchor(href) {
    href = typeof(href) == "string" ? href : $(this).attr("href");
    
    // You could easily calculate this dynamically if you prefer
    var fromTop = 90;
    
    // If our Href points to a valid, non-empty anchor, and is on the same page (e.g. #foo)
    // Legacy jQuery and IE7 may have issues: http://stackoverflow.com/q/1593174
    if(href.indexOf("#") == 0) {
        var $target = $(href);
        
        // Older browser without pushState might flicker here, as they momentarily
        // jump to the wrong position (IE < 10)
        if($target.length) {
            $('html, body').animate({ scrollTop: $target.offset().top - fromTop });
            if(history && "pushState" in history) {
                history.pushState({}, document.title, window.location.pathname + href);
                return false;
            }
        }
    }
}    

// When our page loads, check to see if it contains and anchor
scroll_if_anchor(window.location.hash);

// Intercept all anchor clicks
$("body").on("click", "a", scroll_if_anchor);