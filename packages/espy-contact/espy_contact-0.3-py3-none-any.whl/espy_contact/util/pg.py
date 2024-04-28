from typing import Type
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

def add_model(model_class: Type, db: Session, **kwargs) -> bool:
    try:
        new_model = model_class(**kwargs)
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
        return True
    except IntegrityError:
        db.rollback()
        return False
def update_model(model_class: Type, db: Session, id: int, **kwargs) -> bool:
    try:
        model = db.query(model_class).filter_by(id=id).first()
        if model:
            for key, value in kwargs.items():
                setattr(model, key, value)
            db.commit()
            return True
        return False
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return False

def get_model(model_class: Type, db: Session, id: int) -> object:
    return db.query(model_class).filter_by(id=id).first()

def get_all_models(model_class: Type, db: Session) -> list:
    return db.query(model_class).all()

def delete_model(model_class: Type, db: Session, id: int) -> bool:
    try:
        model = db.query(model_class).filter_by(id=id).first()
        if model:
            db.delete(model)
            db.commit()
            return True
        return False
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return False