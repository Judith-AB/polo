 
from passlib.context import CryptContext  #for hashing
from jose import jwt
from datetime import datetime, timedelta, timezone
SECRET_KEY="polo-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)

def create_token(data):
    to_encode=data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
def decode_token(token):
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])  #forr decryption-expects a list