function jPost(){
	var gu = document.getElementById("GuID");
	var dong = document.getElementById("DongID");
	
	var searchText = $('#sText').value;
	var guVar;
	var dongVar;
	
	for(i=0; i<gu.options.length; i++) {
        if(gu.options[i].selected === true) {
           guVar = gu.options[i].value;         // 어떤 값이 선택되었는지 확인해보고 
            break;								// 선택된 값을 valDong 에 저장.
        }
    }
	
    for(i=0; i<dong.options.length; i++) {
        if(dong.options[i].selected === true) {
            dongVar = dong.options[i].value;         // 어떤 값이 선택되었는지 확인해보고 
            break;								// 선택된 값을 valDong 에 저장.
        }
    }

	    var searchButton = document.getElementById("sBtn");

		 xhr = new XMLHttpRequest();
		 xhr.open("POST","/data",true);
		 xhr.setRequestHeader("Content-type","application/json");

		var obj= new Object();

		obj.si = "Seoul";
		obj.gu =guVar;
		obj.dong = dongVar;
		obj.lastAdd = searchText;
        
		 var jsonData = JSON.stringify(obj);
		try {
			xhr.send(jsonData);
		}
		catch(err) {
		console.log(err);
		 }

		//    $.ajax({
		// 	type : "POST",
		//
		// 	dataType : "json",
		//
		// 	url : "/login",
		//
		// 	data : {
		// 	json : jsonData
		// 	},
		// 	success : function(json) {
		// 				console.log("hi");
		// 	},
		// 	error : function(xhr,errmsg,err){
		// 			   	console.log("bye");
		// 	   }
		//
		// });
	
	
	
	
}