🧠 Job Board API

A full-featured **Job Board REST API** built with **Django & Django REST Framework** that allows employers to post jobs and job seekers to apply. The project demonstrates modern API development with role-based authentication, file uploads, pagination, token refresh, and more.


🚀 Features

- 👤 **User Registration & Login** with JWT Authentication
- 🔐 Role-based Access Control (Employer & Job Seeker)
- 📄 CRUD for Jobs, Users, and Applications using `APIView`
- 📎 Resume Upload (PDF-only)
- 📬 Job Application Flow with Status Tracking
- 🔁 JWT Refresh & Logout (Blacklist)
- 📃 Paginated Results for Jobs & Applications
- 🔒 Secure with CORS, Throttling & HTTPS Enforcement
- 📘 Auto-generated Swagger Documentation


🛠️ Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Auth**: JWT (Simple JWT)
- **DB**: PostgreSQL (locally SQLite)
- **Docs**: Swagger (drf-yasg)
- **Deployment**: Render (or AWS/DigitalOcean)
- **Security**: CORS, HTTPS, Throttling

---

🔧 Installation & Setup

 1. Clone the repo
```bash
git clone https://github.com/yourusername/job-board-api.git
cd job-board-api
```

2. Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables (optional `.env`)
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
python manage.py runserver
```

---

🧪 API Endpoints

✅ Authentication
- `POST /api/register/` - Register (Employer or Job Seeker)
- `POST /api/login/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `POST /api/logout/` - Logout & blacklist token

 🧑‍💼 Jobs (Employer)
- `GET /api/jobs/` - List all jobs (paginated)
- `POST /api/jobs/` - Create job
- `PUT /api/jobs/<id>/` - Update job
- `DELETE /api/jobs/<id>/` - Delete job

👨‍🎓 Applications (Job Seeker)
- `POST /api/jobs/<job_id>/apply/` - Apply for a job
- `GET /api/applications/` - Employer: View applicants
- `GET /api/applications/<id>/` - View application details
- `PUT /api/applications/<id>/` - Employer: Change status

📘 Docs
- Swagger UI: `/swagger/`


---

🧳 Resume Uploads

- Uploads are limited to **PDF only**
- Files are saved to `media/resumes/`

---

 🚀 Deployment

Deployed using [Render](https://render.com), with Gunicorn and Whitenoise for static serving. PostgreSQL used in production.

---

✨ Screenshots (Optional)

Include Postman screenshots or Swagger UI examples here to show off your endpoints.

---


## 🙋‍♂️ Author

Built by [Dennis Kofi Smith](https://github.com/denniskofismith)

```

---
