# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

patients = {
"Grant": "tommorow at 3",
"Ritch" : "tonight after Lancaster ai"
}

class ActionNextAppointment(Action):

    def name(self) -> Text:
        return "action_next_Appointment"

    def run(self, dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

                 name = tracker.get_slot('name')

                 if patients[name] == None:
                     dispatcher.utter_message("You don't have any")
                 else:
                    dispatcher.utter_message("Your next apoitment is " + str(patients[name]))

                 return []
