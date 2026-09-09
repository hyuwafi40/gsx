document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("blogNavToggle");
    const navLinks = document.getElementById("blogNavLinks");

    if (toggle && navLinks) {
        const icon = toggle.querySelector("i");

        const closeNavigation = (restoreFocus = false) => {
            navLinks.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
            toggle.setAttribute("aria-label", "Buka navigasi");
            icon?.classList.replace("fa-xmark", "fa-bars");
            if (restoreFocus) toggle.focus();
        };

        toggle.addEventListener("click", () => {
            const isOpen = navLinks.classList.toggle("open");
            toggle.setAttribute("aria-expanded", String(isOpen));
            toggle.setAttribute("aria-label", isOpen ? "Tutup navigasi" : "Buka navigasi");
            icon?.classList.toggle("fa-bars", !isOpen);
            icon?.classList.toggle("fa-xmark", isOpen);
        });

        navLinks.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => closeNavigation());
        });

        navLinks.addEventListener("keydown", (event) => {
            if (event.key !== "Escape") return;
            closeNavigation(true);
        });

        document.addEventListener("click", (event) => {
            if (!navLinks.classList.contains("open")) return;
            if (navLinks.contains(event.target) || toggle.contains(event.target)) return;
            closeNavigation();
        });

        window.addEventListener("resize", () => {
            if (window.matchMedia("(min-width: 1024px)").matches) {
                closeNavigation();
            }
        });
    }

    const cards = document.querySelectorAll(".blog-card");
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (!entry.isIntersecting) return;
                setTimeout(() => entry.target.classList.add("visible"), index * 100);
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.05 });
        cards.forEach((card) => observer.observe(card));
    } else {
        cards.forEach((card) => card.classList.add("visible"));
    }

    const carousel = document.getElementById("blogCarousel");
    if (carousel) {
        const track = carousel.querySelector(".blog-carousel-track");
        const slides = carousel.querySelectorAll(".blog-carousel-slide");
        const prevButton = document.getElementById("carouselPrev");
        const nextButton = document.getElementById("carouselNext");
        const dotsContainer = document.getElementById("carouselDots");
        const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        let currentIndex = 0;
        let autoPlayInterval;

        const updateCarousel = () => {
            track.style.transform = `translateX(-${currentIndex * 100}%)`;
            slides.forEach((slide, index) => {
                const isCurrent = index === currentIndex;
                slide.setAttribute("aria-hidden", String(!isCurrent));
                slide.inert = !isCurrent;
            });
            const dots = dotsContainer?.querySelectorAll(".blog-carousel-dot") || [];
            dots.forEach((dot, index) => {
                const isCurrent = index === currentIndex;
                dot.classList.toggle("active", isCurrent);
                dot.setAttribute("aria-current", String(isCurrent));
            });
        };

        const goToSlide = (index) => {
            currentIndex = (index + slides.length) % slides.length;
            updateCarousel();
        };

        const stopAutoPlay = () => clearInterval(autoPlayInterval);

        const startAutoPlay = () => {
            if (prefersReducedMotion || slides.length < 2) return;
            stopAutoPlay();
            autoPlayInterval = setInterval(() => goToSlide(currentIndex + 1), 5000);
        };

        const resetAutoPlay = () => {
            stopAutoPlay();
            startAutoPlay();
        };

        const createDots = () => {
            if (!dotsContainer) return;
            dotsContainer.innerHTML = "";
            if (slides.length < 2) {
                dotsContainer.hidden = true;
                if (prevButton) prevButton.hidden = true;
                if (nextButton) nextButton.hidden = true;
                return;
            }
            slides.forEach((_, index) => {
                const dot = document.createElement("button");
                dot.type = "button";
                dot.className = "blog-carousel-dot";
                dot.setAttribute("aria-label", `Slide ${index + 1}`);
                dot.addEventListener("click", () => {
                    goToSlide(index);
                    resetAutoPlay();
                });
                dotsContainer.appendChild(dot);
            });
        };

        prevButton?.addEventListener("click", () => {
            goToSlide(currentIndex - 1);
            resetAutoPlay();
        });

        nextButton?.addEventListener("click", () => {
            goToSlide(currentIndex + 1);
            resetAutoPlay();
        });

        carousel.addEventListener("keydown", (event) => {
            if (event.key === "ArrowLeft") {
                event.preventDefault();
                goToSlide(currentIndex - 1);
                resetAutoPlay();
            } else if (event.key === "ArrowRight") {
                event.preventDefault();
                goToSlide(currentIndex + 1);
                resetAutoPlay();
            }
        });

        let startX = 0;
        track.addEventListener("touchstart", (event) => {
            startX = event.touches[0].clientX;
        }, { passive: true });

        track.addEventListener("touchend", (event) => {
            const distance = startX - event.changedTouches[0].clientX;
            if (Math.abs(distance) <= 50) return;
            goToSlide(currentIndex + (distance > 0 ? 1 : -1));
            resetAutoPlay();
        }, { passive: true });

        carousel.addEventListener("mouseenter", stopAutoPlay);
        carousel.addEventListener("mouseleave", startAutoPlay);
        carousel.addEventListener("focusin", stopAutoPlay);
        carousel.addEventListener("focusout", (event) => {
            if (!carousel.contains(event.relatedTarget)) startAutoPlay();
        });

        createDots();
        updateCarousel();
        startAutoPlay();
    }
});

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

document.body.addEventListener("showToast", (event) => {
    const detail = event.detail || {};
    showToast(detail.message || "Action performed", detail.type || "info");
});