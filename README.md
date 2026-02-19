<h1 align="center">📦 Controle de Estoque - Sistema em Python</h1>

<p align="center">
Sistema de gerenciamento de estoque desenvolvido em Python com foco em
lógica de programação, organização modular e controle de dados.
</p>

<br>

<h2>📌 Sobre o Projeto</h2>

<p>
O <b>Controle de Estoque</b> é uma aplicação executada no terminal que simula
operações essenciais de gerenciamento de produtos.
O projeto foi desenvolvido com o objetivo de fortalecer fundamentos em
programação, aplicando regras de negócio reais em um ambiente controlado.
</p>

<p>
A aplicação permite cadastrar produtos, realizar entradas e saídas de estoque,
visualizar listagens e gerar relatório financeiro, utilizando
<b>dicionários aninhados</b> como estrutura principal de armazenamento.
</p>

<br>

<h2>🚀 Funcionalidades</h2>

<ul>
<li><b>Cadastro de Produto:</b> Geração automática de código e registro inicial no histórico.</li>
<li><b>Entrada de Estoque:</b> Atualização de quantidade com validação de valor positivo.</li>
<li><b>Saída de Estoque:</b> Validação de estoque suficiente antes da retirada.</li>
<li><b>Listagem de Produtos:</b> Exibição organizada com código, nome, preço e quantidade.</li>
<li><b>Relatório Geral:</b> Cálculo do valor total armazenado em estoque.</li>
<li><b>Histórico de Movimentações:</b> Registro completo de entradas e saídas.</li>
<li><b>Menu Interativo:</b> Controle de fluxo contínuo até encerramento do sistema.</li>
</ul>

<br>

<h2>🧠 Estrutura de Dados</h2>

<p>Os produtos são armazenados em um dicionário principal chamado <b>estoque</b>:</p>

<pre>
{
    codigo_produto: {
        "Nome": "Produto",
        "Preço": 0.00,
        "Quantidade": 0,
        "Historico": []
    }
}
</pre>

<p>
Essa estrutura permite acesso direto pelo código do produto e atualização dinâmica
das informações de estoque.
</p>

<br>

<h2>⚙️ Regras de Negócio Implementadas</h2>

<ul>
<li>Não permite cadastro com preço ou quantidade negativos.</li>
<li>Não permite entrada com valor menor ou igual a zero.</li>
<li>Não permite saída com valor menor ou igual a zero.</li>
<li>Impede saída superior à quantidade disponível.</li>
<li>Valida existência do produto antes de qualquer operação.</li>
<li>Registra todas as movimentações no histórico.</li>
<li>Utiliza tratamento de exceções para evitar erros de entrada.</li>
</ul>

<br>

<h2>🛠️ Tecnologias Utilizadas</h2>

<ul>
<li><b>Python 3</b></li>
<li>Estruturas de dados (dicionários e listas)</li>
<li>Funções</li>
<li>Estruturas condicionais</li>
<li>Laços de repetição</li>
<li>Tratamento de exceções (try/except)</li>
<li>F-strings para formatação monetária</li>
</ul>

<br>

<h2>🎯 Objetivo do Projeto</h2>

<p>
Consolidar conhecimentos em lógica de programação e simular a construção
de um sistema funcional aplicando princípios fundamentais de desenvolvimento
back-end e controle de dados.
</p>

<br>

<h2>📈 Possíveis Evoluções</h2>

<ul>
<li>Persistência de dados em arquivo JSON</li>
<li>Implementação com orientação a objetos</li>
<li>Banco de dados (SQLite)</li>
<li>Interface gráfica (Tkinter)</li>
<li>Sistema de busca por nome</li>
<li>Exclusão de produtos</li>
</ul>

<br>

<h2>👨‍💻 Autor</h2>

<p>
<b>Caio Renan</b><br>
Desenvolvedor em formação com foco em back-end e estruturação de sistemas.
</p>
