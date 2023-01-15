function fullscreen(){
    elem = document.getElementsByTagName("body")[0];
    
    if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement){
        if(elem.requestFullscreen){
            elem.requestFullscreen();
        } else if(elem.msRequestFullscreen){
            elem.msRequestFullscreen();
        } else if(elem.mozRequestFullScreen){
            elem.mozRequestFullScreen();
        } else if(elem.webkitRequestFullscreen){
            elem.webkitRequestFullscreen(elem.ALLOW_KEYBOARD_INPUT);
        }
    } else {
        if(document.exitFullscreen){
            document.exitFullscreen();
        } else if(document.msExitFullscreen){
            document.msExitFullscreen();
        } else if(document.mozCancelFullScreen){
            document.mozCancelFullScreen();
        } else if(document.webkitExitFullscreen){
            document.webkitExitFullscreen();
        }
    }
}
