# ClickMart DRF
ClickMart DRF is a e-commerce project.
Built using RESTful APIs with Django REST Framework and Frontend usinf React.js, inspired by online-shopping sites.
where users can view products, after logging in users can add products to cart, remove products from cart, proceed to purchase and can see order status and orders history from users dashboard.

## Screenshots
<img />

## Features
- User Registration
- JWT Authentication (Login / Refresh Token)
- User Profile API
- Product Listing
- Product Detail API
- Cart Management
- Add to Cart
- Update Cart Quantity
- Remove Cart Items
- Order Placement
- Order History
- Email Notification on Order Placement

## Tech Stack
### Backend
- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT Authentication

### Frontend
- React.js
- JavaScript
- CSS

## Environment Variables used in this project for DB config and production config
### .env file :
- SECRET_KEY=
- DEBUG=

#Database Settings
- DB_NAME=
- DB_USER=
- DB_PASSWORD=
- DB_HOST=
- DB_PORT=

#email sending
- EMAIL_HOST_USER=
- EMAIL_HOST_PASSWORD=

### .env.docker file :
- SECRET_KEY=
- DEBUG=
- ALLOWED_HOSTS=

#Database Settings
- DB_NAME=
- DB_USER=
- DB_PASSWORD=
- DB_HOST=
- DB_PORT=

#email sending
- EMAIL_HOST_USER=
- EMAIL_HOST_PASSWORD=

- CSRF_TRUSTED_ORIGINS=

### .env.production file :
- POSTGRES_DB=
- POSTGRES_USER=
- POSTGRES_PASSWORD=
