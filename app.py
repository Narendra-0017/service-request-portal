from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

# Initialize Flask app
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')

# Configure database - use DATABASE_URL environment variable if available (for Render)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///service_portal.db')
# Fix for PostgreSQL on Render (if needed)
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database Models
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    requests = db.relationship('ServiceRequest', backref='service', lazy=True)
    providers = db.relationship('ServiceProvider', backref='service', lazy=True)
    
    def __repr__(self):
        return f'<Service {self.name}>'

class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    rating = db.Column(db.Float, default=4.0)
    
    def __repr__(self):
        return f'<ServiceProvider {self.name}>'

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    urgency = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ServiceRequest {self.id}>'

# Routes
@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/service/<int:service_id>')
def service_form(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_form.html', service=service)

@app.route('/submit_request', methods=['POST'])
def submit_request():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        customer_name = request.form.get('customer_name')
        customer_email = request.form.get('customer_email')
        customer_phone = request.form.get('customer_phone')
        address = request.form.get('address')
        description = request.form.get('description')
        urgency = request.form.get('urgency')
        
        # Create new service request
        new_request = ServiceRequest(
            service_id=service_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            address=address,
            description=description,
            urgency=urgency
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        # Get a random service provider for the selected service
        provider = ServiceProvider.query.filter_by(service_id=service_id).first()
        
        return render_template('confirmation.html', request=new_request, provider=provider)

@app.route('/get_services')
def get_services():
    services = Service.query.all()
    service_list = [{'id': service.id, 'name': service.name} for service in services]
    return jsonify(service_list)

@app.route('/test')
def test():
    return render_template('test.html')

def initialize_database():
    with app.app_context():
        db.create_all()
        # Check if we need to add initial data
        if not Service.query.first():
            # Add services
            services_data = [
                {"name": "Plumbing", "description": "Water leaks, pipe repairs, installations"},
                {"name": "Electrical", "description": "Wiring, electrical repairs, installations"},
                {"name": "Carpentry", "description": "Furniture repairs, installations, woodwork"},
                {"name": "Cleaning", "description": "Home cleaning, deep cleaning services"},
                {"name": "Gardening", "description": "Garden maintenance, landscaping"},
                {"name": "Automotive", "description": "Car repair, maintenance, towing"},
                {"name": "Ambulance", "description": "Emergency medical transport"},
                {"name": "Police", "description": "Emergency law enforcement assistance"},
                {"name": "Fire Fighter", "description": "Fire emergency and rescue services"}
            ]
            
            for service_data in services_data:
                service = Service(name=service_data["name"], description=service_data["description"])
                db.session.add(service)
            
            # Add sample providers for each service
            services = Service.query.all()
            for service in services:
                provider = ServiceProvider(
                    name=f"{service.name} Provider",
                    service_id=service.id,
                    phone="+91 98765 43210",
                    email=f"{service.name.lower().replace(' ', '')}@example.com",
                    address="123 Main St, Mumbai, India",
                    rating=4.5
                )
                db.session.add(provider)
            
            db.session.commit()
            print("Database initialized with sample data!")

# Create database tables within application context
with app.app_context():
    db.create_all()

# Initialize the database with sample data
initialize_database()

if __name__ == '__main__':
    # Use this for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 