
var map;

function myMap() {
  var stavanger = new google.maps.LatLng(58.983991,5.734863);
  var amsterdam = new google.maps.LatLng(52.395715,4.888916);
  var london = new google.maps.LatLng(51.508742,-0.120850);
  var myCenter = new google.maps.LatLng(55.751244, 37.618423);

  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 10};
  map = new google.maps.Map(mapCanvas,mapOptions);
  console.info("main.js")
  
  //flightPath.setMap(map);
  
  var marker=new google.maps.Marker({
  		position:myCenter
  });
  marker.setMap(map); 

  var infowindow = new google.maps.InfoWindow({
  content:"Hello World!"
  });

	//infowindow.open(map,marker); 
}


//function addMarker(pos1, pos2) {
 //    location = new google.maps.LatLng(pos1, pos2);
   //     marker = new google.maps.Marker({
     //       position: location,
       //     map: map
        //});
    //}

