class Goal:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.progress = 0

    def update_progress(self, amount):
        self.progress += amount

class DailyPlanner:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def show_goals(self):
        for goal in self.goals:
            print(f"Goal: {goal.name} | Priority: {goal.priority} | Progress: {goal.progress}%")


planner = DailyPlanner()

goal1 = Goal("1", 1)
goal2 = Goal("2", 2)

planner.add_goal(goal1)
planner.add_goal(goal2)

goal1.update_progress(30)
goal2.update_progress(20)

planner.show_goals()
