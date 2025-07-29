# CS361 Milestone 1
## Project Description
# Vacation Planner – Milestone 1

This project is the implementation of **Milestone 1** for CS3
The Vacation Planner is a simple Python application that helps users choose a travel destination based on their preferences for climate, activities, and budget.

---

## Features

- **Interactive CLI**: Users provide input for climate, activities, and budget.
- **Best Fit Recommendation**: The program calculates the best matching destination based on user input.
- **Clear Output**: The selected best-fit destination is displayed to the user.
- **Inclusivity Heuristics**: All eight inclusivity heuristics are addressed in this milestone.
- **Quality Attributes**: Usability, maintainability, and performance are demonstrated.

---

## User Stories

### 1. Choose Climate
**As a user**, I want to select my preferred climate (Hot, Mild, or Cold) so that my vacation matches my comfort level.  
**Acceptance Criteria**:
- Given the program is running,
- When I select a climate option,
- Then my choice is saved and used in the destination matching.

### 2. Choose Activities
**As a user**, I want to select my preferred pace, scenery, and experience type so that my vacation aligns with my interests.  
**Acceptance Criteria**:
- Given the program is running,
- When I select my pace, scenery, and experience,
- Then my preferences are used to generate a best-fit match.

### 3. Choose Budget
**As a user**, I want to choose a budget (Low, Mid, or High) so that my recommendation fits my financi
**Acceptance Criteria**:
- Given the program is running,
- When I choose a budget,
- Then my recommendation reflects my budget level.

---

## Inclusivity Heuristics

- **IH#1 (Explain Features):** The program provides clear descriptions of each step in the console.
- **IH#2 (Set Expectations):** Each step explains the options and ensures invalid inputs fall back to a safe default.
- **IH#3 (Allow Customization):** Users can restart the planner before generating results.
- **IH#4 (Familiarity):** The interface uses standard numbered menus for input, which is familiar to most users.
- **IH#5 (Backtracking):** Users can restart the program if they want to change answers.
- **IH#6 (Clear Next Steps):** Each prompt clearly instructs what to do next.
- **IH#7 (Multiple Input Methods):** Users can input numbers or hit "Enter" for default values.
- **IH#8 (Error Prevention):** The program validates input and defaults to safe values when invalid input is provided.

---

## Quality Attributes

- **Usability:** Clear prompts, defaults, and simple menus.
- **Maintainability:** Functions are short and modular, each under 10 lines.
- **Performance:** Program loads instantly, with no noticeable delay in input or output.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/playmakerdaniel/cs361-milestone-1.git
   cd cs361-milestone-1

2. (Optional) Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows

3. Run the program: 
python main.py

Example Usage
Welcome to the Vacation Planner!
Step 1: Choose your preferred climate:
1. Hot
2. Mild
3. Cold
Enter choice (1-3): 1
You selected: Hot
...
Generating Recommendations...

Best Fit Match: Aruba
