function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

document.getElementById("modal-btn").addEventListener("click", function () {
    document.getElementById("modal").style.display = "block";
});

// Закрытие модального окна при клике на крестик
document.getElementsByClassName("close")[0].addEventListener("click", function () {
    document.getElementById("modal").style.display = "none";
});

// Закрытие модального окна при клике вне его области
window.addEventListener("click", function (event) {
    if (event.target == document.getElementById("modal")) {
        document.getElementById("modal").style.display = "none";
    }
});