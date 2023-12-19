from fastapi import APIRouter
from .. import models, schemas, oauth2
from fastapi import Depends, status, Response, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from ..utility import scrapper, mcq_gen
import asyncio

router = APIRouter(
    prefix="/gen_mcq",
    tags=["gen_mcq"],
)




@router.post("/url")
async def get_posts(
    url: schemas.URL,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user.access_count > 0:
        data = scrapper.scrape_web_content(url.url)

        mcqs = await (mcq_gen.generate(data))
        user.access_count -= 1
        db.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return mcqs


@router.post("/text")
async def get_posts(
    data: schemas.TextData,
    db: Session = Depends(get_db),
    user_id: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user.access_count > 0:
        data = data.data
        data = data.split()
        mcqs = await mcq_gen.generate(data)  # Use await here
        user.access_count -= 1
        db.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return mcqs