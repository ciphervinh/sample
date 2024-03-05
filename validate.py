from fastapi import FastAPI, Request, Body
from os import environ

app = FastAPI()

label = environ.get('LABEL', 'development')

@app.post("/validate")
async def validating_webhook(request: dict = Body(...)):
    uid = request["request"].get("uid")

    print(f"got request {uid}")
    print(request)

    # Do anything we want with the request, body
    # if we return false, the request is reject, the pod stuck in pending
    return admission_response(True, uid, f"pod is ok")

def admission_response(allowed, uid, message):
    return {"apiVersion": "admission.k8s.io/v1",
                    "kind": "AdmissionReview",
                    "response":
                        {"allowed": allowed,
                         "uid": uid,
                         "status": {"message": message}
                         }
                    }
