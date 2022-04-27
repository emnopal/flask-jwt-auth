from docs import app

if __name__ == '__main__':
    HOST = app.config.get('APP_HOST')
    PORT = app.config.get('APP_PORT')
    DEBUG = app.config.get('DEBUG')
    app.run(host=HOST, port=PORT, debug=DEBUG)
