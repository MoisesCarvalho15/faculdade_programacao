// Criando um array
var frutas = ['Laranja', 'Uva', 'Pera']

// Imprimindo o conteúdo do Array utilizando o for
for (var i = 0; i < frutas.length; i++) {
    console.log('Nome da fruta: ' + frutas[i])
}

console.log();

// Imprimindo o conteúdo do Array utilizando o for in
for (var fruta in frutas) {
    console.log('Nome da fruta: ' + frutas[fruta])
}
