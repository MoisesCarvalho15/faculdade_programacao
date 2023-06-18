dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira'];

console.log(dias_semana);
console.log('Números de elementos do array: ' + dias_semana.length);

// removendo elementos do array utilizando delete
// o elemento se torna undefined e permanece no tamanho do array
delete dias_semana[0];
console.log(dias_semana);
console.log('Números de elementos do array: ' + dias_semana.length);

console.log();

var numeros = [1, 2, 3, 4, 5];
console.log(numeros)

// removendo um elemento no final do array
numeros.pop();
console.log(numeros);

// removendo o primeiro elemento do array
numeros.shift();
console.log(numeros);