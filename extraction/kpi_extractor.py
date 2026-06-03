from pydantic import BaseModel


class FinancialMetrics(BaseModel):
    company: str
    year: int

    revenue: str | None = None
    net_income: str | None = None
    operating_income: str | None = None
    cash_flow: str | None = None
    total_debt: str | None = None