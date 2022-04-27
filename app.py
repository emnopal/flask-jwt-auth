import os
from docs import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    HOST = os.getenv('APP_URL')
    PORT = os.getenv('APP_PORT')
    if os.getenv('ENV').lower() == 'production':
        app.run(host=HOST, port=PORT, debug=False)
    else:
        app.run(host=HOST, port=PORT, debug=True)
