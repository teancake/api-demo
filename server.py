from fastapi import FastAPI
from some_model import SomeModel, Feature
import uvicorn

from pydantic import BaseModel


# somehow pydantic model has to be used with post parameters
# otherwise 422 error would occur
class Request(BaseModel):
    width: int
    height: int
    name: str


class Response:
    @staticmethod
    def build_succ_response(score):
        return '{"success":%s, "errorCode":"SUCC", "errorMsg":"ok", "data":{"score":%f}}' % ("true", score)

    @staticmethod
    def build_failed_response(score):
        return '{"success":%s, "errorCode":"SOME_ERROR_CODE", "errorMsg":"error occurred, the reason is ...", "data":{"score":%f}}' % (
            "false", score)


app = FastAPI()

model = SomeModel()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(request: Request):
    print("request {}".format(request))
    feature = Feature.obtain_feature(request.width, request.height, request.name)
    score = model.infer(feature)
    if score > 0:
        return Response.build_succ_response(score)
    else:
        return Response.build_failed_response(score)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
