const btn = document.querySelectorAll(".navbar-toggler")[0]
let nav = document.getElementById("navbarSupportedContent")
let header = document.querySelectorAll(".navbar-area")[0]
acc = document.querySelectorAll(".accordion-header")

btn.addEventListener("click", function(){
  if (nav.style.display === "block"){
    nav.style.display = "none"
  }else{
    nav.style.display = "block"
  }
})

document.addEventListener('scroll', () => {
  var scroll_position = window.scrollY;
if (scroll_position > 50) {
    header.classList.remove('header-bg-color-transparent');
    header.classList.add('header-bg-color-white');
} else {
    header.classList.remove('header-bg-color-white');
    header.classList.add('header-bg-color-transparent');
}
});


function download(){
  let a = document.createElement('a')
  a.setAttribute('download',"")
  a.href = "https://github.com/emace04/cocoonner/cocooneer.apk"
  document.body.append(a)
  a.click()
  a.remove()
}

  
