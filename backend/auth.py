from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import session
from database import get_db
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt,JWTError


SECRET_KEY = "replace-this-with-a-long-random-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Converts plain-text password into hash password
def hash_password(password:str)->str:
    return pwd_context.hash(password)

# Checking whether the entered password matches the hash password
def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

# Creating JWT Access token
def create_access_token(data:dict)->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES )
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt

# Extracting the bearer token from the request
#outh2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db:session=Depends(get_db)):
    token = credentials.credentials
    
    # Error Handling
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    
        # Extracting the user_id from from the request
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Finding the user in the database
    import crud # CRUD was imported here to prevent circular import
    user = crud.get_user_by_id(db,(user_id))
    if user is None:
        raise credential_exception
    return user