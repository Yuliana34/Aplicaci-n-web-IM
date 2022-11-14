
const btn_sidebar = document.getElementById("sidebarCollapse");
const sidebar = document.getElementById("sidebar");

btn_sidebar.addEventListener("click", () => {
  sidebar.classList.toggle("active")
});  
