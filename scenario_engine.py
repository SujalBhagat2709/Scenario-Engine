import json
import os
import time


class ScenarioEngine:

    def __init__(self):

        self.file = "scenarios.json"

        self.scenarios = {}

        self.load()

    def load(self):

        if os.path.exists(self.file):

            with open(

                self.file,

                "r",

                encoding="utf-8"

            ) as file:

                self.scenarios = json.load(file)

    def save(self):

        with open(

            self.file,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.scenarios,

                file,

                indent=4

            )

    def create_scenario(self):

        print("\nCreate Scenario")

        name = input("Scenario Name: ")

        if name in self.scenarios:

            print("\nScenario already exists.")

            return

        steps = []

        print(

            "\nEnter steps."

        )

        print(

            "Type 'done' when finished.\n"

        )

        while True:

            step = input(

                f"Step {len(steps)+1}: "

            )

            if step.lower() == "done":

                break

            steps.append(step)

        self.scenarios[name] = steps

        self.save()

        print(

            "\nScenario Saved."

        )

    def show_scenarios(self):

        if not self.scenarios:

            print(

                "\nNo scenarios available."

            )

            return

        print(

            "\nAvailable Scenarios\n"

        )

        for name in self.scenarios:

            print("-", name)

    def execute_scenario(self):

        if not self.scenarios:

            print(

                "\nNo scenarios found."

            )

            return

        self.show_scenarios()

        name = input(

            "\nScenario Name: "

        )

        if name not in self.scenarios:

            print(

                "\nScenario not found."

            )

            return

        print(

            "\nExecuting...\n"

        )

        for number, step in enumerate(

            self.scenarios[name],

            start=1

        ):

            print(

                f"[{number}] {step}"

            )

            time.sleep(1)

        print(

            "\nScenario Completed."

        )

    def delete_scenario(self):

        self.show_scenarios()

        name = input(

            "\nDelete Scenario: "

        )

        if name in self.scenarios:

            del self.scenarios[name]

            self.save()

            print(

                "\nScenario Deleted."

            )

        else:

            print(

                "\nScenario Not Found."

            )