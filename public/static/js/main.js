function login(){
uname=document.getElementById("username").value
pwd=document.getElementById("password").value
csrf=document.getElementById("csrf").value


if(uname=='' || pwd== ''){
    alert("Enter proper Credentials.")
}

var data={
    "username":uname,
    "password":pwd
}

fetch('/api/login', {
    method: 'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrf
    },
    'body':JSON.stringify(data)
}).then(result => result.json())
.then(response => {
    console.log(response)
   if(response.status==200){
    window.location.href='/'
   }
   else{
       alert(response.message)
   }
})


}

function register(){
    uname=document.getElementById("username").value
    pwd=document.getElementById("password").value
    email=document.getElementById("email").value
    csrf=document.getElementById("csrf").value
    
    
    if(uname=='' || pwd== ''){
        alert("Enter proper Credentials.")
    }
    
    var data={
        "username":uname,
        "password":pwd,
        "email":email
    }
    
    fetch('/api/register', {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf
        },
        'body':JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
       if(response.status==200){
        alert(response.message);
        //window.location.href='/'
        window.location.href='login'
       }
       else{
           alert(response.message)
       }
    })
    
    
    }
