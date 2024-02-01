// webapp/static/webapp/common.js

document.addEventListener("DOMContentLoaded", function() {
    const storedMode = localStorage.getItem("mode");
    let isDarkMode = storedMode === "dark";

    applyStyles(isDarkMode);
});

function changeColor() {
    const storedMode = localStorage.getItem("mode");
    let isDarkMode = storedMode === "dark";

    applyStyles(isDarkMode);

    // Toggle the dark mode flag
    isDarkMode = !isDarkMode;

    // Store the current mode preference in localStorage
    localStorage.setItem("mode", isDarkMode ? "dark" : "light");
}

function applyStyles(isDarkMode) {
    const body = document.body;
    const header = document.querySelector('header');
    const main = document.querySelector('main');
    const button = document.getElementById('toggleButton');
    const links = document.querySelectorAll('a'); // Assuming your links are anchor tags

    if (isDarkMode) {
        setDarkModeStyles(body, header, main, links);
        button.innerText = 'Light Mode';
    } else {
        setLightModeStyles(body, header, main, links);
        button.innerText = 'Dark Mode';
    }
}

function setLightModeStyles(body, header, main, links) {
    // ... (same as before)
}

function setDarkModeStyles(body, header, main, links) {
    // ... (same as before)
}
