from fastapi import APIRouter
from fastapi import HTTPException
from app.schemas.users import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = []

@router.get("/")
def get_users():
    return users

@router.get("/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code = 404,
        detail= f"User with id {user_id} not found"
    )

@router.post("/")
def create_user(user: UserCreate):
    users.append(
        {
            "id": len(users) + 1,
            "username": user.username,
            "email": user.email,
            "age": user.age,
            "phone_number": user.phone_number
        }
    )
    return users

@router.put("/{user_id}")
def update_user(user_id:int):
    return {"message": f"user details with user id {user_id} is updated"}

@router.delete("/{user_id}")
def delete_user(user_id:int):
    return {"message": f"user with user id {user_id} is deleted"}

