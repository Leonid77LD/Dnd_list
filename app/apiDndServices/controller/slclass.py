import ast  # Абстрактные синтаксические деревья
import time
import uuid

from fastapi import APIRouter
from app.apiDndServices.models.slclass import Api5EDndClass

router = APIRouter(
    prefix="/slclass",
    tags=["Class"]
)


@router.get('/all_classes_5e')
def test_dnd_api():
    res = Api5EDndClass().get_all_classes_5e()
    return True, res


# @router.get("")
# async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
#     try:
#         query = select(operation).where(operation.c.type == operation_type)
#         result = await session.execute(query)
#         return {
#             "status": "success",
#             "data": result.all(),
#             "details": None
#         }
#     except Exception:
#         # Передать ошибку разработчикам
#         raise HTTPException(status_code=500, detail={
#             "status": "error",
#             "data": None,
#             "details": None
#         })
#
