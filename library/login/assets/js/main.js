let passwordHide = document.getElementById('passwordHide');
let password = document.getElementById('password');


let count = 0

function hidePassword() {
    count += 1
    console.log(count)
    if (count == 2){
        count = 0;
    };
    (count == 1)? 
    password.setAttribute('type', 'text'): 
    password.setAttribute('type', 'password');
};