def save_kpis_to_sql(connection, kpis):
    # TODO: save extracted KPI values to Azure SQL or another database
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO kpis (revenue, profit_margin, growth_rate) VALUES (?, ?, ?)',
        (kpis.get('revenue'), kpis.get('profit_margin'), kpis.get('growth_rate'))
    )
    connection.commit()
