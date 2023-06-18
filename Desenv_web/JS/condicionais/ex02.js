var c = 5;
var d = -1;

console.log('If com duas condições, onde ambas precisam ser verdadeiras');

if (c > d && d > 0){
    console.log('"C" é MAIOR que "D" e "D" é um número positivo!');
} else if (c > d && d <= 0){
    console.log('"C" é MAIOR que "D" e "D" NÃO é um número positivo!');
}

console.log('\nIf com duas condições, onde pelo menos uma condição precisa ser verdadeira.');

if (c < d || d > 0){
    console.log('"C" é MENOR que "D" OU "D" é um número positivo!');
} else if (c < d || d < 0){
    console.log('"C" é MENOR que "D" OU "D" NÃO é um número positivo!');
}