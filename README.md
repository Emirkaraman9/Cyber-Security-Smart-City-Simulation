🏦 DigiBank - Smart City & Digital Banking Automation
DigiBank is a comprehensive simulation platform that integrates Digital Banking with Smart City Infrastructure Management. This project demonstrates a hybrid system where urban automation (IoT simulation) meets secure financial transactions (Fiat/Crypto) under a secure, monitored environment.

Designed as a university project for Cyber Security & Big Data, focusing on secure software architecture, design patterns, and real-time monitoring.

🚀 Features
🔐 1. Admin Panel (City Controller)
System Monitoring: Real-time tracking of CPU & RAM usage (simulated Server Health).

Cyber Security Module:

Attack Simulation: "Cyber Attack Alarm" triggers threaded email alerts and logs.

Defense Mechanism: "System Restore" functionality to normalize operations.

User Management: Add/Remove/Search users via Text File (TXT) and Database integration.

Automation: Control city infrastructure (e.g., Street Lights, Traffic Signals).

👤 2. User Panel (Resident)
Secure Login: Credential verification system.

Digital Wallet:

View Balance.

Money Transfer: Send Fiat currency via IBAN or Cryptocurrency (BTC/ETH).

Smart City Services:

Pay Utility Bills (Electricity, Water, Parking).

Smart Home: Trigger home automation routines (e.g., "Night Mode").

Transaction History: View personal logs and past activities.

🛠️ Technical Architecture
This project is built using Python and follows strict Object-Oriented Programming (OOP) principles. It implements several software design patterns to ensure scalability and maintainability.

🏗️ Design Patterns Used:
Singleton Pattern: Ensures a single database connection instance throughout the lifecycle.

Factory Pattern: efficient creation of User and Admin objects based on login type.

Observer Pattern: Used for the Logging System to notify the Admin and write to logs.txt upon critical events (Security Alarms).

💻 Tech Stack:
Language: Python 3.x

GUI: CustomTkinter (Modern UI) / Tkinter

Database: SQLite (Local relational DB)

System Tools: psutil (for resource monitoring), threading (for non-blocking alarms), smtplib (for email alerts).

📸 Screenshots
(You can add screenshots of your GUI here)

Place your screenshots in a folder named screenshots and link them here.
