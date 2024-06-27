function toggleTheme() {
    const themeStyle = document.getElementById("theme_style");
    const lightIcon = document.getElementById("light_icon");
    const darkIcon = document.getElementById("dark_icon");
    if (themeStyle.getAttribute("href") === url_for_light) {
        themeStyle.setAttribute('href', url_for_dark);
        lightIcon.style.display = "none";
        darkIcon.style.display = "block";
        localStorage.setItem("theme", "dark");
    } else {
        themeStyle.setAttribute('href', url_for_light);
        lightIcon.style.display = "block";
        darkIcon.style.display = "none";
        localStorage.setItem("theme", "light");
    }
}

window.onload = function() {
    const theme = localStorage.getItem("theme");
    const themeStyle = document.getElementById("theme_style");
    const lightIcon = document.getElementById("light_icon");
    const darkIcon = document.getElementById("dark_icon");
    if (theme === "dark") {
        themeStyle.setAttribute('href', url_for_dark);
        lightIcon.style.display = "none";
        darkIcon.style.display = "block";
    } else {
        themeStyle.setAttribute('href', url_for_light);
        lightIcon.style.display = "block";
        darkIcon.style.display = "none";
    }
}
