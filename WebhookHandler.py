from fastapi import FastAPI

api = FastAPI()
print("Sadness")

@api.post("/webhook/bitbucket")
async def bitbucket(request):
    print("Got request from bitbucket: {}".format(request))

@api.post("/webhook/teams")
async def teams(request):
    print("Got request from teams: {}".format(request))