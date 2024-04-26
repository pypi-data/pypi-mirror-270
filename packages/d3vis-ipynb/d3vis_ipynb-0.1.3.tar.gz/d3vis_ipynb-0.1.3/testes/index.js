const valueLabel = document.getElementById("value");
const resultLabel = document.getElementById("result");

const minSlider = document.getElementById("fromSlider");
const maxSlider = document.getElementById("toSlider");

let numbersArray = [];

function generateRandomNumbersArray(length, min, max) {
  numbersArray = Array.from(
    { length },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
}

function updateLabels() {
  valueLabel.textContent = minSlider.value + " - " + maxSlider.value;
  updateResult();
}

function updateResult() {
  const minValue = parseInt(minSlider.value);
  const maxValue = parseInt(maxSlider.value);

  const selectedRange = numbersArray.filter(
    (num) => num >= minValue && num <= maxValue
  );

  resultLabel.textContent = selectedRange.join(", ");
}

minSlider.addEventListener("input", () => {
  if (parseInt(minSlider.value) > parseInt(maxSlider.value)) {
    minSlider.value = maxSlider.value;
  }
  updateLabels();
});

maxSlider.addEventListener("input", () => {
  if (parseInt(maxSlider.value) < parseInt(minSlider.value)) {
    maxSlider.value = minSlider.value;
  }
  updateLabels();
});

minSlider.addEventListener("click", () => {
    minSlider.classList.add("top_slider")
    maxSlider.classList.remove("top_slider")
});

maxSlider.addEventListener("click", () => {
    maxSlider.classList.add("top_slider")
    minSlider.classList.remove("top_slider")
});

generateRandomNumbersArray(50, 1, 100);
updateLabels();
