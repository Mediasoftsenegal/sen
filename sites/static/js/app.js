let next = document.querySelector(".next")
let prev = document.querySelector(".prev")

 next.addEventListener('click',function(){
     let items = document.querySelectorAll(".item")
     document.querySelector(".slidesen").appendChild(items[0])
 })

 prev.addEventListener('click',function(){
     let items = document.querySelectorAll(".item")
     document.querySelector(".slidesen").prepend(items[items.length - 1])
})

function slideNext() {
    let items = document.querySelectorAll(".item")
    document.querySelector(".slidesen").appendChild(items[0])
}

function slidePrev() {
    let items = document.querySelectorAll(".item")
    document.querySelector(".slidesen").prepend(items[items.length - 1])
}

next.addEventListener('click', slideNext)
prev.addEventListener('click', slidePrev)

// Automatiser le carrousel toutes les 3 secondes
setInterval(slideNext, 5000)