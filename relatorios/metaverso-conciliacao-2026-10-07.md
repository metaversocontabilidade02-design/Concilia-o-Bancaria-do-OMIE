# Conciliação bancária – METAVERSO CONTABILIDADE (Omie)

Data da análise: 07/10/2026 · Período analisado: 01/09/2026 a 07/10/2026
Fonte: extrato de conta corrente do Omie (API `financas/extrato:ListarExtrato`). Nenhum dado foi alterado.

> **Limitação:** a API do Omie não tem operação para marcar lançamentos como conciliados nem para importar o OFX do banco.
> A marcação final precisa ser feita na tela *Finanças → Conciliação Bancária* do Omie, depois de importar o extrato do banco.
> Este relatório lista o que está pendente no Omie para essa etapa.

## Resumo por conta

| Conta | Saldo Omie (realizado) | Saldo conciliado | Diferença a conciliar | Pendências no período |
|---|---:|---:|---:|---|
| Banco Inter (077 / 8363367-7) | 8.686,36 | 7.658,36 | 1.028,00 | 2 recebimentos não conciliados |
| ASAAS (461 / 1280911-7) | 9.405,65 | 521,65 | 8.884,00 | 2 recebimentos não conciliados; ~7.887,00 vêm de antes de set/26 |
| Cora (403 / 2637131-1) | **-81.434,28** | -130.046,42 | 48.612,14 | 4 recebimentos não conciliados + 56 títulos previstos vencidos |
| Omie.CASH (Boletos) | 0,00 | 0,00 | – | sem movimento |
| Omie.CASH (Ative agora) | 0,00 | 0,00 | – | sem movimento |

## Lançamentos realizados ainda não conciliados (set/26)

| Conta | Data | Cliente | Valor | Cód. lançamento |
|---|---|---|---:|---|
| Inter | 08/09 | CORREA CONSTRUCOES E ENGENHARIA (RPS 99) | 531,00 | 5293446085 |
| Inter | 08/09 | J DE F DANTAS ANDRADE DE SOUZA (260904) | 497,00 | 5293533190 |
| ASAAS | 01/09 | ALCATEIA REPRESENTACAO (RPS 82) | 500,00 | 5292501255 |
| ASAAS | 08/09 | RODRIGO LEITAO ADVOCACIA (RPS 95) | 497,00 | 5293298398 |
| Cora | 01/09 | ELETRO MAQUINAS | 2.400,00 | 5292502169 |
| Cora | 04/09 | LOURDES OLIVEIRA LTDA | 531,00 | 5293261470 |
| Cora | 04/09 | LOURDES OLIVEIRA LTDA | 531,00 | 5293262674 |
| Cora | 08/09 | STOP MODAS 20&25 LTDA | 531,00 | 5293260229 |

Inter e ASAAS somam exatamente a diferença de set/26 entre saldo realizado e conciliado (1.028,00 e 997,00).

## Pontos de atenção (verificar contra o extrato do banco)

1. **Cora com saldo negativo de R$ 81 mil** – não é plausível em conta corrente sem limite. Há recebimentos lançados como "previstos" que provavelmente já entraram no banco e não foram baixados, ou um saldo inicial errado.
2. **Possíveis duplicidades na Cora:**
   - LOURDES OLIVEIRA 531,00 recebido 2x em 04/09 e ainda previsto em 05/09 e 10/09.
   - ELETRO MAQUINAS 2.400,00 recebido em 01/09 e ainda previsto em 09/09.
   - STOP MODAS 531,00 recebido em 08/09 e ainda previsto em 10/09.
   - MEGA 20 TAO 531,00 previsto 2x em 10/09; 5QUENTAO MIX com 3 títulos (531, 531, 1.062).
   - Pagamentos em pares/trios: TIQUETAQUE 53,20 (2x), "IMPOSTO DE RENDA" 53,20 (2x, lançado como recebimento), ADMINISTRADORA DE CARTAO 30,90 (3x), HAPVIDA 4.143,85 + 189,70.
3. **56 títulos "Previstos" vencidos na Cora** (R$ 22.846,67 líquidos) e 3 no Inter / 2 no ASAAS – precisam ser baixados (se pagos/recebidos) ou reprogramados.
4. **ASAAS:** R$ 7.887,00 não conciliados de períodos anteriores a set/26 – rever meses anteriores.
5. "IMPOSTO DE RENDA" (53,20) aparece como **recebimento** na categoria de clientes – provável erro de natureza.

## Próximos passos

1. Baixar os extratos OFX de set/26 e out/26 (Inter, ASAAS, Cora).
2. Com os OFX em mãos, cruzar linha a linha com os lançamentos acima (posso fazer esse cruzamento automaticamente).
3. Corrigir duplicidades e baixar previstos já liquidados.
4. Importar o OFX no Omie e confirmar a conciliação na tela de Conciliação Bancária.
