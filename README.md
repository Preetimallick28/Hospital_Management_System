A Django + Python-based web application designed to streamline hospital operations by managing Patients, Doctors, and Appointments with role-based access control for Management Staff and Doctors.

👥 User Roles
1. Management / Staff
Responsibilities:

➕ Add Patients (Doctor assigned via ForeignKey).

✏ CRUD Operations on Patients (Create, Read, Update, Delete).

📅 Add Appointments (Patient & Doctor as ForeignKeys).

✏ CRUD Operations on Appointments.

📊 Admin Dashboard: View real-time counts of Doctors, Patients, and Appointments.

👤 Profile Management: Update profile, reset password, and logout.

🔍 Search Functionality: Search patients and appointments instantly.

2. Doctor
Responsibilities:

🔐 Access restricted to their own assigned Patients and Appointments only.

📄 View Patients: With options to update, delete, and search.

📅 View Appointments: With options to update, delete, and search.

👤 Profile Management: Update profile and reset password.

🔑 Key Features
Role-based Authentication & Authorization (Django’s built-in auth system).

Doctor-specific data visibility — One doctor cannot see another doctor’s patients or appointments.

Search Functionality for quick record access.

Responsive Dashboard for both Admin and Doctor roles.

Secure Access Control — No unauthorized access before login.

🖥️ Tech Stack
Backend: Python, Django

Frontend: HTML, CSS, Bootstrap, JavaScript

Database: MySQL

Authentication: Django’s built-in auth system with role differentiation



📌 Benefits of Separating Roles
🎯 Clarity: Each Doctor views only their patients & appointments — no data overlap.

🔒 Security: Patient data is visible only to authorized personnel.

⚡ Efficiency: Staff and doctors work independently without confusion.

This system ensures smooth hospital operations, maintains data security, and improves efficiency in managing patients and appointments.
