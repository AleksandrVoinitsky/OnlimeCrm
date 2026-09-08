document.querySelectorAll("[data-password-toggle]").forEach((button) => {
  button.addEventListener("click", () => {
    const input = button.closest(".password-field").querySelector("input");
    const isPassword = input.type === "password";
    input.type = isPassword ? "text" : "password";
    button.setAttribute("aria-pressed", String(isPassword));
    button.setAttribute("aria-label", isPassword ? "Скрыть пароль" : "Показать пароль");
  });
});
