

const galleryImages = document.querySelectorAll(".gallery-grid img");
const lightboxOverlay = document.getElementById("lightboxOverlay");
const lightboxImg = lightboxOverlay.querySelector("img");

galleryImages.forEach((img) => {
    img.addEventListener("click", () => {
        lightboxImg.src = img.src;
        lightboxOverlay.style.display = "flex";
        document.body.style.overflow = "hidden";
    });
});

lightboxOverlay.addEventListener("click", () => {
    lightboxOverlay.style.display = "none";
    document.body.style.overflow = "";
});

(() => {
    "use strict";
    const form = document.getElementById("contactForm");
    form.addEventListener("submit", (event) => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add("was-validated");
    });
})();
