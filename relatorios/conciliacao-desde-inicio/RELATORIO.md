# Conciliação bancária desde o início – METAVERSO CONTABILIDADE (Omie)

Data: 07/10/2026 · Empresa Omie: `metaverso-uuswexa` · CNPJ 39.332.252/0001-53
Extratos usados: Google Drive › DEPARTAMENTO FINANCEIRO › EXTRATOS METAVERSO CONTABILIDADE.
Na primeira etapa (diagnóstico) nenhum dado foi alterado; as correções e inclusões autorizadas estão nas seções finais.

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
| Inter | 26/09/2022 | +150,00 | 5234938505 | Excluído (CDB com sinal trocado; o -150 correto vem no OFX do Inter 2022) | OK (após desbloqueio do período) |
| Inter | 28/08/2024 | -80,00 | 5027039646 | Excluída (transferência inexistente no Inter) | OK (após desbloqueio do período) |
| Cora | 28/08/2024 | +80,00 | 5305452044 | Incluído: devolução de Pix recebida (categoria 1.03.26), que antes vinha embutida na transferência excluída | OK, falta marcar conciliado na tela |

Conferência após as correções: o ASAAS fecha 2025 com saldo 8.522,92 no Omie (movimento do ano = -135,14, igual ao banco); o Inter recebeu os +1.965,71 das transferências corrigidas e, após as duas exclusões, fecha 2025 em 12.211,34; o saldo da Cora em 29/08/2024 ficou inalterado (-63.402,26).
O arquivo `INTER_faltantes_2025.ofx` foi regerado sem essas 4 entradas (133 movimentos).

Períodos contábeis desbloqueados pelo usuário em 07/10/2026; a importação dos OFX do Inter 2021–2024 está liberada.

## Lote de inclusões executado em 07/10/2026 (aprovado pelo usuário)

Plano aprovado: `plano_lancamentos_para_aprovar.xlsx`, com as categorias ajustadas pelo usuário. Todos os lançamentos levam `cCodIntLanc` com prefixo `CBI`/`CBT` e a observação "conc. API". Isso evita duplicidade e permite localizá-los depois.

| Grupo | Qtde | Resultado |
|---|---:|---|
| Movimentos do banco que faltavam (Inter 2021–2026 e Cora 2026) | 1.052 | 1.052 OK |
| CDB Inter: aplicações (2.07.99) e resgates (1.02.02) | 63 | 63 OK |
| Transferências entre contas próprias (Inter/Cora/ASAAS) | 46 | 46 OK |
| Recebimentos da Cora convertidos em transferência Inter → Cora (5036375309, 5036375231, 5201823805) | 3 | Alterados |
| Aplicações "Inter Corporate FIRF CP" de 18/08/2023 e 14/11/2023, que entraram como receita | 2 | Corrigidas para 2.07.99 (saída) |

Decisões do usuário aplicadas:
- Pix de Luana que voltaram para a empresa → 1.03.26 (devolução).
- Aplicações → 2.07.99.
- Calima 187,34 → 2.04.99.
- Fatura do cartão → 2.01.99.

Conferência automática: cada lançamento do lote foi comparado com o extrato (conta, data, valor e sinal). Não sobrou nenhuma divergência.

## Saldos após o lote

| Conta | Data | Banco | Omie | Diferença | Explicação |
|---|---|---:|---:|---:|---|
| Inter | 28/12/2021 | 147,44 | 147,44 | 0,00 | Fechado |
| Inter | 20/12/2022 | 268,01 | 268,01 | 0,00 | Fechado |
| Inter | 27/04/2026 | 40,32 | 739,32 | 699,00 | 3 transferências antigas (abaixo) |
| Cora | movimento 01/01 a 21/07/2026 | -3.882,78 | -7.786,28 | -3.903,50 | Itens pendentes (abaixo) |

### Pendências resolvidas em 07/10/2026 (autorizadas pelo usuário)
1. **Inter, R$ 699,00**: a conta de origem das 3 transferências foi trocada para o Banco Inter:
   - 5201941157: 28/08/2023, 20,00, agora Inter → ASAAS.
   - 5202118313: 16/11/2023, 500,00, agora Inter → Cora.
   - 5202118579: 16/11/2023, 179,00, agora Inter → Cora.

   **O Inter fecha em 40,32 em 27/04/2026, igual ao banco.**
2. **Cora 2026**:
   - 14 recebimentos previstos foram baixados na Cora, com conciliação, na data do extrato.
   - Os títulos 5230641282, 5234256261 e 5232383152 não existiam mais no Omie. Por isso os 3 recebimentos foram lançados direto na conta, com os códigos CBC20260330MG531, CBC20260406NORTE531 e CBC20260505MF597.
   - O pagamento de 125,00 da Associação Comercial do Pará (título 5201935224) foi baixado em 10/02/2026.
   - Movimento de 2026 no Omie = movimento do banco (-3.882,78) + 8.598,50. Os 8.598,50 são os 15 lançamentos do Omie sem movimento no banco.
3. **Extrato Inter em CNAB 240 (.RET) de 01/01/2025 a 27/04/2026**, enviado pelo usuário: os 34 movimentos já estavam no extrato PDF usado e estão lançados. O saldo inicial é 41,62 e o final é 40,32, os dois iguais ao Omie.

### Pendências que continuam
1. Cora: 15 lançamentos do Omie sem movimento no banco (8.598,50). Nove são de Marques Drinks e estão "não conciliados". Os outros 6 estão marcados como conciliados, mas não aparecem no extrato.
2. Saldo de abertura da Cora: depende dos extratos da Cora de 2022–2025.
3. Marcar como conciliado, na tela *Finanças › Conciliação Bancária*, os lançamentos incluídos pela API.

## Cora 2022–2024 (extratos enviados pelo usuário em 07/10/2026)

| Ano | Banco: movimentos / soma | Saldo banco 31/12 | Saldo Omie 31/12 | Situação |
|---|---|---:|---:|---|
| 2022 | 148 / 3.028,58 (conta aberta em 23/06/2022) | 3.028,58 | 3.028,58 | **Fechado** |
| 2023 | 407 / 356,67 | 3.385,25 | -25.729,61 | 117 movimentos do banco faltam no Omie (+15.300,15); 24 previstos a baixar (13.374,00) |
| 2024 | 624 / -1.626,39 | 1.758,86 | -131.483,29 | 189 movimentos do banco faltam no Omie (+97.285,29); 14 previstos a baixar (7.742,00) |

Se o plano `relatorios/conciliacao-desde-inicio/plano_cora_2023_2024_para_aprovar.xlsx` (local, fora do git) for aplicado, o Omie fecha 2024 em 1.758,86, igual ao banco. Conta feita: -131.483,29 + 112.585,44 de inclusões + 21.116,00 de baixas + 440,71 - 900,00 de lançamentos sem banco.

O plano aguarda aprovação. Dos 38 previstos, 27 têm o valor igual ao do banco, mas um pagador diferente do cliente do título.

A única transferência criada hoje que não aparece no extrato da Cora é a de 1.550,00 Cora → Inter em 02/03/2023. A origem provável é a ASAAS. Ainda falta o extrato da Cora de 2025.

### Cora 2023–2024: plano aplicado em 07–08/10/2026 (aprovado pelo usuário)
- 306 lançamentos incluídos (códigos `CBC…`), com as categorias da planilha aprovada.
- 35 previstos baixados com conciliação.
- 3 títulos já não existiam (5029831256, 5029834877 e 5029834109). Os recebimentos foram lançados direto na conta: CBC20241129NOSSA706, CBC20241212EVELYN600 e CBC20241223ANTON600.

| Data | Banco | Omie | Diferença | Explicação |
|---|---:|---:|---:|---|
| 31/12/2022 | 3.028,58 | 3.028,58 | 0,00 | Fechado |
| 31/12/2023 | 3.385,25 | 2.944,54 | -440,71 | Transferência de 1.550,00 em 02/03/2023 que não passou pela Cora (-1.550,00), mais Intertech 670,53 e Playtech 438,76, que não estão no extrato |
| 31/12/2024 | 1.758,86 | 2.218,15 | +459,29 | A diferença de 2023 (-440,71), mais RDS 450 e ICON 450 de 24/07/2024, que não estão no extrato |

Não há outra diferença. Os itens restantes dependem de decisão do usuário (aba "Questões").

### Cora 2022–2024: questões resolvidas em 08/10/2026 (aprovado pelo usuário)
- Transferência CBTa0476295fa9f73e22 (1.550,00 em 02/03/2023): origem trocada de Cora para ASAAS. O destino continua sendo o Inter.
- Incluídos dois lançamentos em 26/09/2022: CBC20220926MARIANA (+125, categoria 1.01.03) e CBC20220926JUCEB (-125, categoria 2.04.99).
- Excluídas as transferências ASAAS ↔ Cora sem movimento no extrato:
  - 15/03/2022, 120,00 (5201936821 e 5201936826);
  - 14/06/2023, 90,00 (5201938174 e 5201938177).

  Os dois lados foram removidos. Na ASAAS o efeito é zero.
- Recebimentos cancelados (baixa desfeita), porque não estão no extrato:
  - Intertech, 670,53 (baixa 4872283922);
  - Playtech, 438,76 (baixa 4872321843);
  - RDS, 450 (baixa 5027218826);
  - ICON, 450 (baixa 5027218830).

  **Os títulos voltaram para "em aberto"**: 4872275652, 4872314771, 5025248180 e 5025248131.

| Data | Banco | Omie |
|---|---:|---:|
| 31/12/2022 | 3.028,58 | 3.028,58 |
| 31/12/2023 | 3.385,25 | 3.385,25 |
| 31/12/2024 | 1.758,86 | 1.758,86 |

**Cora fechada de 2022 a 2024.** O ano de 2025 depende do extrato da Cora de 2025.
- **Correção em 08/10/2026 (informação do usuário):** os 900,00 pagos pela Icon cobrem dois títulos de 450, um da RDS e um da ICON. Por isso:
  - os títulos 5025248180 (RDS) e 5025248131 (ICON) foram baixados de novo em 24/07/2024 (baixas 5305911064 e 5305911190);
  - foi excluído o lançamento CBCcb66d615b479dedbc, um recebimento de 900,00 que duplicava esse pagamento.

  O saldo não mudou.
- Ainda há títulos RDS/ICON de 2024 em aberto (abril, maio e junho), com títulos duplicados em maio e junho. Os 900,00 recebidos da BELCON ENGENHARIA em 16/04, 23/05 e 20/06/2024 entraram como recebimentos avulsos. Isso aguarda a confirmação do usuário.
- **BELCON = pagador da RDS + ICON (informação do usuário).** Os títulos de 2024 foram baixados de dois em dois (450 da RDS + 450 da ICON) pelos 900,00 recebidos da BELCON:
  - 16/04/2024: títulos 5025248150 e 5025248124;
  - 23/05/2024: títulos 5025248175 e 5025248127;
  - 20/06/2024: títulos 5025248177 e 5025248129.

  Os recebimentos avulsos que duplicavam esses pagamentos foram excluídos (CBCb6b9b306f7ae392ef, CBC5cb658e8d79b913ca e CBC21361ae51dd16c1b8). A Cora continua fechando em 1.758,86 em 31/12/2024.
- Ainda estão abertos 4 títulos gerados por OS para maio e junho de 2024, em duplicidade com os títulos acima:
  - RDS: 4968324447 e 4968324550;
  - ICON: 4968324685 e 4968324641.

  Aguardam a decisão do usuário: excluir ou manter.

## Conciliação atual (09/10/2026): Cora set–out e Inter mai–out
- **Cora**: 117 movimentos de 01/09 a 09/10/2026. O saldo do banco em 09/10 é 2.668,72 (bate com o OFX). Faltam 89 lançamentos no Omie, há 18 previstos a baixar e 6 transferências entre contas.
- **Inter**: 46 movimentos de 28/04 a 09/10/2026. O saldo em 09/10 é 137,66 (bate com o extrato). Faltam 33 lançamentos e há 7 transferências entre contas.
- **Inter, diferença nova de +215,93**: 5 lançamentos de abr–mai/2022 foram criados em duplicidade em 07/10, às 18:57, pela importação de extrato na tela do Omie. Sugestão: excluir.
- O plano está em `plano_set_out_2026_cora_inter.xlsx` (local, fora do git) e aguarda aprovação.
- Ainda falta o extrato da Cora de 22/07 a 31/08/2026.

## ASAAS 2026 (01/01 a 09/10/2026)
- O extrato tem 138 movimentos e soma +93,38 (o saldo vai de 0,00 a 93,38).
- No Omie há 35 lançamentos realizados, e **todos casam com o banco**.
- **Falta lançar** (abas `ASAAS *` de `plano_set_out_2026_cora_inter.xlsx`):
  - 88 inclusões:
    - 74 tarifas, que somam -189,81;
    - recebimentos: Ortoclínica (244,96 e 240,00), Rodrigo (mar e abr) e Janaina (cartão, 5 × 373,11);
    - pagamentos: Pix à Luana (2 × 100), SEFA (114,19), Vivo (219,89) e um boleto de 90,00 sem identificação.
  - 3 títulos do Rodrigo:
    - recibos 38 e 47, que estão na conta Cora e foram pagos na ASAAS;
    - RPS 69, baixado na Cora quando o dinheiro entrou na ASAAS.
  - 2 recebimentos de contrato em out/2026 (Alcateia e Rodrigo).
  - 2 transferências: 1.530,00 ASAAS→Inter em 14/09 e 900,00 ASAAS→Cora em 09/10.
- **Diferença de abertura:** o Omie mostra 7.651,92 em 31/12/2025 e o banco mostra 0,00. Como o movimento de 2025 já bate, a diferença é anterior a 2025. Para resolver, é preciso o extrato da ASAAS de 2022–2024 ou um ajuste de saldo.

## Execução do plano aprovado (09/10/2026)
Planilha devolvida pelo usuário com as categorias corrigidas:
- **Lançamentos feitos no Omie:**
  - 204 inclusões (Cora, Inter e ASAAS), todas OK;
  - 26 baixas de título;
  - 8 transferências entre contas;
  - o RPS 69 do Rodrigo saiu da Cora e foi baixado de novo na ASAAS.
- **Categorias informadas pelo usuário:**
  - Estagiário 2.03.98;
  - Retirada de sócio 2.03.96, que vale para a Luana a partir daqui;
  - Multa 2.05.02;
  - Salário 2.03.01;
  - Rescisão 2.03.04;
  - Comissão 2.02.01;
  - Devolução ao cliente 2.09.02;
  - Serviços PF 2.04.93 e PJ 2.04.92;
  - Empréstimos 2.05.99;
  - Lanche 2.03.12.
- **Pix do Antônio (2.000,00 em 10/09):** quitou os RPS 81 (Ant. Costa Barão), 92 (Super 20tão), 105 (Moama) e 101 (O Vintão).
- **Baixas que o Omie recusou** (o título foi emitido como cobrança Cora, então a integração faz a baixa sozinha):
  - Ministério 75;
  - Popperl 531;
  - FLX 922,49 e 3.279,99;
  - O Vintão RPS 101, 438: este não vai baixar sozinho, porque foi pago por Pix avulso.
- **Conferência de saldos em 09/10/2026:**
  - **Cora:** o movimento de set–out no Omie bate com o banco, considerando os itens pendentes listados acima e abaixo (7.382,69). A diferença de abertura de 30.659,47 em 31/08 vem do período 22/07–31/08, que ainda não tem extrato.
  - **Inter:** o Omie mostra 896,70 e o banco 137,66. A diferença de 759,04 é a soma de:
    - 5 lançamentos duplicados de 2022: +215,93;
    - 3 lançamentos de 08/10 que não estão no banco: +179,67;
    - Pix à S N ainda não lançado: +363,44.
  - **ASAAS:** o Omie mostra 6.748,30 e o banco 93,38. A diferença de 6.654,92 é a soma de:
    - saldo antigo anterior a 2025: 7.651,92;
    - menos os recebimentos de outubro ainda não lançados (Alcateia 500 e Rodrigo 497): −997.
- **Ainda pendente com o usuário:**
  - Marques 1.062 (09/09): quais títulos baixar;
  - E. Ferreira 543,21 (19/09);
  - Pix de 363,44 para a S N (25/09);
  - recebimentos de contrato de outubro sem nota (Norte Gestão, Alcateia e Rodrigo);
  - exclusões no Inter;
  - saldo antigo da ASAAS.
- 09/10: o Pix de 363,44 para a S N (25/09, Inter) foi lançado em 2.04.06 Material de Escritório/Limpeza (lançamento 5306684963), conforme informado pelo usuário. Com isso, a diferença que sobra no Inter é 395,60 (os 5 duplicados mais os 3 itens de 08/10).
