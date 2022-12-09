# In this versio we are gonna work with email to password reset
from demo import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)