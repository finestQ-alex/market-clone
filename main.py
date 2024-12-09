from fastapi import FastAPI, UploadFile, Form, Request, Depends
from fastapi.staticfiles import StaticFiles
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
SECRET = "fastapi"
api_key_header = APIKeyHeader(name="Authorization")


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
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM items')
    rows = cur.fetchall()
    res = jsonable_encoder(dict(row) for row in rows)
    return JSONResponse(res)


@app.get('/images/{item_id}')
def get_image(item_id):
    cur = con.cursor()
    image_byte = cur.execute(f"""
                            SELECT image FROM items AS item
                            WHERE item.id = {item_id}
                            """).fetchone()[0]

    return Response(content=bytes.fromhex(image_byte))


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
