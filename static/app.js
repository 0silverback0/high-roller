const $modalBtn = $('.modalbtn')
const $filter = $('.modal')
const $addTocart = $('.add-to-cart')
const $cart = $('.test')

$modalBtn.click( e => {
    $filter.modal('show')
    console.log($modalBtn)
})

$addTocart.click( e => {
    e.preventDefault()
    // alert('here')
    $cart.addClass('cart')
    
    setTimeout(() => {
        $cart.removeClass('cart')
        console.log('here')
    }, 1100);

})