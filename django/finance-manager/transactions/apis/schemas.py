from ninja import Schema


class TransactionSchemaIn(Schema):
    user_id: int
    amount: float
    is_revenue: bool
    revenue_type: str = None
    expenses_type: str = None
    description: str = None


class TransactionSchemaOut(Schema):
    id: int
    amount: str
    is_revenue: bool
    revenue_type: str = None
    expenses_type: str = None
    description: str = None

    def resolve_amount(self, obj):
        return f'{"+" if self.is_revenue else "-"}{obj.amount:,.2f}'
