from scenario_engine import ScenarioEngine


class ScenarioApp:

    def __init__(self):

        self.engine = ScenarioEngine()

    def menu(self):

        while True:

            print("\n")

            print("=" * 35)

            print("      SCENARIO ENGINE")

            print("=" * 35)

            print("1. Create Scenario")

            print("2. Execute Scenario")

            print("3. View Scenarios")

            print("4. Delete Scenario")

            print("5. Exit")

            choice = input(

                "\nEnter Choice: "

            )

            if choice == "1":

                self.engine.create_scenario()

            elif choice == "2":

                self.engine.execute_scenario()

            elif choice == "3":

                self.engine.show_scenarios()

            elif choice == "4":

                self.engine.delete_scenario()

            elif choice == "5":

                print(

                    "\nThank You!"

                )

                break

            else:

                print(

                    "\nInvalid Choice"

                )


if __name__ == "__main__":

    app = ScenarioApp()

    app.menu()