
/* Log in handler For Login Fuction

@param1 : userName 
@param2 : passWord
@respons : True / False

*/

$(document).on("click", "#login_btn", function () {
	 var sesskey = "10";
	 console.log("the request");
	 var userName = $("#login_username").val();
	 var passWord = $("#password").val();
	 $.post('/validateLogin',{'sesskey':sesskey,'userName':userName,'passWord':passWord},function(data){
        if(data == "True"){
          	console.log("respons relesed",data);
          	window.location.href = 'adminindex? seeskey='+sesskey
        }else{
		swal({
            title: 'Error' ,
            type: "error",
            text: "User Name or Password is Incorrect",
            timer: 3000,
            showConfirmButton: true
        });
        }
    });

});



/* Upload zipp Handler For Uploading zipp

@param1: file
@param2: category
@response: True / False  ( True or False indicate the sucess or Failur of uploaded File)

*/
$(document).on("click", "#upload", function () {
	
	
});

