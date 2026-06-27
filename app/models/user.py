class User(db.Model):
    # ... పాత కోడ్ ...
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # ఇక్కడ కొత్తగా ఈ లైన్ యాడ్ చేయండి
    is_premium = db.Column(db.Boolean, default=False)