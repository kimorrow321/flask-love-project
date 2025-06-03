window.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("bgAudio");

    if (!localStorage.getItem("musicPlayed")) {
        audio.play().then(() => {
            localStorage.setItem("musicPlayed", "true");
        }).catch(() => {
            showPlayButton();
        });
    } else {
        audio.autoplay = false;
        // Autoplay dimatikan untuk reload berikutnya, tapi tetap play manual
    }

    function showPlayButton() {
        const btn = document.createElement("button");
        btn.innerText = "play musik nya disini ya be 🎵";
        btn.style.position = "fixed";
        btn.style.top = "20px";
        btn.style.right = "20px";
        btn.style.zIndex = "9999";
        btn.style.padding = "10px";
        btn.style.fontSize = "16px";
        btn.style.borderRadius = "10px";
        btn.style.background = "white";
        btn.style.color = "#333";
        btn.onclick = () => {
            audio.play();
            btn.remove();
            localStorage.setItem("musicPlayed", "true");
        };
        document.body.appendChild(btn);
    }

    // Transisi halaman dan suara flip
    const flip = document.getElementById("flipSound");
    document.querySelectorAll(".nav-form").forEach(form => {
        form.addEventListener("submit", e => {
            e.preventDefault();
            document.querySelector(".page-container").classList.add("fade-out");
            if (flip) flip.play();
            setTimeout(() => form.submit(), 600);
        });
    });
});