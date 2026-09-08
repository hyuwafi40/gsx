function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.body.addEventListener('htmx:configRequest', (event) => {
    const csrfToken = getCookie('csrftoken');
    if (csrfToken) {
        event.detail.headers['X-CSRFToken'] = csrfToken;
    }
});

document.body.addEventListener('showToast', (e) => {
    const message = e.detail.message || 'Action performed';
    const type = e.detail.type || 'info';
    if (typeof showToast === 'function') {
        showToast(message, type);
    }
});
