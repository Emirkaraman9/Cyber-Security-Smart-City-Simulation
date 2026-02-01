# 🏦 DigiBank – Smart City & Digital Banking Automation

DigiBank is a hybrid simulation platform that integrates **Digital Banking Systems** with **Smart City Infrastructure Management**.  
The project demonstrates how urban automation (IoT simulation) can coexist with secure financial transactions (Fiat & Crypto) in a monitored and protected environment.

Developed as a university project for **Cyber Security & Big Data**, focusing on:

- Secure software architecture  
- Object-Oriented Design  
- Design Patterns  
- Real-time system monitoring  
- Attack & defense simulations  

---

## 🚀 Features

### 🔐 1. Admin Panel – City Controller

**System Monitoring**
- Real-time CPU & RAM usage tracking (Simulated Server Health)

**Cyber Security Module**
- 🚨 Attack Simulation  
  - “Cyber Attack Alarm” triggers threaded email alerts  
  - Automatic logging system  
- 🛡 Defense Mechanism  
  - “System Restore” to normalize operations  

**User Management**
- Add / Remove / Search users  
- TXT file + Database integration  

**Smart City Automation**
- Control city infrastructure  
  - Street lights  
  - Traffic signals  

---

### 👤 2. User Panel – Resident

**Secure Authentication**
- Credential verification system

**Digital Wallet**
- View balance  
- Money transfer  
  - Fiat via IBAN  
  - Cryptocurrency (BTC / ETH simulation)

**Smart City Services**
- Pay utility bills  
  - Electricity  
  - Water  
  - Parking  
- Smart Home automation  
  - Example: “Night Mode”

**Transaction History**
- Personal logs  
- Past activities  

---

## 🛠 Technical Architecture

The project is developed with **Python** following strict **Object-Oriented Programming (OOP)** principles and modular architecture.

### 🧩 Design Patterns Implemented

- **Singleton Pattern**  
  - Ensures a single database connection instance throughout the lifecycle

- **Factory Pattern**  
  - Efficient creation of User and Admin objects based on login type

- **Observer Pattern**  
  - Logging system notifies Admin and writes to logs.txt upon critical events (Security Alarms)

---

## 💻 Tech Stack

- **Language:** Python 3.x  
- **GUI:** CustomTkinter / Tkinter  
- **Database:** SQLite  
- **Monitoring:** psutil  
- **Multithreading:** threading  
- **Email Alerts:** smtplib  

---

## 📸 Screenshots

Place your screenshots inside the `/screenshots` folder and link them here.

Example structure:

/screenshots  
   ├── login.png  
   ├── admin_panel.png  
   └── user_panel.png  

---

## ⚙ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Emirkaraman9/digibank-smart-city.git
cd digibank-smart-city
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Required libraries:
- customtkinter  
- psutil  

### 3. Run the application

```bash
python main.py
```

---

## 🛡 Security & Simulation Notes

This project includes a **Defense Simulation Module**.

- The “Cyber Attack” button simulates a breach scenario  
- Used to test:
  - Logging system  
  - Notification threads  
  - System resilience  

### 🧪 Stress Testing

- A separate **Java Attack Bot** is included in `/tools`  
- Performs HTTP Flood simulation  
- Used to observe:
  - Load handling  
  - Thread stability  
  - Monitoring behavior  

---

## 🧠 Project Goals

- Demonstrate secure software design  
- Combine Smart City + FinTech concepts  
- Implement design patterns in real scenario  
- Build cyber-attack awareness  
- Practice multi-threaded architecture  

---

## 📝 License

This project was developed for **educational purposes only**.
