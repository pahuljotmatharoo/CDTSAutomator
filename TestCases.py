#Created by Pahuljot Matharoo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Currently check involves seeing if the validation message appears after clicking the accept button
#Sleeps are needed sometimes for page to just catch up

#Selecting browser function
def browser(selected):
    if (selected == 1):
        firefox = webdriver.Chrome()
        firefox.maximize_window()
        return firefox
    elif (selected == 2):
        firefox = webdriver.Firefox()
        firefox.maximize_window()
        return firefox
    elif (selected == 3):
        firefox = webdriver.Edge()
        firefox.maximize_window()
        return firefox

#Test Case 1: Creating a new contact
#Checking if it worked or not is not working currently
def TestCase1(selected,name, type):
    firefox = browser(selected)
    firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")
    # Wait for the "Material Management" button to be clickable and click it
    MaterialManagement_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
    )
    MaterialManagement_button.click()

    # Wait for the "Contacts" button to be clickable and click it
    Contact_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[1]/div[2]/div/button[3]'))
    )
    Contact_button.click()

    time.sleep(1)

    # Wait for the "Add" button to be clickable and click it
    Add_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/a'))
    )
    Add_button.click()

    # Wait for the "Name" field to be clickable and type in it
    Name_input = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Name"]'))
    )
    Name_input.send_keys(name)

    # Wait for the "Drop Down" field to be clickable and click it
    Contact_Type = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="TypeID"]'))
    )
    Contact_Type.click()

    # Wait for the "Drop Down" field to show up
    menu = WebDriverWait(firefox, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.MuiList-root.MuiList-padding.MuiMenu-list.muiltr-r8u8y9"))
    )

    match type:
        case 1:
    # Now select publisher drop-down option and click it
            Publisher = WebDriverWait(firefox, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[1]'))
            )
            Publisher.click()
        case 2:
            Rightholder = WebDriverWait(firefox, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
            )
            Rightholder.click()
        case 3:
            Other = WebDriverWait(firefox, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[3]'))
            )
            Other.click()

    time.sleep(1)

    #Wait for Submit Button to be clickable and click it
    Submit_Button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div[1]/div/div[2]/button[2]'))
    )

    Submit_Button.click()

    # Get the page source
    page_source = firefox.page_source
    time.sleep(1)
    x = " "

    # Check if the expected text is present
    if "Contact has been created successfully." in page_source:
        x = "Pass, created new contact"
    elif f"Contact with Name {name} already exists" in page_source:
        x = "Pass, contact already existed"
    else:
        x = "Fail"

    time.sleep(1)
    firefox.close()
    return x

#Test Case 2: Create a new materal
#Checking is not working
#number is media type selection
def TestCase2(selected, name, number, author, descrip):
    firefox = browser(selected)
    firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")
    # Wait for the "Material Management" button to be clickable and click it
    MaterialManagement_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
    )
    MaterialManagement_button.click()

    #Click Materials Tab
    Material_button = WebDriverWait(firefox, 10).until (
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[1]/div[2]/div/button[2]'))
    )
    Material_button.click()

    #Click Add button
    Add_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/a'))
    )
    Add_button.click()

    #Used for Name input box
    Name_input = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Name"]'))
    )
    Name_input.send_keys(name)

    #Click media dropdown menu
    Media_Type_dropdown = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="MediaTypeID"]'))
    )
    Media_Type_dropdown.click()

    #Select media type
    counter = number + 1
    xpathh = f'/html/body/div[3]/div[3]/ul/li[{counter}]'
    Media_selection = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpathh))
    )
    Media_selection.click()

    time.sleep(1)

    #Click Author dropdown
    Author_dropdown_select = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="AuthorID"]'))
    )
    Author_dropdown_select.click()

    #Select Author
    xpathhh = f'/html/body/div[3]/div[3]/ul/li[{author}]'
    Author_selection = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpathhh))
    )
    Author_selection.click()

    time.sleep(1)

    #Select Description
    description = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Description"]'))
    )
    description.send_keys(descrip)
    time.sleep(1)

    #Click the submit button
    Submit_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div[1]/div/div[2]/span'))
    )
    time.sleep(1)
    Submit_button.click()

    #Same logic used for seeing if successful or not
    x = " "
    page_source = firefox.page_source
    if "Material has been created successfully." in page_source:
        x = "Pass, created new material"
    elif "Material with the same Name, Media Type, and Author already exists" in page_source:
        x = "Pass, material already existed"
    else:
        x = "Fail"
    time.sleep(1)
    firefox.close()
    return x

#Test Case 3: Create a new product
#index is client selection
def TestCase3(selected,index, passw, commer, type, name, descrip):
    firefox = browser(selected)
    firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")

    # Wait for the "Product Management" button to be clickable and click it
    ProjectManagement_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-navbar-side-panel"]/div/ul/a[3]'))
    )
    ProjectManagement_button.click()

    #Add Button click
    Add_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div[1]/div/div/a'))
    )
    Add_button.click()

    #Name Input box
    Name_input = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Name"]'))
    )
    Name_input.send_keys(name)

    #Click on product dropdown
    Product_Type_dropdown = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="TypeID"]'))
    )
    Product_Type_dropdown.click()

    time.sleep(1)

    #Used for selecting product type
    type_xpath = f'/html/body/div[3]/div[3]/ul/li[{type}]'
    Type_selection = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, type_xpath))
    )
    Type_selection.click()

    time.sleep(1)

    #Select password box and select correct option
    password = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div[2]/div/div/div/div/div/div[3]/div/div'))
    )
    password.click()
    xpath_pass = f'/html/body/div[3]/div[3]/ul/li[{passw}]'

    password_selection = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_pass))
    )
    password_selection.click()

    time.sleep(1)

    #Select commericalization box and select correct option
    commerc = WebDriverWait(firefox, 10).until (
        EC.element_to_be_clickable((By.XPATH, '//*[@id="IsCommercialized"]'))
    )
    commerc.click()

    commerc_xpath = f'/html/body/div[3]/div[3]/ul/li[{commer}]'
    time.sleep(1)
    commerc_dropdown = WebDriverWait(firefox, 10).until (
        EC.element_to_be_clickable((By.XPATH, commerc_xpath))
    )
    commerc_dropdown.click()

    #Click client dropdown
    time.sleep(1)
    Client_dropdown = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ClientID"]'))
    )
    Client_dropdown.click()

    time.sleep(1)

    #Click current client option
    xpathh = f'/html/body/div[3]/div[3]/ul/li[{index + 1}]'
    Client_selection = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpathh))
    )
    Client_selection.click()

    time.sleep(1)

    #Description box
    description = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Description"]'))
    )
    description.send_keys(descrip)

    #Select submit button
    Submit_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div[1]/div/div[2]/span/button'))
    )
    time.sleep(1)
    Submit_button.click()

    time.sleep(0.5)

    #Same logic for seeing if it worked
    page_source = firefox.page_source
    time.sleep(1)
    x = " "
    if "Product has been created successfully." in page_source:
        x = "Pass, created new product"
    elif "Product with same name already exists" in page_source:
        x = "Pass, product already existed"
    else:
        x = "Fail"
    time.sleep(1)
    firefox.quit()
    return x

#Add Author
#Checking looks good
def TestCase4(selected, name):

    firefox = browser(selected)

    firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")

    #Click admin button on side
    Admin_button = WebDriverWait(firefox, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[7]'))
    )
    Admin_button.click()

    #Click add button
    add_button = WebDriverWait(firefox, 10).until (
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'))
    )
    add_button.click()

    time.sleep(1)

    #Select name input box
    name_input = WebDriverWait(firefox, 10).until (
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div/input'))
    )
    name_input.send_keys(name)

    time.sleep(1)

    #Click submit button
    submit_button = WebDriverWait(firefox, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/button'))
    )
    submit_button.click()
    time.sleep(0.5)

    #Logic for checking if it work or not
    x = " "
    page_source = firefox.page_source
    if "Author has been created successfully." in page_source:
        x = "Pass, added new author"
    elif "Failed to create author, or author already exists." in page_source:
        x = "Pass, author already exists"
    else:
        x = "Fail"
    time.sleep(1)
    firefox.quit()
    return x

#Delete Contact
#Checking looks good
def TestCase5(browse, contact):
    firefox = browser(browse)

    firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")
    # Wait for the "Product Management" button to be clickable and click it
    ProjectManagement_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
    )
    ProjectManagement_button.click()

    #Contact button
    Contact_button = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[1]/div[2]/div/button[3]'))
    )
    Contact_button.click()

    time.sleep(1)

    #Used to click the (...) button beside contact for the one which we want
    expand_button = WebDriverWait(firefox, 10).until (
        EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[{contact + 1}]/td[4]/button'))
    )
    expand_button.click()

    time.sleep(1)

    #Click delete button
    delete_button = WebDriverWait(firefox, 10).until (
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]'))
    )
    delete_button.click()

    time.sleep(1)

    # Click delete confirmation
    delete_confirmation = WebDriverWait(firefox, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/li[2]'))
    )
    delete_confirmation.click()

    #Checking logic
    x = " "
    time.sleep(0.5)
    page_source = firefox.page_source
    if "Contact has been deleted successfully." in page_source:
        x = "Pass, deleted contact"
    elif "A Product/Material is using this Address" in page_source:
        x = "Pass, contact is in use"
    else:
        x = "Fail"
    time.sleep(1)
    firefox.quit()
    return x
