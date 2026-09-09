document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("htmx:afterRequest", (event) => {
        if (!event.detail.successful) return;

        const commentForm = event.target.closest(".blog-comments form");
        commentForm?.reset();
    });
});