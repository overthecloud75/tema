async def should_run_middleware(request) -> bool:
    """미들웨어의 실행 여부를 결정
    """
    path = request.url.path
    if (path.startswith('/login')
            or path.startswith('/register')
            or path.startswith('/docs')
            or path.startswith('/openapi.json')
        ) or (
            path == '/' 
            or path == '/favicon.ico'    
        ):
        return False
    return True

