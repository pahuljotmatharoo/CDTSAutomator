#Created by Pahuljot Matharoo
import streamlit as st
from run_testcase import *

#States are used by Streamlit to prevent refreshing of element everytime a button/input is updated, stores current state and doesn't allow it to be edited
#Saving a state means that it doesn't change unless refreshed page

#These are all the states used in the code
# Ensure keys are initialized in session state
if "authors" not in st.session_state:
    st.session_state["authors"] = []

if "optionss" not in st.session_state:
    st.session_state["optionss"] = []

# Initialize a flag in session state to ensure the block only runs once
if "options_loaded" not in st.session_state:
    st.session_state["options_loaded"] = False

if "authors_loaded" not in st.session_state:
    st.session_state["authors_loaded"] = False

if "selected_option_type" not in st.session_state:
    st.session_state["selected_option"] = None

# Ensure session state is initialized for dropdown items
if "dropdown_items_loaded" not in st.session_state:
    st.session_state["dropdown_items_loaded"] = False

# Ensure session state is initialized for dropdown items
if "contact_items_loaded" not in st.session_state:
    st.session_state["contact_items_loaded"] = False

if 'label_list' not in st.session_state:
    st.session_state.label_list = []

#Function Checking which browser to use
def browser(selected_browser):
    firefox = 0
    if selected_browser == "Chrome":
        firefox = 1
    elif selected_browser == "Firefox":
        firefox = 2
    elif selected_browser == "Edge":
        firefox = 3
    return firefox

# App title and layout
st.title("CDTS Test Automator")

# Tabs for each test case
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Create New Contact", "Create New Material", "Create New Product", "Add New Author", "Remove Contact", "Results"])

#First Tab
with tab1:
    loop_count = st.number_input("Loops:", min_value=1, step=1, key=f"loop_count_1")
    name = st.text_input("Name:", "", key=f"name_1")
    options = ["Publisher", "Rightholder", "Other"]
    options_browser = ["Chrome", "Firefox", "Edge"]
    selected_option_browser = st.selectbox("Choose a browser:", options_browser, key=f"type_11")
    selected_option = st.selectbox("Choose a Contact Type:", options, key=f"type_1")
    if (selected_option == "Publisher"):
        type_data = 1
    elif (selected_option == "Rightholder"):
        type_data = 2
    elif (selected_option == "Other"):
        type_data = 3

    firefox = browser(selected_option_browser)

    if st.button(f"Run Create Contact Test Case", key=f"run_1"):
        if name and loop_count and type_data:
            y = run1(firefox, loop_count, name, type_data)
            st.session_state.label_list.append(y)
        else:
            st.warning("Please enter both a valid loop count and a name.")

with tab2:
    loop_count = st.number_input("Loops:", min_value=1, step=1, key="loop_count_2")
    name = st.text_input("Name:", "", key="name_2")
    options_browser = ["Chrome", "Firefox", "Edge"]
    selected_option_browser = st.selectbox("Choose a browser:", options_browser, key="type_12")
    selected_description = st.text_input("Description:", "", key="descrip_1")

    # Set up Firefox options
    #This is the part which gets the items loaded into the box
    options = webdriver.FirefoxOptions()
    options.set_preference("permissions.default.image", 2)  # Block images
    options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")  # Disable Flash
    options.add_argument("--headless")  # Enable headless mode

    # Load Media Types into session state
    if not st.session_state.get("options_loaded"):
        optionss = []
        firefox = webdriver.Firefox(options=options)
        firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")
        MaterialManagement_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
        )
        MaterialManagement_button.click()

        Material_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[1]/div[2]/div/button[2]'))
        )
        Material_button.click()

        Add_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/a'))
        )
        Add_button.click()

        Media_Type_dropdown = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="MediaTypeID"]'))
        )
        Media_Type_dropdown.click()

        counter = 1
        while True:
            try:
                xpath = f'/html/body/div[3]/div[3]/ul/li[{counter}]'
                temp = WebDriverWait(firefox, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                optionss.append(temp.text)
                counter += 1
            except:
                break

        firefox.close()
        st.session_state["optionss"] = optionss
        st.session_state["options_loaded"] = True

    # Load Authors into session state
    if not st.session_state.get("authors_loaded"):
        authors = []
        firefox = webdriver.Firefox(options=options)
        firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")
        MaterialManagement_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
        )
        MaterialManagement_button.click()

        Material_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[1]/div[2]/div/button[2]'))
        )
        Material_button.click()

        Add_button = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="fuse-main"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/a'))
        )
        Add_button.click()

        Author_dropdown_select = WebDriverWait(firefox, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="AuthorID"]'))
        )
        Author_dropdown_select.click()

        counter = 1
        while True:
            try:
                xpath = f'/html/body/div[3]/div[3]/ul/li[{counter}]'
                temp = WebDriverWait(firefox, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                authors.append(temp.text)
                counter += 1
            except:
                break

        firefox.close()
        st.session_state["authors"] = authors
        st.session_state["authors_loaded"] = True

    # Use session state values for dropdowns
    selected_item_options = st.selectbox("Select a Media Type:", st.session_state["optionss"], key="select_media_type")
    selected_item_authors = st.selectbox("Select an Author:", st.session_state["authors"], key="select_author")

    # Ensure the correct browser is initialized
    firefox = browser(selected_option_browser)

    if st.button("Run Create Material Test Case", key="run_2"):
        if name and loop_count:
            selected_index_type = st.session_state["optionss"].index(selected_item_options)
            selected_index_author = st.session_state["authors"].index(selected_item_authors) + 1
            y = run2(firefox, loop_count, name, selected_index_type, selected_index_author, selected_description)
            st.session_state.label_list.append(y)
        else:
            st.warning("Please enter a valid loop count, name, and valid option selection.")



with tab3:
    # Initialize session state for dropdown items if not already done
    if "dropdown_items" not in st.session_state:
        st.session_state["dropdown_items"] = []
        st.session_state["dropdown_items_loaded"] = False

    loop_count = st.number_input("Loops:", min_value=1, step=1, key=f"loop_count_{3}")
    name = st.text_input("Name:", "", key=f"name_{3}")
    selected_description = st.text_input("Description:", "", key=f"descrip_2")
    options_browser = ["Chrome", "Firefox", "Edge"]
    selected_option_browser = st.selectbox("Choose a browser:", options_browser, key=f"type_17")

    # This is the part which gets the items loaded into the boxes
    if not st.session_state["dropdown_items_loaded"]:
        # Load dropdown items only if not already loaded
        options = webdriver.FirefoxOptions()

        # Disable images in Firefox
        options.set_preference("permissions.default.image", 2)  # 2 = block images
        options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")  # Disable Flash plugins

        # Enable headless mode
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

        driver.get("https://cdts-dev.cel.uwaterloo.ca:9423/")

        # Wait for and click the "Material Management" button
        project_management_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-navbar-side-panel"]/div/ul/a[3]'))
        )
        project_management_button.click()

        # Wait for and click the "Add" button
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fuse-main"]/div/div/div[1]/div/div/a'))
        )
        add_button.click()

        # Wait for and click the dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div')
            )
        )
        dropdown.click()

        # Extract dropdown items
        dropdown_items = []
        checking = True
        counter = 1
        while checking:
            xpath = f'/html/body/div[3]/div[3]/ul/li[{counter}]'
            try:
                temp = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                dropdown_items.append(temp.text)
                counter += 1
            except:
                checking = False

        # Close the browser
        driver.close()

        # Update session state with the dropdown items
        st.session_state["dropdown_items"] = dropdown_items
        st.session_state["dropdown_items_loaded"] = True

    # Use session state to populate the dropdown items
    dropdown_items = st.session_state["dropdown_items"]
    selected_item = st.selectbox("Select a client:", dropdown_items)

    options_type = ["Product Type 1", "Product Type 2", "Product Type 3", "Product Type 4"]
    type_data = 0
    selected_option_type = st.selectbox("Select a Product Type:", options_type, key=f"type_15")
    if selected_option_type == "Product Type 1":
        type_data = 1
    elif selected_option_type == "Product Type 2":
        type_data = 2
    elif selected_option_type == "Product Type 3":
        type_data = 3
    elif selected_option_type == "Product Type 4":
        type_data = 4

    options_pass = ["Yes", "No"]
    pass_data = 0
    selected_option_password = st.selectbox("Will the content be Open (not password-protected)?:", options_pass, key=f"type_13")
    if selected_option_password == "Yes":
        pass_data = 1
    elif selected_option_password == "No":
        pass_data = 2

    options_commer = ["Yes", "No"]
    commer_data = 0
    selected_option_commer = st.selectbox("Will the product be commercialized?:", options_commer, key=f"type_14")
    if selected_option_commer == "Yes":
        commer_data = 1
    elif selected_option_commer == "No":
        commer_data = 2

    firefox = browser(selected_option_browser)

    if st.button(f"Run Create Product Test Case {3}", key=f"run_3"):
        if name and loop_count:
            selected_item_index = dropdown_items.index(selected_item)
            y = run3(firefox, selected_item_index, pass_data, commer_data, type_data, loop_count, name, selected_description)
            st.session_state.label_list.append(y)
        else:
            st.warning("Please enter both a valid loop count and a name.")


with tab4:
    loop_count = st.number_input("Loops:", min_value=1, step=1, key=f"loop_count_5")
    name = st.text_input("Name:", "", key=f"name_4")
    options_browser = ["Chrome", "Firefox", "Edge"]
    selected_option_browser = st.selectbox("Choose a browser:", options_browser, key=f"type_111")
    firefox = browser(selected_option_browser)

    if st.button(f"Run Create Contact Test Case", key=f"run_4"):
        if name and loop_count:
            y = run4(firefox, loop_count, name)
            st.session_state.label_list.append(y)
        else:
            st.warning("Please enter both a valid loop count and a name.")

with tab5:
    # Initialize session state variables
    if "contact_items" not in st.session_state:
        st.session_state["contact_items"] = []
    if "contact_items_loaded" not in st.session_state:
        st.session_state["contact_items_loaded"] = False

    options_browser = ["Chrome", "Firefox", "Edge"]
    selected_option_browser = st.selectbox("Choose a browser:", options_browser, key=f"type_18")
    firefox = browser(selected_option_browser)

    # This is the part which gets the items loaded into the boxes
    if not st.session_state["contact_items_loaded"]:
        options = webdriver.FirefoxOptions()

        # Disable images in Firefox
        options.set_preference("permissions.default.image", 2)  # 2 = block images
        options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")  # Disable Flash plugins

        # Enable headless mode
        options.add_argument("--headless")

        # Start WebDriver
        firefox = webdriver.Firefox(options=options)

        try:
            # Navigate to the URL
            firefox.get("https://cdts-dev.cel.uwaterloo.ca:9423/")

            # Wait for the "Material Management" button and click it
            ProjectManagement_button = WebDriverWait(firefox, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/ul/a[2]'))
            )
            ProjectManagement_button.click()

            # Wait for the "Contact" button and click it
            Contact_button = WebDriverWait(firefox, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[1]/div[2]/div/button[3]'))
            )
            Contact_button.click()

            # Collect contacts into an array
            contacts = []

            # Wait for the table to load and extract contact items
            table_rows = WebDriverWait(firefox, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr')
                )
            )
            for row in table_rows:
                # Extract the text from the first column of each row
                contact_text = row.find_element(By.XPATH, './td[1]').text
                contacts.append(contact_text)

            # Save contacts to session state
            st.session_state["contact_items"] = contacts
            st.session_state["contact_items_loaded"] = True

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            # Ensure the browser is closed
            firefox.quit()

    # Use session state to populate the dropdown
    contacts = st.session_state["contact_items"]
    selected_item = st.selectbox("Select a contact to remove:", contacts)
    if st.button(f"Run Create Product Test Case {3}", key=f"run_5"):
        selected_contact = contacts.index(selected_item)
        y = run5(firefox, selected_contact)
        st.session_state.label_list.append(y)

with tab6:
    if st.session_state.label_list:
        for idx, label in enumerate(st.session_state.label_list, start=1):
            st.write(f"{idx}. {label}")
    else:
        st.write("No labels added yet.")
