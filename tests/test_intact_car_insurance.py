# test_intact_car_insurance.py

from pytest_bdd import scenarios
from step_definitions.test_intact_car_insurance_steps import *

# Define the feature file(s) to be used
scenarios("../features/intact_car_insurance.feature")
