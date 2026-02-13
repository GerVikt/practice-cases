
let value = 0;
const result = document.getElementById("result");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");
const message = document.getElementById("message");

function update() {
  result.textContent = value;
  if (value > 0) result.style.background = "yellow";
  else if (value < 0) result.style.background = "green";
  else result.style.background = "red";

  plus.disabled = value >= 10;
  minus.disabled = value <= -10;
  message.textContent = (value === 10 || value === -10) ? "Вы достигли экстремального значения" : "";
}

plus.onclick = () => { value++; update(); };
minus.onclick = () => { value--; update(); };
update();
