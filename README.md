# Phishing para captura de senhas do Facebook

### Ferramentas

- Kali Linux
- setoolkit
- Python

### Configurando o Phishing no Kali Linux

- Acesso root: ``` sudo su ```
- Iniciando o setoolkit: ``` setoolkit ```
- Tipo de ataque: ``` Social-Engineering Attacks ```
- Vetor de ataque: ``` Web Site Attack Vectors ```
- Método de ataque: ```Credential Harvester Attack Method ```
- Método de ataque: ``` Site Cloner ```
- Obtendo o endereço da máquina: ``` ifconfig ```
- URL para clone: http://www.facebook.com

### Resutados





# 🛡️ SEToolkit Automation

Um script desenvolvido em Python para automatizar interações com o **Social-Engineer Toolkit (SET)** por meio do terminal.

O projeto foi criado com finalidade educacional, explorando os recursos de automação do Python e sua capacidade de interagir com ferramentas utilizadas em testes de segurança da informação.

---

## ⚙️ Requisitos

Antes de executar o projeto, certifique-se de possuir:

* **Kali Linux:** Sistema operacional recomendado para execução.
* **Python 3:** Interpretador utilizado para executar o script.
* **Pexpect:** Biblioteca Python para automatizar aplicações interativas de linha de comando.
* **Social-Engineer Toolkit (SET):** Framework utilizado para testes de engenharia social.

---

## 📦 Instalação

### 1. Instale o Kali Linux

Este projeto foi desenvolvido para funcionar no Kali Linux.

### 2. Verifique a instalação do Python 3

O Python 3 geralmente já vem instalado no Kali Linux.

Para verificar sua versão, execute:

```bash
python3 --version
```

### 3. Instale a biblioteca Pexpect

A biblioteca Pexpect é responsável por permitir que o Python interaja com aplicações executadas no terminal.

Para instalá-la, utilize o seguinte comando:

```bash
sudo apt update
sudo apt install python3-pexpect
```

### 4. Instale o SEToolkit

Instale o Social-Engineer Toolkit utilizando o gerenciador de pacotes do Kali Linux:

```bash
sudo apt install set
```

Para verificar se a instalação foi realizada corretamente, execute:

```bash
sudo setoolkit
```

---

## 🚀 Como executar

Primeiramente, clone este repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DO_PROJETO
```

Execute o script Python:

```bash
python3 main.py
```

---

## 🧰 Tecnologias utilizadas

| Tecnologia | Finalidade                                      |
| ---------- | ----------------------------------------------- |
| Python 3   | Linguagem principal do projeto                  |
| Pexpect    | Automação de aplicações interativas no terminal |
| Kali Linux | Ambiente de execução                            |
| SEToolkit  | Framework para testes de engenharia social      |

---

## 🎯 Objetivos do projeto

* Explorar os recursos de automação do Python.
* Aprender a interagir com aplicações executadas pelo terminal.
* Praticar gerenciamento de processos utilizando Python.
* Aprimorar conhecimentos em programação.
* Estudar ferramentas utilizadas em testes de segurança da informação.

---

## ⚠️ Aviso legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais e testes de segurança autorizados**.

O objetivo é explorar os recursos de automação do Python e compreender como ferramentas de segurança podem ser controladas programaticamente.

Não utilize este projeto para realizar atividades sem autorização, obter informações de terceiros ou comprometer sistemas.

O autor não se responsabiliza pelo uso indevido do software.

---

## 👨‍💻 Autor

**GhostXYZ**

Desenvolvedor Python | Entusiasta de Cyber Security | Ethical Hacking

---

<p align="center">
  <b>Aprender • Automatizar • Pesquisar • Proteger</b>
</p>

