document.addEventListener('DOMContentLoaded', () => {
  const elements = [
    document.getElementById('value0'),
    document.getElementById('value1'),
    document.getElementById('value2'),
    document.getElementById('value3')
  ];

  fetch('https://raw.githubusercontent.com/v4run75/Utility-Code/master/value.txt')
    .then(response => response.text())
    .then(value => {
      const values = value.trim().split('\n');
      elements.forEach((element, index) => {
        if (element && values[index]) {
          element.textContent = values[index];
        }
      });
    })
    .catch(error => console.error(error));
});