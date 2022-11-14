const signUp = document.getElementById('sign-up'),signIn = document.getElementById('sign-in'),
loginIn = document.getElementById('loginInForm'),loginUp = document.getElementById('loginUpForm');

signUp.addEventListener('click', ()=>{
    loginIn.classList.remove('block')
    loginUp.classList.remove('none')

    loginIn.classList.toggle('none')
    loginUp.classList.toggle('block')
})

signIn.addEventListener('click', ()=>{
    loginIn.classList.remove('none')
    loginUp.classList.remove('block')

    loginIn.classList.toggle('block')
    loginUp.classList.toggle('none')
})

loginIn.addEventListener('submit', (e)=>{
    e.preventDefault();
    const form = new FormData();
    let username = document.getElementById("lusername").value;
    username = username.replace(/\s/g, '');
    let password = document.getElementById("lpassword").value;
    form.append("username", username);
    form.append("password", password);
    fetch("/login",{
        method: "POST",
        body: form
    }).then(
        res => res.json()
    ).then(res => {
        if (res.status === "success") {
            Swal.fire({
                icon: 'info',
                text: 'PEXT Welcomes You!',
            }).then( _ => {
                window.location.replace("/dash");
            })                        
        } else{
            Swal.fire({
                icon: 'error',
                text: 'Account does not exist!',
            });
        }
    });        
})

loginUp.addEventListener('submit', (e)=>{
    e.preventDefault();
    const form = new FormData();
    let username = document.getElementById("susername").value;
    username = username.replace(/\s/g, '');
    let email = document.getElementById("semail").value;
    let password = document.getElementById("spassword").value;
    form.append("username", username);
    form.append("email", email);
    form.append("password", password);
    if (/^[a-z0-9_.]+$/.test(username)) {
        if (/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[a-zA-Z!#$%&?@ "])[a-zA-Z0-9!#$%&@?]{8,20}$/.test(password)) {
            signUp.style.display = "none";
            fetch("/signup",{
                method: "POST",
                body: form
            }).then(
                res => res.json()
            ).then(res => {
                if (res.status === "success") {
                    Swal.fire({
                        icon: 'success',
                        text: 'Account Created Successfully!',
                    }).then( _ =>{
                        loginUp.reset();                        
                    })                                         
                } else{
                    Swal.fire({
                        icon: 'error',
                        text: 'Account already exist!',
                    });
                }
            });
        } else {
            Swal.fire(
                "Minimum 8 characters\nMaximum 20 characters \nAt least one uppercase character\nAt least one lowercase character\nAt least one digit\nAt least one special character\n"
            );
        }            
    } else{
        Swal.fire({
            icon: 'error',
            text: 'Username is invalid!',
        });
    }
})

