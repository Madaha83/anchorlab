// Small progressive enhancements. The site works without this file.

// Plausible analytics setup (kept here so the CSP needs no 'unsafe-inline').
window.plausible = window.plausible || function () { (plausible.q = plausible.q || []).push(arguments); };
plausible.init = plausible.init || function (i) { plausible.o = i || {}; };
plausible.init();

document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", function () {
  // Mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    var setOpen = function (open) {
      nav.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    };
    toggle.addEventListener("click", function () { setOpen(!nav.classList.contains("open")); });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { setOpen(false); toggle.focus(); }
    });
  }

  // Analytics events: Apply buttons (where clicked) and partner email links
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("join.html#apply") !== -1 || href === "#apply") {
      var where = a.classList.contains("nav-cta") ? "nav" : (a.closest(".lab-hero") ? "hero" : "page");
      window.plausible("Apply CTA Click", { props: { location: where } });
    } else if (href.indexOf("mailto:") === 0 && document.body.querySelector("#ethics-h")) {
      window.plausible("Partner Contact");
    }
  });
});
