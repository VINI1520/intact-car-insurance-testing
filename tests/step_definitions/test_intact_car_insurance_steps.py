import pytest
from pytest_bdd import scenarios, parsers, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_text_field(browser, element_id, value):
    field_element = browser.find_element(By.ID,element_id)
    field_element.send_keys(value)

def fill_select_option(browser, element_id, value):
    
    # Click on the Chosen dropdown to open it
    dropdown = browser.find_element(By.XPATH, "//div[@id='" + element_id +"']")
    dropdown.click()

    # Wait for the desired year option to be visible and clickable
    element_id_xpath = "//li[contains(@class, 'active-result') and text()='" + value + "']"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, element_id_xpath)))

    # Click on the desired year option to select it
    select_option = browser.find_element(By.XPATH, element_id_xpath)
    select_option.click()

def validate_field(browser, element_id, expected_value):
    field_value = browser.find_element(By.ID,element_id).get_attribute('value')
    assert field_value == expected_value

def validate_select_option(browser, element_id, expected_value):
    field_value = browser.find_element(By.XPATH, "//div[@id='" + element_id + "']/a/span").text
    assert field_value == expected_value

def convert_bdd_table(table):
    # Remove leading/trailing whitespaces and split the data by lines
    rows = [row.strip() for row in table.split('\n') if row.strip()]

    # Extract the header row and remove the first and last separator characters
    header_row = rows[0].strip('|').strip()
    headers = [header.strip() for header in header_row.split('|') if header.strip()]

    values_table = []

    # Iterate over the data rows and add them to values_table
    for row in rows[1:]:
        values_row = [value.strip() for value in row.strip('|').split('|') if value.strip()]
        values_table.append(values_row)

    result = []
    for row in values_table:
        entry = {}
        for i, h in enumerate(headers):
            entry[h] = row[i]
        result.append(entry)
    return(result)

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given('I am on the intact car insurance website')
def visit_example_website(browser):
    browser.get("https://apps.intact.ca/qc/quick-quote/desktop/index.html#s1")

@then('I should see the title "Quick Quote"')
def check_title(browser):
    title_label = browser.find_element(By.XPATH, "//h1[@id='step1']")
    assert "Quick Quote" in title_label.text

@then('I should see the phone number "1 844 336 5801"')
def check_phone_number(browser):
    phone_number_header = browser.find_element(By.ID,"phonenumberheader")
    assert "1 844 336 5801" in phone_number_header.text

@when('I submit the form to request an insurance quote')
def submit_empty_form(browser):
    submit_button = browser.find_element(By.ID, "getprice")
    submit_button.click()

@then('I should see error messages for the missing fields')
def check_error_messages(browser):
    year_error = browser.find_element(By.ID, "yearError")    
    assert "Please select the year of this vehicle." in year_error.text

    make_error = browser.find_element(By.ID, "makeError")    
    assert "Please select the make of this vehicle." in make_error.text

    model_error = browser.find_element(By.ID, "modelError")    
    assert "Please select the model of this vehicle." in model_error.text

    distance_workschool_error = browser.find_element(By.ID, "distanceWorkSchoolError")    
    assert "Please specify the distance, in kilometres, between the driver's place of residence and where the driver works or goes to school." in distance_workschool_error.text

    annual_km_error = browser.find_element(By.ID, "annualKmError")    
    assert "Please specify the annual kilometres for this vehicle." in annual_km_error.text

    last_name_error = browser.find_element(By.ID, "lastNameError")    
    assert "Please answer this question with at least 2 alphabetical characters." in last_name_error.text

    date_birth_year_error = browser.find_element(By.ID, "dateOfbirthYearError")    
    assert "Please enter a valid date of birth . You must be between 16 and 99 years old." in date_birth_year_error.text

    phone_number_error = browser.find_element(By.ID, "phoneNumberError")    
    assert "Please enter your 10-digit phone number, including the area code." in phone_number_error.text

    postal_code_error = browser.find_element(By.ID, "postalCodeError")    
    assert "Please answer this question." in postal_code_error.text

    first_licensed_error = browser.find_element(By.ID, "firstLicencedAtError")    
    assert "Please answer this question." in first_licensed_error.text

@when(parsers.cfparse('I fill in the following fields:\n{table}'))
def step_fill_form_fields(browser, table):
    
    result = convert_bdd_table(table)
    
    for row in result:
        value = row["Value"]
        element_id = row["Element ID"]

        if 'select' in element_id:
            fill_select_option(browser, element_id, value)
        else:
            fill_text_field(browser, element_id, value)

@then(parsers.cfparse('I validate the following fields:\n{table}'))
def step_validate_form_fields(browser, table):

    result = convert_bdd_table(table)
    
    for row in result:
        value = row["Value"]
        element_id = row["Element ID"]

        if 'select' in element_id:
            validate_select_option(browser, element_id, value)
        else:
            validate_field(browser, element_id, value)

@then('I should see a message asking to obtain the clients credit information')
def step_verify_client_credit_information_request(browser):
    client_credit_information_request_message = browser.find_element(By.ID, "SaveUp")
    assert 'You could save up to 25%* by clicking “yesˮ!' in client_credit_information_request_message.text

@then('I should see a loading indicator')
def step_verify_loading_indicator_request(browser):
    browser.implicitly_wait(10)
    loading_form = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'loading'))
    )

    # Wait for the loading form to disappear
    WebDriverWait(browser, 30).until(
        EC.invisibility_of_element(loading_form)
    )

@then('I should see a message to call a representative to continue')
def step_verify_message_call_representative(browser):
    browser.implicitly_wait(10)
    loading_form = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'step2content'))
    )