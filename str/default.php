<?php 	/* https://raw.githubusercontent.com/m8t/home-video-player/master/playlist-m3u.php */

	$v = isset($_GET['v']) ? $_GET['v'] : "";
	$f = isset($_GET['f']) ? $_GET['f'] : ".m3u8";

	$opts = array(
		'http'=>array(
		'method'=>"GET",
		'header'=>"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
	));

	$context = stream_context_create($opts);

	$url = 'https://pastebin.com/raw/iyiGaiE9';

	if ($v == "ssiptvarg") 
	$url = 'https://raw.githubusercontent.com/mortal251/ssiptvarg/main/nacionalygratuita.m3u';
	else if ($v == "ssiptvazul") 
	$url = 'https://raw.githubusercontent.com/mortal251/ssiptvarg/main/nacionalparaiptvazul.m3u';
	else if ($v == "ar") $url = 'http://www.m3u.cl/lista/AR.m3u';
	else if ($v == "bo") $url = 'http://www.m3u.cl/lista/BO.m3u';
	else if ($v == "cl") $url = 'http://www.m3u.cl/lista/CL.m3u';
	else if ($v == "co") $url = 'http://www.m3u.cl/lista/CO.m3u';
	else if ($v == "es") $url = 'http://www.m3u.cl/lista/ES.m3u';
	else if ($v == "mx") $url = 'http://www.m3u.cl/lista/MX.m3u';
	else if ($v == "pe") $url = 'http://www.m3u.cl/lista/PE.m3u';
	else if ($v == "ve") $url = 'http://www.m3u.cl/lista/VE.m3u';
	else if ($v == "tdt") $url = 'https://www.tdtchannels.com/lists/tv_mpd.m3u8';
	else if ($v == "pluto") $url = 'https://i.mjh.nz/PlutoTV/mx.m3u8';

	$file = file_get_contents($url);
	header ("Content-Type: video/vnd.mpegurl");
	header ("Content-Disposition: attachment;filename=hvp-playlist.m3u");
	header ("Pragma: no-cache");
	header ("Expires: 0");
	echo $file;
?>
