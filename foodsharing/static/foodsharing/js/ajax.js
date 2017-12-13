$(document).ready(function(){
//main func jquery + ajax
	console.info('trrrr');
	//.class or .id does this mean contecst pr the place where i should insert data. or element on which i listnet to click wavelet
		$.ajax({
			type:GET,
			url:'/home',
			success:function(data){
				for (var i = data.length - 1; i >= 0; i--) {
					$('#test').append('<p>'+data[i]+'</p>')
				}
				
			}
		});
})