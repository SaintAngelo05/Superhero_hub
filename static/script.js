const registerDiv = document.getElementById("sRegister")
const loginDiv = document.getElementById("sLogin")

//The follwing code is used to show a specific element (div) on the page
function ShowElement(element){

    //Getting the DOM object
    let domProperty = document.querySelector(element);
    //domProperty.style.opacity = opacity;
    domProperty.style.visibility = "visible";
    domProperty.style.opacity = 1;
}

document.getElementById('sRegister').addEventListener('click', function() {
  document.getElementById('login').classList.add('hidden');
  document.getElementById('register').classList.remove('hidden');
});

document.getElementById('sLogin').addEventListener('click', function() {
  document.getElementById('register').classList.add('hidden');
  document.getElementById('login').classList.remove('hidden');
});



//The follwing code is used to hide a specific element (div) on the page
function HideElement(element){

    //Getting the object for the element
    let domProperty = document.querySelector(element);
    
    domProperty.style.visibility = "hidden";
    domProperty.style.opacity = 0;
}

//Using callback functions and an event listener (click) to execute "ShowElement" and "HideElement" functions
registerDiv.addEventListener("click",()=>{
    HideElement("#login");
    ShowElement("#register");
});

loginDiv.addEventListener("click",()=>{
    HideElement("#register");
    ShowElement("#login");
});


