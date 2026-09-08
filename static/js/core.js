function showToast(message, type = "success") {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const toast = document.createElement("div");
    toast.className = "glass toast";

    let icon = "fa-circle-check";
    let iconColor = "var(--success)";

    if (type === "info") {
        icon = "fa-circle-info";
        iconColor = "var(--primary)";
    } else if (type === "danger") {
        icon = "fa-circle-exclamation";
        iconColor = "var(--danger)";
    }

    const iconElement = document.createElement("i");
    iconElement.className = `fa-solid ${icon}`;
    iconElement.style.color = iconColor;
    iconElement.style.fontSize = "18px";

    const textSpan = document.createElement("span");
    textSpan.style.fontWeight = "500";
    textSpan.style.fontSize = "13px";
    textSpan.style.color = "var(--text-dark)";
    textSpan.textContent = message;

    toast.appendChild(iconElement);
    toast.appendChild(textSpan);
    container.appendChild(toast);

    setTimeout(() => {
        if (toast.parentNode) {
            toast.remove();
        }
    }, 4000);
}

document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, idx) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add("visible");
                }, idx * 120);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.05 });

    cards.forEach(card => observer.observe(card));

    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    const btnToggle = document.getElementById("btnToggle");

    if (btnToggle) {
        btnToggle.addEventListener("click", () => {
            sidebar.classList.add("active");
            overlay.classList.add("active");
        });
    }

    document.addEventListener("click", (e) => {
        const actionIcon = e.target.closest(".action-icon");
        if (actionIcon) {
            const message = actionIcon.dataset.toastMessage;
            const type = actionIcon.dataset.toastType || "info";
            if (message) {
                showToast(message, type);
            }
        }

        const closeButton = e.target.closest(".modal-close");
        if (closeButton) {
            const modal = closeButton.closest(".modal");
            if (modal) modal.classList.remove("active");
            if (overlay) overlay.classList.remove("active");
            return;
        }

        const deleteBtn = e.target.closest(".delete-btn");
        if (deleteBtn) {
            e.preventDefault();
            const url = deleteBtn.dataset.deleteUrl;
            const name = deleteBtn.dataset.name;
            const modal = document.getElementById("deleteModal");
            const form = document.getElementById("deleteForm");
            const nameSpan = document.getElementById("deleteObjectName");
            if (modal && form && nameSpan) {
                form.action = url;
                nameSpan.textContent = name;
                modal.classList.add("active");
                if (overlay) overlay.classList.add("active");
            }
            return;
        }

        if (e.target === overlay) {
            const activeModals = document.querySelectorAll(".modal.active");
            activeModals.forEach(m => m.classList.remove("active"));
            if (overlay) overlay.classList.remove("active");
        }
    });

    document.body.addEventListener("htmx:afterSwap", () => {
        const modal = document.querySelector(".modal.active");
        if (modal && overlay) {
            overlay.classList.add("active");
        }
    });
});