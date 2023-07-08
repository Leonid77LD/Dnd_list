import ast  # Абстрактные синтаксические деревья
import time
import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from apiDndServices.db_table.slclass import Slclass
from app.apiDndServices.models.slclass import Api5EDndClass
from database import get_async_session

from requests import get

router = APIRouter(
    prefix="/slclass",
    tags=["Class"]
)


@router.get('/all_classes_5e')
async def test_dnd_api(db: AsyncSession = Depends(get_async_session)):
    classes = get('https://www.dnd5eapi.co/api/classes/')
    print(classes.text)
    print(db)
    if classes.status_code == 200:
        content = ast.literal_eval(classes.text)  # converting string into dictionary
        print(content)
        for i in content['results']:
            stmt = insert(Slclass), [{
                'cdclass': uuid.uuid4(),
                'index': i['index'],
                'full_nmclass': i['name'],
                'url': i['url'],
            }]
            res = db.execute(stmt)
            db.commit()
            print(res)
    return True, res


@router.get('/select_orm')
async def _select(db: AsyncSession = Depends(get_async_session)):
    stmt = select(Slclass)
    res = await db.execute(stmt)
    res = res.all()
    res_list = []
    for qwe in res:
        print(qwe)
        res_list.append(qwe[0].as_dict())

    return True, res_list

@router.get('/insert_text')
async def _insert(db: AsyncSession = Depends(get_async_session)):
    tmp = uuid.uuid4()
    stmt = f""" Insert into slclass (cdclass, nmclass) values ('{tmp}'::uuid, 'test'); """
    await db.execute(text(stmt))
    await db.commit()
    return True, 'object add'

@router.get('/insert_orm')
async def _insert_orm(db: AsyncSession = Depends(get_async_session)):
    tmp = uuid.uuid4()
    stmt = insert(Slclass).values(cdclass=uuid.uuid4(), nmclass='test_orm')
    await db.execute(stmt)
    await db.commit()
    return True, 'object add'

# @router.get('/update')
# async def update(db: AsyncSession = Depends(get_async_session)):
#     classes = get('https://www.dnd5eapi.co/api/classes/')
#     print(classes.text)
#     print(db)
#     if classes.status_code == 200:
#         content = ast.literal_eval(classes.text)  # converting string into dictionary
#         print(content)
#         for i in content['results']:
#             stmt = insert(Slclass), [{
#                 'cdclass': uuid.uuid4(),
#                 'index': i['index'],
#                 'full_nmclass': i['name'],
#                 'url': i['url'],
#             }]
#             res = db.execute(stmt)
#             db.commit()
#             print(res)
#     return True, res

# @router.get('/delete')
# async def delete(db: AsyncSession = Depends(get_async_session)):
#     classes = get('https://www.dnd5eapi.co/api/classes/')
#     print(classes.text)
#     print(db)
#     if classes.status_code == 200:
#         content = ast.literal_eval(classes.text)  # converting string into dictionary
#         print(content)
#         for i in content['results']:
#             stmt = insert(Slclass), [{
#                 'cdclass': uuid.uuid4(),
#                 'index': i['index'],
#                 'full_nmclass': i['name'],
#                 'url': i['url'],
#             }]
#             res = db.execute(stmt)
#             db.commit()
#             print(res)
#     return True, res


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
