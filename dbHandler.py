from .dbCreator import session,ToDo
obj = ToDo

def read():
  return session.query(obj).order_by(obj.time.asc()).all()

def add_task(obj):
  try:
    session.add(obj)
    session.commit()

    return True
  except Exception as e:
    return(str(e))