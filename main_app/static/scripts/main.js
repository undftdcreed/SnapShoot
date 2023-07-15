
  

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
  
