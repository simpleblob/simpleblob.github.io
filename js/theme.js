// Light/dark toggle. Pages follow the system setting until the reader picks
// one; the choice is kept in localStorage. Loaded in <head> so a saved theme
// applies before first paint. Without JavaScript the button stays hidden.
(() => {
  const KEY = "theme";
  const root = document.documentElement;
  try {
    const saved = localStorage.getItem(KEY);
    if (saved === "light" || saved === "dark") root.dataset.theme = saved;
  } catch {}

  const isDark = () =>
    (root.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")) === "dark";

  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;
    const sync = () => button.setAttribute("aria-pressed", String(isDark()));
    button.addEventListener("click", () => {
      root.dataset.theme = isDark() ? "light" : "dark";
      try { localStorage.setItem(KEY, root.dataset.theme); } catch {}
      sync();
    });
    matchMedia("(prefers-color-scheme: dark)").addEventListener("change", sync);
    sync();
    button.hidden = false;
  });
})();
