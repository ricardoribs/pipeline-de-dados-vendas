-- models/faturamento_por_estado.sql

SELECT
    estado_cliente,
    SUM(preco_produto * quantidade) AS faturamento_total
FROM
    {{ source('main', 'vendas') }} -- Diz ao dbt para usar a tabela 'vendas' do nosso banco
GROUP BY
    estado_cliente
ORDER BY
    faturamento_total DESC