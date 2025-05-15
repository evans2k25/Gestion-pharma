document.querySelector(".jsFilter").addEventListener("click", function () {
  document.querySelector(".filter-menu").classList.toggle("active");
});

document.querySelector(".grid").addEventListener("click", function () {
  document.querySelector(".list").classList.remove("active");
  document.querySelector(".grid").classList.add("active");
  document.querySelector(".products-area-wrapper").classList.add("gridView");
  document
    .querySelector(".products-area-wrapper")
    .classList.remove("tableView");
});

document.querySelector(".list").addEventListener("click", function () {
  document.querySelector(".list").classList.add("active");
  document.querySelector(".grid").classList.remove("active");
  document.querySelector(".products-area-wrapper").classList.remove("gridView");
  document.querySelector(".products-area-wrapper").classList.add("tableView");
});

var modeSwitch = document.querySelector(".mode-switch");
modeSwitch.addEventListener("click", function () {
  document.documentElement.classList.toggle("light");
  modeSwitch.classList.toggle("active");
});

document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const productId = this.getAttribute("data-id");

      if (confirm("Voulez-vous vraiment supprimer ce produit ?")) {
        fetch(`/delete-product/${productId}/`, {
          method: "DELETE",
          headers: {
            "X-CSRFToken": "{{ csrf_token }}", // Nécessaire pour Django
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              // Supprimer le produit de la vue
              this.parentElement.parentElement.remove();
            } else {
              alert("Erreur lors de la suppression.");
            }
          })
          .catch((error) => console.log(error));
      }
    });
  });
});
