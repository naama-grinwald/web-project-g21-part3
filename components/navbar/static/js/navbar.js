function navbar() {

  var navbar = document.getElementById("navbar");
  var sticky = navbar.offsetTop;

  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}


/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function navbar_res() {
  var x = document.getElementById("navbar");
  console.log(x)
  if (x.className == "nav sticky" || x.className == "nav") {
      x.classList+= ' responsive';
    }
  else {
              x.classList = "nav sticky"
      }
   console.log(x)
}
