document.getElementById("currentyear").textContent = new Date().getFullYear();
document.getElementById("lastModified").textContent = document.lastModified;

// 📊 DATOS (tomados del HTML)
const temp = parseFloat(document.getElementById("temp").textContent);
const windSpeed = parseFloat(document.getElementById("wind").textContent);

// 🔥 FUNCIÓN (UNA SOLA LÍNEA como pide la tarea)
function calculateWindChill(t, v) {
    return (13.12 + 0.6215 * t - 11.37 * Math.pow(v, 0.16) + 0.3965 * t * Math.pow(v, 0.16)).toFixed(1);
}

// 📌 MOSTRAR RESULTADO
const windChillElement = document.getElementById("windchill");

// ✔ Condición requerida por la actividad
if (temp <= 10 && windSpeed > 4.8) {
    windChillElement.textContent = `${calculateWindChill(temp, windSpeed)} °C`;
} else {
    windChillElement.textContent = "N/A";
}