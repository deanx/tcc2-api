from sqlalchemy.orm import Session

import models, sql_models

def save_questionario(db: Session, questionario: sql_models.QuestionarioCreate):
    db_questionario = models.Questionario(**questionario.dict())
    db.add(db_questionario)
    print(db_questionario)
    db.commit()
    db.refresh(db_questionario)
    return db_questionario

def save_post(db: Session, post: sql_models.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    print(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post