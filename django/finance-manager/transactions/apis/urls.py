from typing import List

from ninja import NinjaAPI

from transactions.apis.schemas import TransactionSchemaIn, TransactionSchemaOut
from transactions.models import Transaction

api = NinjaAPI()


@api.get('/transactions', response=List[TransactionSchemaOut])
def transactions_list(request):
    return Transaction.objects.all()


@api.get('/transactions/{item_id}')
def transaction_detail(request, item_id):
    return {'item_id': item_id}


@api.post('/transactions', response=TransactionSchemaOut)
def transaction_create(request, payload: TransactionSchemaIn):
    return Transaction.objects.create(**payload.dict())
