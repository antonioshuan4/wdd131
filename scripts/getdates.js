const year = new Date().getFullYear();
document.getElementById("currentYear").textContent = year;

const lastModified = document.lastModified;
document.getElementById("lastModified").textContent = "Last Modification: " + lastModified;