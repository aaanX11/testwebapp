$(document).ready(function(){
//main func jquery + ajax
	console.info('trrrr');
	//.class or .id does this mean contecst pr the place where i should insert data. or element on which i listnet to click wavelet
	$.getJSON({
		//type:'GET',
		url:'/home',
		success:function(data){
			var elem = document.getElementById('col-sm-2sidenav');
			var elem2 = document.querySelector("div.map-containter");
			var chld = elem.firstChild;
			console.info(chld);
			var cln = chld.cloneNode(true);//fill cln with data[0] data
			console.info(cln);
			cln.style = "visibility: visible;";
			var elemMod = document.querySelector("div.modal").cloneNode(true);
			elemMod.style = "visibility: visible;";
			//addMarker(data[0].fields.latitude, data[0].fields.longitude);
				//querySelector("#mylink > img:first-of-type")
				cln.querySelector("a:first-of-type").href = cln.querySelector("a:first-of-type").href.replace('0', data[0].pk.toString());
				cln.querySelector("a:first-of-type").textContent = data[0].fields.date;

				cln.querySelector("p.share-adress").textContent = data[0].fields.latitude.toString() +  data[0].fields.longitude.toString();
				cln.querySelector("div.share-owner").textContent = data[0].fields.source.toString();
				//cln.querySelector("a:last-of-type").textContent = "Хочу забрать";
				cln.querySelector("a:last-of-type").addEventListener('click', function(event){
					//nothing happens here 
				});
			var frag = document.createDocumentFragment();
			frag.appendChild(cln);
			elem.appendChild(frag);
			var frag2 = document.createDocumentFragment();
			frag2.appendChild(elemMod);
			elem2.appendChild(frag2);
			//console.info(data);
			//for (var i = data.length - 1; i >= 0; i--) {
			//	$('#test').append('<p>'+data[i]+'</p>');
			//}
			
		}
	});
})

function addMarker(pos1, pos2) {
	location = new google.maps.LatLng(pos1, pos2);
    marker = new google.maps.Marker({
        position: location,
        map: map
    });
}