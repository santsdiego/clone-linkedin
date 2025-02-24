# LEIA COM ATENÇÃO

Esta é uma aplicação criada com NextJS, utilizando ReactJS.

## O que fazer para começar a codar no projeto

**Extensões obrigatórias! em seu VSCode:**

```txt
1.Prettier - Code Formatter
2.PostCSS Language Support
3.TailwindCSS IntelliSense
```

**Extensões não obrigatórias:**

```txt
1.Material Icon Theme (recomendado)
```

## Instalação das dependências

Após instalar as extensões e já estiver com o projeto clonado, execute o seguinte comando no terminal:

```bash
npm install
```

## Executando servidor de teste

Para executar o servidor de testes do Frontend, execute o comando:

```bash
npm run dev
```

Abra [http://localhost:3000](http://localhost:3000) no seu navegador para ver o resultado.
As Páginas automaticamente atualizam no navegador assim que uma alteração é feita.

## Fontes externas

Esse projeto utiliza [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) para automaticamente otimizar o carregamento das fontes.\
Qualquer importação de fonte, utilizem o `next/font` como primeiro plano. Utilizem este recurso pois o framework lida melhor com esse tipo de importação.\
A fonte padrão do nosso projeto será a "SourceSans3";\
A fonte ja foi importada no `src/app/Layout.tsx`;\
A configuração de importação da fonte está localizada em `src/utils/font.ts`;\
Caso seja necessário a importação desta fonte em outros Layouts, faça a importação do arquivo `src/utils/font.ts`.

## Informações importantes sobre o TailwindCSS

Sim, o Tailwind é um framework CSS. Ele oferece a possibilidade de criar layouts de forma mais produtiva.\
Abaixo estão algumas informações importantes sobre o Tailwind CSS.

1. Tenha em mente que o TailwindCSS é **"Mobile-first"**. O que isso significa:
   O TailwindCSS prioriza as configurações em dispositivos móveis. Isso significa que os designs são otimizados para telas menores, garantindo que os sites funcionem bem nos dispositivos móveis. Basicamente quase toda a sua estrutura é construída em unidades de medida relativas, sendo assim mais fácil e produtivo de lidar com diferentes tamanhos de telas.
2. O Tailwind utiliza prefixos `sm, md, lg e xl` para definir tamanhos para dispositivos. São os famosos "breakpoints".\
   Para simplificar um pouco:

   1. sm: (small, Min-width: 640px): Telas pequenas (smartphones);
   2. md: (medium, Min-width: 768px): Telas médias (tablets);
   3. lg: (large, Min-width: 1024px): Telas grandes (laptops);
   4. xl: (extra-large, Min-width: 1280px): Telas extra grandes (desktops);
   5. 2xl: (2extra-large, Min-width: 1536px): Telas muito grandes (4K, etc.).

3. Como funciona o "mobile-first" e os Breakpoints?
   No Tailwind, você pode aplicar estilos específicos para diferentes tamanhos de tela usando os prefixos acima. Por exemplo:

```tsx
<div class="bg-gray-200 p-4 xl:bg-blue-500 xl:text-white">
  Este fundo ficará azul e o texto branco em telas 1920x1080.
</div>
```

O que está acontecendo no código acima:

```txt
Em telas menores que 1280px, o fundo será cinza e o texto preto.
Em telas 1280px ou maiores (incluindo 1920x1080), o fundo ficará azul e o texto branco.
```

## Saiba mais

Para saber mais sobre Next.js, veja sua documentação:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
