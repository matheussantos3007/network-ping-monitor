# Network Ping Monitor: Automação de Monitoramento de Ativos

Este projeto consiste em uma aplicação de software desenvolvida para automatizar a verificação contínua de disponibilidade de hosts e ativos críticos em uma rede de provedor de internet (ISP).

---

## 🎯 Objetivo do Projeto
O propósito principal é substituir testes manuais de conectividade por um monitoramento resiliente e programático.
* **Detecção Automática:** Identificar quedas de equipamentos na rede de forma ágil.
* **Geração de Logs:** Registrar timestamps exatos de falhas para análise de SLA.
* **Alertas em Tempo Real:** Notificar administradores do sistema sobre indisponibilidades.

---

## 🛠️ Tecnologias Utilizadas
A solução foi arquitetada utilizando práticas modernas de desenvolvimento de software:
* **Python 3:** Linguagem base para a lógica do script e manipulação de dados.
* **Subprocess & Multithreading:** Módulos nativos para executar requisições ICMP (ping) paralelas, otimizando o tempo de resposta.
* **Loguru / Logging:** Biblioteca para estruturação de arquivos de log de auditoria.
* **Git & GitHub:** Ferramentas para controle de versão do código fonte.

---

## 🧠 O Que Foi Aprendido com a Experiência
O desenvolvimento deste software consolidou conceitos fundamentais de programação estruturada e automação de redes:
* **Programação Concorrente:** Aplicação de threads para monitorar múltiplos IPs simultaneamente, eliminando gargalos sequenciais.
* **Tratamento de Exceções:** Implementação de estruturas robustas de *try/except* para lidar com falhas de timeout e erros de DNS.
* **Manipulação de Arquivos:** Persistência de dados de rede em relatórios estruturados para análise técnica posterior.
