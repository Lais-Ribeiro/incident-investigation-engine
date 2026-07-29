# Incident Investigation Engine

> Automatizando a investigação de incidentes operacionais por meio da análise de dados de observabilidade.

---

## 📖 Sobre o projeto

O **Incident Investigation Engine** é um projeto desenvolvido para automatizar parte do processo de investigação de incidentes em ambientes distribuídos.

A solução recebe um incidente em formato JSON, interpreta as informações disponíveis, identifica os parâmetros necessários para a investigação, consulta dados de observabilidade (simulados neste projeto) e realiza uma análise automatizada do comportamento das métricas durante o período do incidente.

Ao final da execução, é gerado um relatório consolidado contendo evidências que auxiliam na identificação da possível causa do problema, reduzindo o esforço manual e acelerando o processo de análise.

Este projeto foi desenvolvido com fins de estudo e demonstração de conhecimentos em Engenharia de Software, Engenharia de Dados, Observabilidade e automação de processos.

---

## 🎯 O problema

Em ambientes corporativos, a investigação inicial de um incidente costuma exigir diversas atividades manuais.

Após o registro de um incidente, o analista precisa interpretar as informações disponíveis, identificar o período afetado, localizar a aplicação envolvida, consultar métricas e logs em plataformas de observabilidade e reunir evidências para iniciar a análise da causa raiz.

Além de consumir tempo, esse processo pode variar de acordo com a experiência do analista, tornando a investigação menos padronizada e aumentando o tempo de resolução do incidente.

---

## 💡 Objetivo

Desenvolver uma aplicação capaz de automatizar as etapas iniciais da investigação de incidentes operacionais, reduzindo o tempo gasto na coleta de informações, padronizando o processo de análise e fornecendo um relatório estruturado para apoiar a identificação da causa raiz.

---

## 🚀 Funcionalidades previstas

- Receber incidentes em formato JSON.
- Interpretar automaticamente as informações presentes na descrição do incidente.
- Extrair dados relevantes para a investigação.
- Simular consultas em uma plataforma de observabilidade.
- Analisar o comportamento das métricas durante o período do incidente.
- Identificar possíveis anomalias.
- Gerar um relatório consolidado com os resultados da análise.

---

## 🏗️ Arquitetura

O projeto será desenvolvido utilizando uma arquitetura modular, onde cada componente possuirá uma responsabilidade específica.

```text
Incidente (JSON)
        │
        ▼
 Parser do Incidente
        │
        ▼
 Modelo de Dados
        │
        ▼
 Engine de Consultas
        │
        ▼
 Simulador de Observabilidade
        │
        ▼
 Motor de Análise
        │
        ▼
 Geração de Relatório
```

Essa separação facilita a manutenção, reutilização de código e evolução do projeto.

---

## 🛠️ Tecnologias

Tecnologias previstas para o desenvolvimento da primeira versão:

- Python
- Git
- GitHub
- JSON
- Pandas
- Pytest
- Visual Studio Code

---

## 📂 Estrutura do projeto

Em construção.

---

## 📅 Roadmap

- [x] Inicialização do repositório
- [x] Definição da proposta do projeto
- [ ] Estruturação da arquitetura
- [ ] Criação da estrutura de diretórios
- [ ] Modelagem dos dados
- [ ] Desenvolvimento do parser de incidentes
- [ ] Simulação das consultas de observabilidade
- [ ] Desenvolvimento do motor de análise
- [ ] Geração do relatório final
- [ ] Testes automatizados
- [ ] Documentação técnica

---

## 👩‍💻 Autor

Projeto desenvolvido por **Lais Ribeiro da Silva** como parte dos estudos em Engenharia de Software, Engenharia de Dados e automação de processos, com foco na aplicação de conceitos utilizados em ambientes corporativos de observabilidade e investigação de incidentes.