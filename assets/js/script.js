// intro slider
let introSlideIndex = 1

const plusIntroSlides = (n) => {
    showIntroSlides(introSlideIndex += n)
}

const showIntroSlides = (n) => {
    var introSlides = document.getElementsByClassName('intro-box')
    if (n > introSlides.length) {
        introSlideIndex = 1
    }
    if (n < 1) {
        introSlideIndex = introSlides.length
    }
    for (let i = 0; i < introSlides.length; i++) {
        introSlides[i].classList = 'col-md-12 intro-box fade'
    }
    introSlides[introSlideIndex - 1].classList = 'col-md-12 intro-box fade show'
}

showIntroSlides(introSlideIndex)

// get csrf-token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
