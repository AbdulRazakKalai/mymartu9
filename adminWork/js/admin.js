
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
$(document).on("click", "#uploads", function () {
     var sesskey = "10";
     console.log("the request");
     //var files = $("#files").files[0];
     var files = $('input#files')[0].files[0] 
     var category = $("#category").val();
     var fileData = new FormData();
     var xhr = new XMLHttpRequest();
     fileData.append("files",files);
     fileData.append('category',category); 
     xhr.open("post", 'uploadZippImage', true);
       xhr.send(fileData)
      xhr.onreadystatechange = function (oEvent) {
            if (xhr.readyState === 4) {
               if (xhr.status === 200 ) {
                  // console.log('readyState- '+fileName+' :',xhr.readyState,'status- '+fileName+' :',xhr.status);
                  //callback (JSON.parse(xhr.responseText));
                  if( xhr.responseText == 'True'){
                   swal({
                     title: 'success',
                     type: "success",
                     text: 'File Uploaded Successfully',
                     showCancelButton: false,
                     showConfirmButton: true,
                     html:true
                    });
                 }else{
                    swal({
                          title: 'Error',
                          type: "error",
                          text: 'uploaded file allready exist in martu9',
                          showCancelButton:false,
                          showConfirmButton: true,
                          html:true
                     });
                 }
               }
               else {
                  swal({
                     title: 'error',
                     type: "Error",
                     text: 'Error while Uploading file',
                     showCancelButton: false,
                     showConfirmButton: true,
                     html:true
                    });
            }
         }
     };
 
});


/* Change Passwod

@param1: currentPassword
@param2: newPassword
@response: True / False  ( True or False indicate the sucess or Failur of uploaded File)

*/


$(document).on("click", "#newpswd", function () {
   console.log("newpswd...");
   var sesskey = 10;
	 var oldPassword = $("#change-pswd").val();
   var newPassword = $("#confirm-pswd").val();
   console.log("Password:",oldPassword,newPassword);
   $.post('/changePassword',{'sesskey':sesskey,'oldPassword':oldPassword,'newPassword':newPassword},function(data){
        if(data == "True"){
            swal({
                     title: 'success',
                     type: "success",
                     text: 'Password Changed Successfully',
                     showCancelButton: false,
                     showConfirmButton: true,
                     html:true
                    });
        }else{
    swal({
            title: 'Error' ,
            type: "error",
            text: "Please Enter Your Correct Previous Password ",
            timer: 3000,
            showConfirmButton: true
        });
        }
    });
	
});

/* Upload data Handler For Uploading data file

@param1: file
@response: True / False  ( True or False indicate the sucess or Failur of uploaded File)

*/
$(document).on("click", "#uploadData", function () {
     console.log("the request");
     //var files = $("#files").files[0];
     var files = $('input#upload-data-file')[0].files[0] 
     var fileData = new FormData();
     var xhr = new XMLHttpRequest();
     console.log("files",files)
     fileData.append("files",files);
     xhr.open("post", 'uploadDataFile', true);
       xhr.send(fileData)
      xhr.onreadystatechange = function (oEvent) {
            if (xhr.readyState === 4) {
               if (xhr.status === 200 ) {
                  // console.log('readyState- '+fileName+' :',xhr.readyState,'status- '+fileName+' :',xhr.status);
                  //callback (JSON.parse(xhr.responseText));
                  if( xhr.responseText == 'True'){
                   swal({
                     title: 'success',
                     type: "success",
                     text: 'File Uploaded Successfully',
                     showCancelButton: false,
                     showConfirmButton: true,
                     html:true
                    });
                 }else{
                    swal({
                          title: 'Error',
                          type: "error",
                          text: 'uploaded file allready exist in martu9',
                          showCancelButton:false,
                          showConfirmButton: true,
                          html:true
                     });
                 }
               }
               else {
                  swal({
                     title: 'error',
                     type: "Error",
                     text: 'Error while Uploading file',
                     showCancelButton: false,
                     showConfirmButton: true,
                     html:true
                    });
            }
         }
     };
 
});
