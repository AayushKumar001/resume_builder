const date = new Date();

document.querySelector('.year').innerHTML = date.getFullYear();


window.onload = onPageLoad();
function onPageLoad() {

    var url = window.location.href;
    if (url.includes('experience')){
        check('ex')
    }
    else if(url.includes('education')){
        check('ex')
        check('ed')
    }
    else if(url.includes('skills')){
        check('ex')
        check('ed')
        check('sk')
    }
    else if(url.includes('summary')){
        check('ex')
        check('ed')
        check('sk')
        check('su')
        check('pr')
    }    
    else if(url.includes('project')){
        check('ex')
        check('ed')
        check('sk')
        check('pr')
    }
}
function check(id){
    document.getElementById(id).disabled=false
    document.getElementById(id).checked = true
}