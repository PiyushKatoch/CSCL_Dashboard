(function () {
    var preload = document.getElementById("preload");
    var loading = 0;
    var id = setInterval(frame,15);

    function frame() {
        if (loading == 100) {
            clearInterval(id);
            window.open("home", "_self");
        } else {
            loading = loading + 1;
            if (loading == 99) {
                preload.style.animation = "fadeout 1s easeout forwards";
            }
        }
    }
})();