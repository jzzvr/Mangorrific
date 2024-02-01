// webapp/static/webapp/script.js

let isDarkMode = false;

function changeColor() {
    const body = document.body;
    const header = document.querySelector('header');
    const main = document.querySelector('main');
    const button = document.getElementById('toggleButton');
    const links = document.querySelectorAll('a'); // Assuming your links are anchor tags

    // Toggle between two background colors and text colors for body, header, and main
    if (isDarkMode) {
        setLightModeStyles(body, header, main, links);
        button.innerText = 'Dark Mode';
    } else {
        setDarkModeStyles(body, header, main, links);
        button.innerText = 'Light Mode';
    }

    // Toggle the dark mode flag
    isDarkMode = !isDarkMode;
}

// Function to set styles for light mode
function setLightModeStyles(body, header, main, links) {
    body.style.backgroundColor = '#fff';
    body.style.color = '#000';
    header.style.backgroundColor = '#fff';
    header.style.color = '#000';
    main.style.backgroundColor = '#fff';
    main.style.color = '#000';

    // Set text color for each link in light mode
    links.forEach(link => {
        link.style.color = '#000';
    });
}

// Function to set styles for dark mode
function setDarkModeStyles(body, header, main, links) {
    body.style.backgroundColor = '#000';
    body.style.color = '#fff';
    header.style.backgroundColor = '#121212';
    header.style.color = '#fff';
    main.style.backgroundColor = '#121212';
    main.style.color = '#fff';

    // Set text color for each link in dark mode
    links.forEach(link => {
        link.style.color = '#fff';
    });
}
