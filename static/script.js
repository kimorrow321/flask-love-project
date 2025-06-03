window.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById("bgAudio");
    const flip = document.getElementById("flipSound");
    const lastTime = sessionStorage.getItem("audioTime");
    if (lastTime !== null) audio.currentTime = parseFloat(lastTime);

    audio.play().catch(() => {
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
        };
        document.body.appendChild(btn);
    });

    document.querySelectorAll(".nav-form").forEach(form => {
        form.addEventListener("submit", e => {
            e.preventDefault();
            document.querySelector(".page-container").classList.add("fade-out");
            flip.play();
            setTimeout(() => form.submit(), 600);
        });
    });
});
