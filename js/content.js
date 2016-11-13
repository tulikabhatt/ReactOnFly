function checkEmotion(){

fetch('https://localhost:5000/').then(function(res){ 
		return res.json();
	 }).then(function(raw){
	 	var json = JSON.parse(raw);

	 	console.log(json);
	 	console.log(json['value']);
	 	if(json['value']){
	 		
	 		document.querySelector('.UFILikeLink').click(); 
	 		
	 	}
	 	setTimeout(checkEmotion,5000);
	})

};


checkEmotion();