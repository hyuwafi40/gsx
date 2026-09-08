document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    const submitButton = document.getElementById("loginSubmit");

    if (form && submitButton) {
        form.addEventListener("submit", () => {
            submitButton.classList.add("is-loading");
            submitButton.disabled = true;
        });
    }
});