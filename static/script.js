// Optional: lightweight client-side help (e.g., prevent empty/NaN submissions)
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (!form) return;
  
    form.addEventListener("submit", (e) => {
      const nums = [...form.querySelectorAll('input[type="number"]')].map(i => parseFloat(i.value));
      if (nums.some(v => Number.isNaN(v))) {
        e.preventDefault();
        alert("Please fill all values correctly.");
      }
    });
  });
  