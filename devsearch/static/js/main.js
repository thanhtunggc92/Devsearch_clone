

// Get value from id and class
let searchForm = document.getElementById('searchForm')
let pagelinks = document.getElementsByClassName('page-link')
// ensure searchform exits
if(searchForm){for (let i =0 ; i < pagelinks.length ; i++){
    pagelinks[i].addEventListener('click',function(e){
        e.preventDefault()
        let page = this.dataset.page
        searchForm.innerHTML += `<input value=${page} name=page hidden/>`
        searchForm.submit()
    })
}
}
