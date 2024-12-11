from fastapi import FastAPI, UploadFile, Form, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from fastapi.security import APIKeyHeader


con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

# 구동시 SQL Lite 테이블 생성
cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                image BLOB,
                price INTEGER NOT NULL,
                description TEXT ,
                place TEXT NOT NULL,
                insertAt INTEGER NOT NULL
            );
            """)
app = FastAPI()
SECRET = "super-coding"
manager = LoginManager(SECRET, '/login')
api_key_header = APIKeyHeader(name="Authorization")


@manager.user_loader()
def query_user(data):
    WHERE_STATEMENT = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENT = f'''id="{data['id']}"'''
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute(f"""
                      SELECT * from users WHERE {WHERE_STATEMENT}
                      """).fetchone()
    return user


@app.post('/login')
def login(id: Annotated[str, Form()],
          password: Annotated[str, Form()]):
    user = query_user(id)
    # print(user)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(data={
        'sub': {
            'id': user['id'],
            'name': user['name'],
            'email': user['email']
        }
    })
    return {'access_token': access_token}


@app.post('/signup')
def signup(id: Annotated[str, Form()],
           password: Annotated[str, Form()],
           name: Annotated[str, Form()],
           email: Annotated[str, Form()]):
    cur.execute(f"""
                    INSERT INTO users(id,name,email,password)
                    VALUES ('{id}','{name}','{email}','{password}')
                    """)
    con.commit()
    return '200'


@app.post("/items")
async def create_item(
    #   image : UploadFile,
    #   title : Annotated[str, Form()],
    #   price : Annotated[int, Form()],
    #   description : Annotated[str, Form()],
    #   place : Annotated[str, Form()],
    request: Request
):
    try:
        # FormData 객체 가져오기
        form_data = await request.form()

        # # 데이터 추출
        image = form_data.get("image")  # UploadFile 객체
        title = form_data.get("title")  # 텍스트 데이터
        price = form_data.get("price")
        description = form_data.get("description")
        place = form_data.get("place")
        insertAt = form_data.get("insertAt")

        # 출력 (디버깅)
        # print("Image:", image.filename)  # 파일 이름 출력
        # print("Title:", title)
        # print("Price:", price)
        # print("Description:", description)
        # print("Place:", place)
        image_bytes = await image.read()
        cur.execute(f"""
                    INSERT INTO
                    items (title, image, price, description, place, insertAt)
                    VALUES ('{title}', '{image_bytes.hex()}', {price},
                            '{description}', '{place}', '{insertAt}')
                    """)
        con.commit()
        # 응답으로 반환
        return '200'

    except Exception as e:
        print(str(e))


@app.get("/items")
async def get_item_list(token: str = Depends(APIKeyHeader(name="Authorization"))):
    # 컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                      SELECT * FROM items;
                      """).fetchall()

    return JSONResponse(jsonable_encoder(dict(row)for row in rows))


@app.get('/images/{item_id}')
def get_image(item_id):
    cur = con.cursor()
    image_byte = cur.execute(f"""
                            SELECT image FROM items AS item
                            WHERE item.id = {item_id}
                            """).fetchone()[0]

    return Response(content=bytes.fromhex(image_byte))


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
