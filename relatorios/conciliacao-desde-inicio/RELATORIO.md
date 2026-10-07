# Conciliação bancária desde o início – METAVERSO CONTABILIDADE (Omie)

Data: 07/10/2026 · Empresa Omie: `metaverso-uuswexa` · CNPJ 39.332.252/0001-53
Extratos usados: Google Drive › DEPARTAMENTO FINANCEIRO › EXTRATOS METAVERSO CONTABILIDADE.
Nenhum dado do Omie foi alterado nesta etapa.

Planilha detalhada, linha a linha (fica só localmente, fora do git): `conciliacao_metaverso_desde_inicio.xlsx`.
Scripts que reproduzem o cruzamento: `scripts/`.

## Cobertura dos extratos

| Conta | Extrato no Drive | Situação |
|---|---|---|
| Banco Inter 077 / 8363367-7 | PDF 01/01/2021 a 27/04/2026 (825 movimentos) | Cruzado linha a linha |
| Cora 403 / 2637131-1 | CSV/OFX 01/01/2026 a 21/07/2026 (668 movimentos) | Cruzado linha a linha |
| ASAAS 461 / 1280911-7 | PDF 01/01/2025 a 31/12/2025 (96 movimentos) | Cruzado linha a linha |
| Cora antes de 2026, ASAAS antes de 2025 e depois de 2025, Inter depois de 27/04/2026 | **Não há extrato no Drive** | Não foi possível conciliar |

Os saldos lidos dos extratos foram conferidos: o saldo encadeado do Inter não tem nenhuma quebra; ASAAS vai de 135,14 para 0,00; o OFX da Cora informa saldo de 719,65 em 21/07/2026.

## Resultado por conta

| Conta | Saldo banco | Saldo Omie (mesma data) | Diferença | Casados | Falta lançar no Omie | No Omie sem banco |
|---|---:|---:|---:|---:|---:|---:|
| Inter (27/04/2026) | 40,32 | 10.315,63 | 10.275,31 | 134 | 691 (líq. -10.568,10) | 2 |
| Cora (21/07/2026) | 719,65 | ≈ -98 mil | ≈ 99 mil | 181 | 487 (líq. -1.151,38) | 15 |
| ASAAS (31/12/2025) | 0,00 | 8.527,89 | 8.527,89 | todos os de 2025 | 0 | 0 |

### Banco Inter
- O Omie só tem movimentos a partir de 05/2022 e começa com saldo zero. No banco, o saldo era R$ 196,11 em 30/04/2022, e houve 236 movimentos em 2021.
- De 2023 em diante, quase só as transferências Cora ↔ Inter foram lançadas. Pagamentos de fatura do cartão Inter, aplicações e resgates de CDB, boletos recebidos e Pix para pessoas **não estão no Omie** (691 movimentos).
- Erros: a aplicação em CDB de 26/09/2022 está com o sinal trocado (+150 em vez de -150). Uma "transferência Inter → Cora" de -80,00 em 28/08/2024 não existe no banco.

### Cora (2026)
- 29 títulos "Previstos" no Omie têm um movimento no banco com o mesmo valor e devem ser baixados. Em alguns recebimentos de R$ 531 o nome do pagador é diferente, por isso estão marcados como "conferir".
- 487 movimentos do banco não estão no Omie. Os maiores grupos são Pix para pessoas (Luana, Zilma, Elis, Celso, Talyssa, Gabriel etc.), Hapvida, Tron, fatura Cora e vários recebimentos de clientes (FLX, Eletro Máquinas, Cantinho Animal, Antônio de Sousa Costa, Icon etc.).
- 15 lançamentos do Omie não têm movimento no banco. Os principais são 9 recebimentos de MARQUES DRINKS (R$ 3.572,50), que podem ter sido pagos de forma agrupada ou em outra conta.
- O saldo de abertura de 2026 no Omie é **-101.619,66**, contra **4.602,43** no banco. Essa diferença de R$ 106 mil vem de antes de 2026 e só pode ser investigada com os extratos da Cora de 2022 a 2025.

### ASAAS (2025)
- O movimento de 2025 bate com o banco, com diferença de R$ 4,97: três tarifas (1,99 + 1,99 + 0,99) foram lançadas como receita.
- O saldo de abertura de 2025 no Omie é 8.658,06, contra 135,14 no banco. Dessa diferença, R$ 7.390,00 são lançamentos "não conciliados" anteriores a 2025 que não existem no banco.
- Quatro saídas classificadas como "Transf. ASAAS → Cora" (457,00, 750,00, 230,00 e 528,71) **entraram no Banco Inter** (Pix de "A.L.L. Assessoria", nome do titular da conta Inter).

## Por que não marquei como conciliado
A API do Omie não tem operação para conciliar nem para importar OFX. A marcação final é feita na tela *Finanças › Conciliação Bancária*.

## Próximos passos sugeridos
1. **Inter**: importar no Omie os OFX do Inter de 2021 a 2026, a mesma rotina usada em 27/04/2026 para 05–12/2022, e lançar o saldo inicial de 196,11 em 30/04/2022 (ou o saldo de 01/01/2021).
2. **Corrigir os erros** da aba "Erros a corrigir": CDB, transferência de -80, tarifas do ASAAS e destino das 4 transferências.
3. **Cora**: baixar os 29 previstos confirmados e lançar os 487 movimentos faltantes, de preferência importando o OFX de 2026 que está no Drive.
4. **Enviar ao Drive** os extratos da Cora de 2022–2025 e do ASAAS de 2022–2024 e 2026, para fechar as diferenças de abertura.
5. ASAAS: identificar e estornar os R$ 7.390,00 não conciliados anteriores a 2025.

## Correções executadas no Omie em 07/10/2026 (autorizadas)

| Conta | Data | Valor | Cód. lançamento | Ação | Resultado |
|---|---|---:|---|---|---|
| ASAAS | 11/08/2025 | -457,00 | 5202076157 | Destino da transferência Cora → **Banco Inter** | OK |
| ASAAS | 14/08/2025 | -750,00 | 5202076577 | Destino Cora → **Banco Inter** | OK |
| ASAAS | 01/10/2025 | -230,00 | 5202078842 | Destino Cora → **Banco Inter** | OK |
| ASAAS | 15/12/2025 | -528,71 | 5202089098 | Destino Cora → **Banco Inter** | OK |
| ASAAS | 07/08/2025 | +1,99 | 5202075539 | Excluído (tarifa lançada como receita; o -1,99 correto já existia) | OK |
| ASAAS | 10/09/2025 | +1,99 | 5202077653 | Excluído (idem) | OK |
| ASAAS | 10/09/2025 | +0,99 | 5202077710 | Excluído (idem) | OK |
| Inter | 26/09/2022 | +150,00 | 5234938505 | Excluir (CDB com sinal trocado) | **Bloqueado**: período contábil set/2022 fechado no Painel do Contador |
| Inter | 28/08/2024 | -80,00 | 5027039646 | Excluir (transferência inexistente) | **Bloqueado**: período contábil ago/2024 fechado no Painel do Contador |

Conferência após as correções: o ASAAS fecha 2025 com saldo 8.522,92 no Omie (movimento do ano = -135,14, igual ao banco); o Inter recebeu os +1.965,71 das transferências corrigidas.
O arquivo `INTER_faltantes_2025.ofx` foi regerado sem essas 4 entradas (133 movimentos).

**Atenção para a importação dos OFX**: os períodos até pelo menos ago/2024 estão bloqueados no Painel do Contador. A importação dos extratos do Inter de 2021 a 2024 também vai ser recusada até que esses meses sejam desbloqueados.
