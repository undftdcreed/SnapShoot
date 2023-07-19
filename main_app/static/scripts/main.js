
  

  $(document).ready(function() {
    $(".navbar-burger").click(function() {
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");
    });
  
    // Handle theme change
    $('input[name="themes"]').change(function() {
      if (this.checked) {
        const selectedTheme = this.id;
        document.documentElement.className = selectedTheme + "-theme";
      }
    });
  });

  //theme change
  document.addEventListener('DOMContentLoaded', function () {
    const themeSwitcher = document.querySelector('.theme-switcher');
  
    if (themeSwitcher) {
      const body = document.querySelector('body');
  
      themeSwitcher.addEventListener('change', function () {
        if (this.checked) {
          body.className = this.id + '-theme';
        }
      });
    }
  });
  
