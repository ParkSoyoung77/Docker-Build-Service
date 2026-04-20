import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 현재 파일(main.py)의 위치를 기준으로 templates 폴더 경로를 잡습니다.
current_dir = os.path.dirname(os.path.realpath(__file__))
templates_path = os.path.join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    k8s_data = {
        "title": "Kubernetes Navigation",
        "subtitle": "컨테이너 오케스트레이션의 바다를 항해하다",
        "sections": [
            {"id": "arch", "title": "Cluster Architecture", "desc": "Control Plane & Worker Node"},
            {"id": "object", "title": "K8s Objects", "desc": "Pod, Service, Deployment"},
            {"id": "network", "title": "Networking", "desc": "Ingress & Service Mesh"},
            {"id": "storage", "title": "Storage & PV", "desc": "Persistent Volumes"}
        ]
    }
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": k8s_data}
    )

    # if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)