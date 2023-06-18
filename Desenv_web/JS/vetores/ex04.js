dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira'];
console.log(dias_semana);

// inserindo elementos com o splice
// para inserir utilizamos o número 0 no segundo argumento.
dias_semana.splice(3, 0, 'Quarta-feira');
console.log(dias_semana);

// substituindo um elemento
// para isso utilizamos o número 1 no segundo argumento.
dias_semana.splice(0, 1, 'Item Modificado');
console.log(dias_semana);

// removendo um elemento
dias_semana.splice(0, 1);
console.log(dias_semana);