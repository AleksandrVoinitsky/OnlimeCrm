document.querySelectorAll("[data-password-toggle]").forEach((button) => {
  button.addEventListener("click", () => {
    const input = button.closest(".password-field").querySelector("input");
    const isPassword = input.type === "password";
    input.type = isPassword ? "text" : "password";
    button.setAttribute("aria-pressed", String(isPassword));
    button.setAttribute("aria-label", isPassword ? "Скрыть пароль" : "Показать пароль");
  });
});

const products = Array.from(document.querySelectorAll("[data-product]"));
const catalogSearch = document.querySelector("[data-catalog-search]");
const catalogResult = document.querySelector("[data-catalog-result]");
let selectedCategory = "all";

function filterProducts() {
  const query = catalogSearch?.value.trim().toLowerCase() ?? "";
  let visibleCount = 0;

  products.forEach((product) => {
    const matchesCategory = selectedCategory === "all" || product.dataset.category === selectedCategory;
    const matchesQuery = product.dataset.productName.toLowerCase().includes(query);
    const visible = matchesCategory && matchesQuery;
    product.hidden = !visible;
    visibleCount += Number(visible);
  });

  if (catalogResult) {
    catalogResult.textContent = `${visibleCount} ${visibleCount === 1 ? "продукт" : "продукта"}`;
  }
}

document.querySelectorAll("[data-filter]").forEach((filter) => {
  filter.addEventListener("click", () => {
    selectedCategory = filter.dataset.filter;
    document.querySelectorAll("[data-filter]").forEach((item) => item.classList.toggle("is-active", item === filter));
    filterProducts();
  });
});

catalogSearch?.addEventListener("input", filterProducts);

let cartCount = 0;
document.querySelectorAll("[data-add-to-cart]").forEach((button) => {
  button.addEventListener("click", () => {
    cartCount += 1;
    document.querySelectorAll("[data-cart-count]").forEach((count) => {
      count.textContent = String(cartCount);
    });
    button.classList.add("is-added");
    button.innerHTML = 'Добавлено <span aria-hidden="true">✓</span>';
  });
});
