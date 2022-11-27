let $modalBtn = $('.modalbtn')

let $filter = $('.modal')

$modalBtn.click( e => {
    $filter.modal('show')
    console.log($modalBtn)
})