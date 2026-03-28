document.getElementById("currentyear").textContent = new Date().getFullYear();
document.getElementById("lastModified").textContent = document.lastModified;

// Datos estáticos para el cálculo
const temp = 8; // °C
const windSpeed = 10; // km/h

// Requisito: Función para calcular sensación térmica
function calculateWindChill(t, v) {
    // Fórmula para Celsius: 13.12 + 0.6215t - 11.37v^0.16 + 0.3965tv^0.16
    return (13.12 + (0.6215 * t) - (11.37 * Math.pow(v, 0.16)) + (0.3965 * t * Math.pow(v, 0.16))).toFixed(1);
}

const windChillElement = document.getElementById("windchill");

// Requisito: Solo llamar si cumple las condiciones (<= 10°C y > 4.8 km/h)
if (temp <= 10 && windSpeed > 4.8) {
    windChillElement.textContent = calculateWindChill(temp, windSpeed) + " °C";
} else {
    windChillElement.textContent = "N/A";
}