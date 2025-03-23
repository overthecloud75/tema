from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
import time

from domain.main import main_router
from domain.user import user_router
from configs import PROJECT_NAME, logger
from utils import get_access_logging, should_run_middleware, get_current_user

app = FastAPI()
app.include_router(main_router.router)
app.include_router(user_router.router)

openapi_schema = get_openapi(
        title=PROJECT_NAME,
        version='1.0.0',
        description=f'{PROJECT_NAME} API Description',
        routes=app.routes,
    )
    
# Security 스키마 추가
openapi_schema['components']['securitySchemes'] = {
    'Bearer': {
        'type': 'http',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
    }
}

# 모든 엔드포인트에 security 요구사항 추가
openapi_schema['security'] = [
    {'Bearer': []}
]
    
app.openapi_schema = openapi_schema

# 미들웨어를 사용하여 요청/응답 로깅
@app.middleware('http')
async def log_requests(request: Request, call_next):

    start_time = time.time()

    if not await should_run_middleware(request):
        try :
            response = await call_next(request)
            get_access_logging(start_time, request, response)
        except Exception as e:
            logger.error(e)
            response = JSONResponse(
                status_code=500,
                content={'message': 'Internal Server Error'}
            )
            response.headers['authorization'] = 'Bearer'
            get_access_logging(start_time, request, response)
        return response

    try: 
        request.state.user = get_current_user(request) # request에 user 정보 추가 
    except Exception as e:
        logger.error(e)
        response = JSONResponse(
            status_code=401,
            content={'message': 'Could not validate credentials'}
        )
        response.headers['authorization'] = 'Bearer'
    else:
        response = await call_next(request)
    get_access_logging(start_time, request, response)
    return response



