from sqlalchemy import text

from database.postgres_sql import get_engine


def save_metrics(
    company: str,
    year: int,
    metrics: dict
) -> None:
    """
    Save extracted financial metrics to PostgreSQL.

    Args:
        company: Company name.
        year: Fiscal year.
        metrics: Extracted KPI dictionary.
    """
    engine = get_engine()

    query = """
    INSERT INTO financial_metrics (
        company,
        year,
        revenue,
        net_income,
        operating_income,
        cash_flow,
        total_assets,
        total_liabilities,
        risk_factors,
        growth_drivers
    )
    VALUES (
        :company,
        :year,
        :revenue,
        :net_income,
        :operating_income,
        :cash_flow,
        :total_assets,
        :total_liabilities,
        :risk_factors,
        :growth_drivers
    )
    """

    # Use both capitalized and lower‑case keys from the extraction model
    params = {
        "company": company,
        "year": str(year),
        "revenue": metrics.get("Revenue") or metrics.get("revenue"),
        "net_income": metrics.get("Net Income") or metrics.get("net_income"),
        "operating_income": metrics.get("Operating Income") or metrics.get("operating_income"),
        "cash_flow": metrics.get("Cash Flow from Operating Activities") or metrics.get("cash_flow"),
        "total_assets": metrics.get("Total Assets") or metrics.get("total_assets"),
        "total_liabilities": metrics.get("Total Liabilities") or metrics.get("total_liabilities"),
        "risk_factors": "\n".join(metrics.get("Top Risk Factors", []) or metrics.get("risk_factors", [])),
        "growth_drivers": "\n".join(metrics.get("Top Growth Drivers", []) or metrics.get("growth_drivers", []))
    }

    with engine.begin() as connection:
        connection.execute(text(query), params)

    print(
        f"Successfully saved metrics for {company} {year}"
    )

if __name__ == "__main__":
    sample_metrics = {
        "Revenue": "$391,035",
        "Net Income": "$93,736",
        "Operating Income": "$123,216",
        "Cash Flow from Operating Activities": "$118,254",
        "Total Assets": "$364,980",
        "Total Liabilities": "$308,030",
        "Top Risk Factors": [
            'Macroeconomic conditions including inflation, interest rates, and currency fluctuations could materially impact results.',
            'High competition with aggressive pricing, short product life cycles, and rapid technological changes.',
            'Dependence on single or limited sources for certain components, with potential supply shortages.',
            'Exposure to foreign exchange rate fluctuations impacting sales and margins.',
            'Legal and regulatory challenges, including significant tax disputes such as the State Aid Decision.'
        ],
        "Top Growth Drivers": [
            'Increased Services revenue from advertising, App Store, and cloud services.',
            'Higher Mac sales driven by increased laptop demand.',
            'Continued strong iPhone sales performance.',
            'Ingest your first company financial statement (e.g., 10-K, 10-Q reports in PDF format) using the sidebar uploader.',
            'Our AI engine will parse the financial metrics, risks, and growth drivers.',
            '<button id="refreshBtn" class="refresh-button" title="Refresh data"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 4V1L8 5l4 4V6c3.31 0 6 2.69 6 6a6 6 0 01-5.65 5.99L12 18a6 6 0 01-5.99-5.65L6 12H4a8 8 0 0016 0c0-4.42-3.58-8-8-8z"/></svg></button>t capital return program.'
        ]
    }

    save_metrics(
        company="Apple",
        year=2024,
        metrics=sample_metrics
    )