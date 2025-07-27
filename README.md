# Financial & Legal Case Manager

A comprehensive 3-tier web application built with Flask, PostgreSQL, and Docker to manage clients, legal cases, and complex financial transactions for a specialized firm. This project serves as a full-stack, DevOps-centric case study, from initial client briefing to a fully automated CI/CD pipeline deploying to a production VPS.

---

### Live Demo

`https://app.komocred.com.br`

*(Note: This is the live production URL for the client. The public version of this code in this repository uses anonymized business logic.)*

---

## 1. Project Overview & Business Problem

This application was developed as a real-world solution for a financial-legal firm that previously relied on manual spreadsheets to manage client cases and calculate complex, multi-party financial distributions. The manual process was time-consuming, prone to human error, and lacked security and data integrity.

The core challenge was to translate a unique set of business rules into a secure, reliable, and intuitive web application for non-technical users.

**Key Objectives:**
* **Centralize Data:** A single source of truth for clients, legal cases, and financial movements.
* **Automate Complex Calculations:** Implement specific business logic for fee distribution among clients, lawyers, partners, and the firm.
* **Ensure Security:** Protect sensitive financial data with user authentication and a secure production environment.
* **Streamline Operations:** Provide features like client search, data editing/deletion, and automated financial reporting (Excel export).
* **Automate Deployment:** Build a complete CI/CD pipeline for reliable and hands-off updates.

---

## 2. Tech Stack & Architectural Decisions

| Category                 | Technology                         | Rationale                                                                                                                                                              |
| :----------------------- | :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend** | Python, Flask, Gunicorn            | Chosen for rapid development, robustness, and alignment with existing skills. Gunicorn serves the app in production.                                                      |
| **Database** | PostgreSQL                         | Selected for its reliability, data integrity features (transactions), and robust performance.                                                                          |
| **Frontend** | HTML, Jinja2 Templates, Tailwind CSS | A Server-Side Rendering (SSR) approach was chosen to simplify the stack, reduce complexity, and ensure a clean, responsive UI without heavy JavaScript frameworks.      |
| **Infrastructure** | Docker, Docker Compose             | To ensure perfect parity between development and production environments, simplifying dependencies and deployment.                                                        |
| **Deployment** | Linux VPS (Ubuntu), Nginx          | A standard, robust production environment. Nginx acts as a high-performance reverse proxy.                                                                             |
| **Security** | Let's Encrypt (HTTPS), UFW, Tailscale  | A multi-layered security approach: SSL encryption for all traffic, a host-based firewall, and a private VPN (Tailscale) for secure administrative access.                 |
| **CI/CD** | GitHub Actions (Self-Hosted Runner)  | To create a fully automated, secure pipeline that builds and deploys the application on every push to the main branch directly inside the production server.            |

---

## 3. Core Features

* **Secure User Management:** A closed-system with a fixed set of users and a manual, admin-driven password reset mechanism for enhanced security.
* **Full CRUD Functionality:** Create, Read, Update, and Delete operations for Clients, Legal Cases, and Financial Transactions.
* **Dynamic Financial Calculator:** A core module (`calculos.py`) that accurately computes financial distributions based on the specific type of legal case.
* **Intelligent UI:** The user interface dynamically enables or disables financial transaction types based on the context of the legal case, preventing user error.
* **Batch Processing:** A tool to register recurring monthly payments (installments) in a single operation, calculating future payment dates automatically.
* **Client Search:** Fast and efficient client lookup by name or CPF.
* **Formatted Excel Reporting:** A one-click tool to export detailed financial reports for any given period, with professional formatting (currency, dates, bold headers).

---

## 4. How to Run Locally

To run this project in a local development environment, you will need Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/financial-legal-manager.git](https://github.com/your-username/financial-legal-manager.git)
    cd financial-legal-manager
    ```

2.  **Create the environment file:**
    Create a `.env` file in the root of the project. A `.env.example` file is provided to show the required variables.

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

4.  **Create the initial users:**
    In a separate terminal, run the command to populate the database with the initial user accounts defined in your `.env` file.
    ```bash
    docker-compose exec app flask create-initial-users
    ```

5.  **Access the application:**
    The application will be available at `http://localhost:5000`.
