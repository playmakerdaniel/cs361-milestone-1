def select_climate():
    print("Step 1: Choose your preferred climate:")
    print("1. Hot\n2. Mild\n3. Cold")
    choice = input("Enter choice (1-3): ").strip()
    if choice == "1":
        print("You selected: Hot")
        return "Hot"
    elif choice == "2":
        print("You selected: Mild")
        return "Mild"
    elif choice == "3":
        print("You selected: Cold")
        return "Cold"
    else:
        print("Invalid input, defaulting to Mild.")
        return "Mild"

def select_activities():
    print("Step 2: Choose your activity preferences:")

    print("Pace:")
    print("1. Relaxing\n2. Balanced\n3. Fast-Paced")
    pace_input = input("Enter choice (1-3): ").strip()
    pace = {"1": "Relaxing", "2": "Balanced", "3": "Fast-Paced"}.get(pace_input, "Balanced")

    print("Scenery:")
    print("1. Beach\n2. Mountains\n3. Urban")
    scenery_input = input("Enter choice (1-3): ").strip()
    scenery = {"1": "Beach", "2": "Mountains", "3": "Urban"}.get(scenery_input, "Beach")

    print("Experience:")
    print("1. Cultural & Historic\n2. Adventure & Outdoors\n3. Food & Nightlife")
    experience_input = input("Enter choice (1-3): ").strip()
    experience = {"1": "Cultural & Historic", "2": "Adventure & Outdoors", "3": "Food & Nightlife"}.get(experience_input, "Cultural & Historic")

    print(f"Your preferences are: {pace}, {scenery}, {experience}")
    return pace, scenery, experience

def select_budget():
    print("Step 3: Choose your budget:")
    print("1. Low\n2. Mid\n3. High")
    choice = input("Enter choice (1-3): ").strip()
    if choice == "1":
        print("Selected budget: Low")
        return "Low"
    elif choice == "2":
        print("Selected budget: Mid")
        return "Mid"
    elif choice == "3":
        print("Selected budget: High")
        return "High"
    else:
        print("Invalid input, defaulting to Mid.")
        return "Mid"

def generate_recommendations(climate, activities, budget):
    destinations = [
        {"location": "Aruba", "climate": "Hot", "pace": "Relaxing", "scenery": "Beach", "experience": "Food & Nightlife", "budget": "High"},
        {"location": "Miami, Florida", "climate": "Hot", "pace": "Balanced", "scenery": "Beach", "experience": "Food & Nightlife", "budget": "Mid"},
        {"location": "Dubai, UAE", "climate": "Hot", "pace": "Fast-Paced", "scenery": "Urban", "experience": "Cultural & Historic", "budget": "High"},

        {"location": "San Diego, California", "climate": "Mild", "pace": "Relaxing", "scenery": "Beach", "experience": "Adventure & Outdoors", "budget": "Mid"},
        {"location": "Asheville, North Carolina", "climate": "Mild", "pace": "Balanced", "scenery": "Mountains", "experience": "Adventure & Outdoors", "budget": "Mid"},
        {"location": "Barcelona, Spain", "climate": "Mild", "pace": "Fast-Paced", "scenery": "Urban", "experience": "Cultural & Historic", "budget": "High"},

        {"location": "Prague, Czech Republic", "climate": "Cold", "pace": "Relaxing", "scenery": "Urban", "experience": "Cultural & Historic", "budget": "Low"},
        {"location": "Reykjavik, Iceland", "climate": "Cold", "pace": "Balanced", "scenery": "Mountains", "experience": "Adventure & Outdoors", "budget": "Mid"},
        {"location": "Quebec City, Canada", "climate": "Cold", "pace": "Fast-Paced", "scenery": "Urban", "experience": "Food & Nightlife", "budget": "Mid"},

        {"location": "Cabo San Lucas, Mexico", "climate": "Hot", "pace": "Relaxing", "scenery": "Beach", "experience": "Adventure & Outdoors", "budget": "Mid"},
        {"location": "Tokyo, Japan", "climate": "Mild", "pace": "Fast-Paced", "scenery": "Urban", "experience": "Food & Nightlife", "budget": "High"},
        {"location": "Banff, Canada", "climate": "Cold", "pace": "Balanced", "scenery": "Mountains", "experience": "Adventure & Outdoors", "budget": "Mid"},
    ]

    best_match = None
    best_score = -1

    for d in destinations:
        score = 0
        if d["climate"] == climate:
            score += 1
        if d["pace"] == activities[0]:
            score += 1
        if d["scenery"] == activities[1]:
            score += 1
        if d["experience"] == activities[2]:
            score += 1
        if d["budget"] == budget:
            score += 1

        if score > best_score:
            best_score = score
            best_match = d["location"]

    print("\nGenerating Recommendation...\n")
    print(f"Best Fit Match: {best_match}")

def confirm_and_continue():
    confirm = input("\nYou are about to view your recommendations. Continue? (Y/N): ").strip().lower()
    if confirm != 'y':
        print("Exiting program. Goodbye!")
        exit()

def main():
    print("Welcome to the Vacation Planner!")

    while True:
        climate = select_climate()
        activities = select_activities()
        budget = select_budget()

        go_back = input("\nWould you like to restart the planner? (Y/N): ").strip().lower()
        if go_back != 'y':
            break

    confirm_and_continue()
    generate_recommendations(climate, activities, budget)

if __name__ == "__main__":
    main()


