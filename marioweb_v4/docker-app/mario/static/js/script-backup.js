document.addEventListener('DOMContentLoaded', () => {
  const element = document.getElementById('value0');
  const element1 = document.getElementById('value1');
  const element2 = document.getElementById('value2');
  const element3 = document.getElementById('value3');

  fetch('https://raw.githubusercontent.com/v4run75/Utility-Code/master/value.txt')
    .then(response => response.text())
    .then(value => {
      element.textContent = value;
      element1.textContent = value;
      element2.textContent = value;
      element3.textContent = value;
    })
    .catch(error => console.error(error));
});

