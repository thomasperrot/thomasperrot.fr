function appear(elt) {
    var s = elt.style,
        result = s.opacity = parseFloat(s.opacity) + 0.05;
    if (result <= 1) {
        setTimeout(appear, 50, elt);
    }
}

function animate() {
    var myList = document.getElementsByClassName('list-item');
    var timeWaiting = 0;
    for (var i = 0; i < myList.length; i++) {
        var s = myList[i].style;
        s.opacity = 0;
        timeWaiting += 1000;
        setTimeout(appear, timeWaiting, myList[i]);
    }
}