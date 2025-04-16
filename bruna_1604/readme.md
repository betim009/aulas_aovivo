
# Exercício de Manipulação de Objetos – Bandas de Rock 🎸

Este exercício tem como objetivo praticar conceitos básicos de **tipos de dados** e **manipulação de objetos** em JavaScript, usando uma base de dados com bandas de rock.

---

## 🎯 Objetivo

Adicionar a cada objeto do array `bandasDeRock` uma nova propriedade chamada `nota`, representando uma nota fictícia para a banda (de 0 a 10).

---

## 💡 Instruções

Você já tem o seguinte array de objetos:

```javascript
const bandasDeRock = [
    {
        nome: "Queen",
        origem: "Reino Unido",
        anoFormacao: 1970,
        hitFamoso: "Bohemian Rhapsody"
    },
    {
        nome: "Nirvana",
        origem: "Estados Unidos",
        anoFormacao: 1987,
        hitFamoso: "Smells Like Teen Spirit"
    },
    {
        nome: "The Rolling Stones",
        origem: "Reino Unido",
        anoFormacao: 1962,
        hitFamoso: "(I Can't Get No) Satisfaction"
    },
    {
        nome: "Metallica",
        origem: "Estados Unidos",
        anoFormacao: 1981,
        hitFamoso: "Enter Sandman"
    },
    {
        nome: "Legião Urbana",
        origem: "Brasil",
        anoFormacao: 1982,
        hitFamoso: "Tempo Perdido"
    },
    {
        nome: "AC/DC",
        origem: "Austrália",
        anoFormacao: 1973,
        hitFamoso: "Back in Black"
    }
];
```

---

## 📝 Tarefa

Adicione uma nova chave `nota` para **cada banda**. Exemplo:

```javascript
bandasDeRock[0].nota = 9.5;
```

Você pode escolher notas fictícias, como no exemplo abaixo:

```javascript
bandasDeRock[0].nota = 9.5; // Queen
bandasDeRock[1].nota = 9.0; // Nirvana
bandasDeRock[2].nota = 8.5; // The Rolling Stones
bandasDeRock[3].nota = 9.2; // Metallica
bandasDeRock[4].nota = 8.8; // Legião Urbana
bandasDeRock[5].nota = 9.1; // AC/DC
```

---

## ✅ Desafio Extra (Opcional)

Sem utilizar laços de repetição (sem `for`, `forEach`, `map`, etc.), adicione as notas diretamente e depois exiba o nome e a nota da primeira banda:

```javascript
console.log(bandasDeRock[0].nome + " - Nota: " + bandasDeRock[0].nota);
```

---

## 📌 Conceitos Reforçados

- Tipos de dados: `string`, `number`
- Acesso e modificação de propriedades de objetos
- Organização de dados em arrays

---

## 🧠 Dica

Você pode também usar esse array como base para novos exercícios, como ordenar por ano de formação, filtrar por país ou até gerar frases automáticas com os dados.

---

## 🎯 2 - Objetivo

Criar **uma frase descritiva** para **cada banda** usando os dados disponíveis no objeto. A frase deve seguir o seguinte formato:

> `"Queen" é uma banda do Reino Unido formada em 1970. Seu maior sucesso é "Bohemian Rhapsody".`

---

## 💡 Instruções

- Use as propriedades: `nome`, `origem`, `anoFormacao` e `hitFamoso`.
- Crie uma variável para cada frase.
- Utilize concatenação (`+`) ou template strings (`` `texto ${variavel}` ``).
- **Não utilize loops ou estruturas de repetição.**
- Crie **uma frase por banda** manualmente.

---

## 📌 Exemplo (somente a primeira banda)

```javascript
const frase1 = `"${bandasDeRock[0].nome}" é uma banda do ${bandasDeRock[0].origem} formada em ${bandasDeRock[0].anoFormacao}. Seu maior sucesso é "${bandasDeRock[0].hitFamoso}".`;
```

Repita esse processo para as outras bandas no array.

---

## 🧠 Dica

Esse exercício é ótimo para reforçar:

- Acesso direto a propriedades de objetos em arrays
- Tipos de dados: `string`, `number`
- Template strings (`` `texto ${valor}` ``)

---

Bons estudos e divirta-se montando suas frases! 🚀





Bons estudos! 🚀
