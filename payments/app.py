
# from flask import app

from functions.intex_setFastApi import root,app
import os
import uvicorn
app
if __name__ == "__main__":
    # រត់លើ host 0.0.0.0 ដើម្បីឱ្យ Flutter ភ្ជាប់បានតាម IP Laptop
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv('PORT'), reload=True)

