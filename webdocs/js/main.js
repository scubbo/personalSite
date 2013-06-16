// JavaScript Document
$(document).ready(function() {
  var topBarHTML = '<div id="topNavBar" class="topNavBar"><a id="topNav1" class="topNav1 topNav" href="/">Home</a><a id="topNav2" class="topNav1 topNav" href="http://nftnf.blogspot.co.uk/">Blog</a><a id="topNav3" class="topNav1 topNav" href="/sections/cool">Cool Things</a><a id="topNav4" class="topNav1 topNav" href="/sections/contact">Contact</a></div>';
  $('body').prepend($(topBarHTML));
  $(".topNavBar>a").hover(function () {
  	$(this).stop();
  	if ($(this).hasClass('topTab1Selected') || $(this).hasClass('topTab2Selected') || $(this).hasClass('topTab3Selected') || $(this).hasClass('topTab4Selected') || $(this).hasClass('topTab5Selected') || $(this).hasClass('topTab6Selected') || $(this).hasClass('topTab7Selected')) {
  	} else {
  		$(this).animate({
  			height: '45px', 
  			lineHeight: '38px',
  			marginBottom: '-5px'
  		}, 200, function() {});
  	}
  }, function () {
  	if ($(this).hasClass('topTab1SelectedOver') || $(this).hasClass('topTab2SelectedOver') || $(this).hasClass('topTab3SelectedOver') || $(this).hasClass('topTab4SelectedOver') || $(this).hasClass('topTab5SelectedOver') || $(this).hasClass('topTab6SelectedOver') || $(this).hasClass('topTab7SelectedOver')){
  	
  	} else {
  		$(this).animate({
  			height: '40px',
  			lineHeight: '33px',
  			marginBottom: '0px'
  		}, 200, function() {});
  	}
  });
});
