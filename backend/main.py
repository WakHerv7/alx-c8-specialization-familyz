from app import app, db

def init_db():
    db.init_app(app)
    db.app = app
    with app.app_context():
        db.create_all()

if __name__ ==  '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=8100)