document.addEventListener("DOMContentLoaded", () => {
    const commentForm = document.querySelector(".blog-comments form");
    if (commentForm) {
        commentForm.addEventListener("htmx:afterRequest", (event) => {
            if (event.detail.successful) {
                commentForm.reset();
            }
        });
    }
});