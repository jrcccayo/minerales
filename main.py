
if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))  # Usa 8000 como puerto por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)

asgi_app = app

