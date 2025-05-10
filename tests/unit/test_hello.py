from app.routes import hello

def test_read_root():
    response = hello.read_root()
    
    assert isinstance(response, dict)
    assert "message" in response
    assert response["message"] == "Hello, FastAPI!"
    assert response == {"message": "Hello, FastAPI!"}
