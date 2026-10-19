# HealthFlow AI
### Agentic AI for Intelligent Hospital Appointment Scheduling

**FAAI CA-3 | Symbiosis Institute of Technology, Pune**

**Team Members**
- **Het Shah** — PRN: 25070126513
- **Mahit Turakhia** — PRN: 24070126101

---

## 1. Overview

HealthFlow AI is a domain-specific Agentic AI Proof of Concept designed to simplify hospital appointment scheduling and improve healthcare workflow efficiency.

The system uses a coordinated multi-agent workflow to process appointment requests, analyse doctor availability, identify scheduling conflicts, recommend suitable appointment slots, validate decisions, and manage appointment bookings.

Built using Python and Streamlit, the application demonstrates how agent-based automation can reduce repetitive administrative work and support more consistent scheduling decisions.

The project uses synthetic hospital data and is intended for academic demonstration purposes.

## 2. Problem Statement

Hospital appointment scheduling can involve repetitive manual tasks, including checking doctor availability, identifying occupied slots, coordinating appointment requests, and updating booking records.

These processes can lead to scheduling conflicts, inefficient use of available slots, and additional administrative effort.

HealthFlow AI addresses this challenge by introducing a structured agentic workflow that analyses requests, recommends available slots, validates scheduling decisions, and records bookings when validation succeeds.

## 3. Key Features

- **Intelligent Appointment Scheduling:** Identifies suitable appointment slots based on doctor availability and existing bookings.
- **Multi-Agent Workflow:** Coordinates planning, analysis, scheduling, and validation tasks.
- **Conflict Detection:** Identifies occupied slots and helps prevent double bookings.
- **Alternative Slot Recommendations:** Suggests another available slot when the requested option is unavailable.
- **Appointment Booking:** Records validated appointments in the application's data store.
- **Output Validation:** Checks doctor, department, slot availability, and scheduling conflicts before booking.
- **Interactive Dashboard:** Displays appointment information, doctor availability, booking status, and workflow results.
- **Synthetic Data:** Uses dummy patient IDs, doctor records, appointment histories, and schedules for safe demonstration.
- **Workflow Monitoring:** Displays agent actions, decisions, validation results, and booking outcomes.

## 4. Agent Architecture

HealthFlow AI uses the following components:

1. **Planner Agent:** Breaks an appointment request into smaller tasks and defines the execution sequence.
2. **Analysis Agent:** Examines doctor availability, appointment records, and relevant synthetic appointment history.
3. **Scheduling / Executor Agent:** Searches for available slots and recommends a suitable appointment.
4. **Critic / Validation Agent:** Checks the recommendation for scheduling conflicts and invalid assignments.
5. **Booking Service:** Rechecks availability and saves the appointment after successful validation.
6. **Streamlit Dashboard:** Displays the workflow, booking confirmation, appointment records, and updated metrics.

### Workflow

Appointment Request → Planner Agent → Analysis Agent → Executor Agent → Critic Agent → Booking Service → Updated Dashboard

If validation fails, the system should reject the recommendation and search for another suitable slot when possible.

## 5. Technology Stack

- **Programming Language:** Python
- **Frontend and Dashboard:** Streamlit
- **Data Processing:** Pandas
- **Data Storage:** Local CSV files or the persistence mechanism implemented in the application
- **Agent Workflow:** Modular Python functions and rule-based decision logic
- **Development Environment:** Visual Studio Code

The Proof of Concept does not require paid APIs. The agent workflow can operate using predefined rules and synthetic data.

## 6. Project Structure

The application is organised into modular components for data handling, agent execution, booking, and dashboard rendering.

```text
HealthFlow-AI/
├── app.py
├── agents/
│   ├── planner.py
│   ├── analysis.py
│   ├── executor.py
│   └── critic.py
├── data/
│   ├── doctors.csv
│   ├── appointments.csv
│   └── appointment_history.csv
├── utils/
│   └── data_generator.py
├── requirements.txt
└── README.md
```

The structure above represents the intended Streamlit PoC layout. Adjust it to match the actual files in the final project.

## 7. Installation and Setup

### Prerequisites

- Python 3.9 or later
- Visual Studio Code or another Python-compatible editor
- pip package manager

### Step 1: Open the project directory

```bash
cd HealthFlow-AI
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

If the dependencies are not listed in the requirements file, install the required packages:

```bash
pip install streamlit pandas
```

## 8. Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 9. Demonstration Workflow

The application can be demonstrated through the following sequence:

1. Open the HealthFlow AI dashboard.
2. Select a synthetic patient ID.
3. Choose the required department and appointment date.
4. Submit an appointment request.
5. Observe the Planner Agent create the task sequence.
6. Review the Analysis Agent's availability checks.
7. Observe the Executor Agent select a suitable slot.
8. Review the Critic Agent's validation results.
9. Confirm that a valid appointment is saved.
10. Verify the appointment ID, booking status, updated schedule, and dashboard metrics.

A second demonstration can use an occupied slot to show how the system rejects the conflict and searches for an alternative.

## 10. Testing and Validation

The following scenarios should be evaluated:

- Booking an available appointment slot.
- Rejecting an occupied slot.
- Recommending an alternative slot.
- Handling an unknown department.
- Handling a date with no available appointments.
- Rejecting an invalid recommendation.
- Preventing duplicate bookings.
- Verifying that bookings persist after application reruns.
- Checking that dashboard metrics update after booking.
- Verifying cancellation and slot release, if implemented.

Test results should be documented according to actual execution. Features that have not been tested should not be reported as successfully validated.

## 11. Limitations

- The application uses synthetic data rather than live hospital records.
- Scheduling decisions depend on the rules and constraints implemented in the Proof of Concept.
- Appointment history and no-show risk estimates are illustrative and are not clinically validated.
- The application is intended for academic demonstration, not production hospital deployment.
- Real-world use would require stronger security, authentication, privacy controls, reliable persistence, and integration with hospital systems.

## 12. Future Scope

Potential enhancements include:

- Integration with hospital appointment management systems.
- Secure staff authentication and role-based access control.
- Automated appointment reminders and notifications.
- Calendar integration and improved scheduling constraints.
- More advanced scheduling optimisation.
- Optional local language-model integration for natural-language appointment requests.
- Comprehensive automated testing and production-grade persistence.

These enhancements are future possibilities and should not be considered implemented unless they are actually developed.

## 13. Conclusion

HealthFlow AI demonstrates how a coordinated Agentic AI workflow can support hospital appointment scheduling through planning, analysis, execution, decision-making, and validation.

By combining modular Python components with an interactive Streamlit dashboard and synthetic hospital data, the project presents a practical Proof of Concept for improving routine healthcare administration workflows.

The project emphasises transparent decision-making, scheduling conflict detection, and validation before booking, illustrating how agent-based systems can assist operational processes beyond the capabilities of a basic chatbot.

---

**Project:** HealthFlow AI  
**Subject:** Foundations of Agentic Artificial Intelligence (FAAI)  
**Institution:** Symbiosis Institute of Technology, Pune  
**Team:** Het Shah and Mahit Turakhia
