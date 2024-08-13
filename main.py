from fastapi import FastAPI, Depends, UploadFile, Form, Request
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sql_models import QuestionarioCreate, PostCreate
from crud_helper import save_questionario, save_post
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import boto3
import os
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/questionario")
def questionario(questionario: QuestionarioCreate, db:Session = Depends(get_db)):
    save_questionario(db, questionario)
    return "saved"

@app.post("/post")
def post(post: PostCreate, db:Session = Depends(get_db)):
    save_post(db, post)
    return "saved"

@app.post("/upload-picture")
async def upload(content: Request):
    async with content.form() as form:
      filename = form["filename"]
      contents :str = form["blobs"]
      contents = contents.replace("data:image/png;base64,","",1)
      image_bytes = base64.b64decode(contents)
      with open(filename, "wb") as new_image:
          new_image.write(image_bytes)
          print("salvo em disco ", filename)
      session = boto3.Session(aws_access_key_id=os.environ["aws_access_key_id"], aws_secret_access_key=os.environ["aws_secret_access_key"])
      s3 = session.client('s3')
      s3.put_object(Body=image_bytes, Bucket="lemonstudio-images-oregon-tcc2", Key=filename)
      print("salvo no s3 ", filename)