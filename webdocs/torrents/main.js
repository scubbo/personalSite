console.log('loaded');
/*$(document).ready(function() {
	/*$.post('/cgi-bin/getPiDiskUsage.sh', 
		function(data) {
			console.log(data);
		}
	);*/ /*

	$('#searchbox').keydown(function() {
		if (event.which == 13) {
			//getTorrents();

		}
	});
});

function getTorrents() {
	$('#torrents').html('<tr><th id="titleHeader">Title</th><th id="seedsHeader">Seeds</th><th id="directLinkHeader">Direct Link</th><th id="directDownloadHeader">Start Download</th>');
	$.post('/cgi-bin/torrentSearch.py', {'query':$('#searchbox').val()}, 
		function(data) {
			$.each(data, function(i, val) {
				$('#torrents').append('<tr><td>' + val.title + '</td><td>' + val.seeds + '</td><td><a href="' + val.url + '">Direct Link</a></td><td><a class="directDownload" x-url="' + val.url + '" x-hash="' + val.hash + '" x-title="' + val.title + '">START DOWNLOAD</a></td></tr>');
			});
			$('.directDownload').click(function() {
				$(this).parent().parent().fadeOut();
				$.post('/cgi-bin/startDownload.py', {'url':$(this).attr('x-url'), 'hash':$(this).attr('x-hash'), 'title':$(this).attr('x-title')});
			});
		}
	);
	
}*/
