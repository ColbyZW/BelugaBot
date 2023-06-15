from fastapi import FastAPI

api = FastAPI()

@api.post("/webhook/bitbucket")
async def bitbucket(request):
    print(request)

@api.post("/webhook/teams")
async def teams(request):
    print(request)