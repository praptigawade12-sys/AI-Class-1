def study_plan(subjects,hrs):
    plan = {}
    time_per_sub = hrs/len(subjects)

    for s in subjects:
        plan[s] = round(time_per_sub,2)

def main():
    print("========== AI Study Planner ==========")
    subjects = []
    print("Enter your subjets(type 'done' to finish):")
    while True:
        sub = input("Subjects: ").strip()
        if sub.lower() == 'done':
            break
        if sub != "":
            subjects.append(sub)

    if not subjects:
        print("No subjects entered. Exiting")
        return

    hrs = float(input("\nHow many hours can you study today:"))

    plan = study_plan(subjects,hrs)

    print("\n---- Your AI-Genrated Study Plan ----")
    for subjects,h in plan.items():
        print(f" - {subjects} : {hrs} hours")

    print("\nTip : Take a 5-10 min break after every session!")
    print("All tha best with your studies!")

main()