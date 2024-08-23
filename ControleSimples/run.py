from app import app
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Use "controlesimples" como host, que está mapeado para 127.0.0.1 no arquivo hosts
    app.run(host="localhost", port=port, debug=True)
