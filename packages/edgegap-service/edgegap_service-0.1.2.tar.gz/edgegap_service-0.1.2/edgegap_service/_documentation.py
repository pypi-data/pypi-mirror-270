from fastapi import FastAPI, templating, Request, responses


class DocumentationRoute:
    @staticmethod
    def init_documentation(app: FastAPI, templates: templating.Jinja2Templates):
        @app.get("/", response_class=responses.HTMLResponse, include_in_schema=False)
        async def root(request: Request):
            urls = {
                "Docs": f"{request.base_url}docs",
                "Redoc": f"{request.base_url}redoc",
            }

            return templates.TemplateResponse(
                name="index.html",
                context={
                    "request": request,
                    "urls": urls,
                    "title": getattr(app, 'title')
                }
            )
