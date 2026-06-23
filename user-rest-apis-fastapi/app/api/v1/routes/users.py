from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = []

@router.get("/")
def get_users():
    return {"message": "All users"}


@router.get("/{student_id}")
def get_user(student_id:int):
    return {"message": f"Details of student with student id : {student_id}"}

@router.post("/")
def create_user():
    return {"message": "user with is created"}

@router.put("/{student_id}")
def update_user(student_id:int):
    return {"message": f"Student details with student id {student_id} is updated"}

@router.delete("/{student_id}")
def delete_user(student_id:int):
    return {"message": f"Student with student id {student_id} is deleted"}

