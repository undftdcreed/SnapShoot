$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  

 // Get the theme switcher input elements
const themeInputs = document.querySelectorAll('input[name="themes"]');

// Handle theme change
themeInputs.forEach((input) => {
  input.addEventListener('change', () => {
    if (input.checked) {
      const selectedTheme = input.id;
      document.documentElement.className = selectedTheme + '-theme';
    }
  });
});
