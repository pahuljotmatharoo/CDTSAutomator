#Created by Pahuljot Matharoo
from TestCases import *
import streamlit as st
import threading

#Basically, thread running needed to be faster application, rest is pretty self explanitory
#Store results in array
#FIREFOX,SELECTED and Browserr are passed in for determining which browser to use

def run1(browserr, loop_count, name, type):
    x = []
    def run_in_thread():
        try:
            if len(name) < 5:
                return
            for i in range(loop_count):
                result = TestCase1(browserr, name, type)
                x.append(result)
                time.sleep(1)  # Optional delay between loops
        except ValueError:
            st.warning("Please enter a valid number.")

    # Start the thread for the test case execution
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()  # Wait for the thread to complete
    return x

def run2(firefox,loop_count, name, number, number2, descrip):
    x = []
    def run_in_thread():
        try:
            if len(name) < 5:
                return

            for i in range(loop_count):
                result = TestCase2(firefox, name, number, number2, descrip)
                x.append(result)
                time.sleep(1)  # Optional delay between loops

        except ValueError:
            st.warning("Please enter a valid number.")

    # Start the thread for the test case execution
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()  # Wait for the thread to complete
    return x

def run3(selected,index_select, passw,commer,type, loop_count, name, descrip):
    x = []
    def run_in_thread():
        try:
            if len(name) < 5:
                st.warning("Please enter a name with at least 5 characters.")
                return

            for i in range(loop_count):
                result = TestCase3(selected, index_select, passw, commer, type, name, descrip)
                x.append(result)
                time.sleep(1)  # Optional delay between loops

        except ValueError:
            st.warning("Please enter a valid number.")

    # Start the thread for the test case execution
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()  # Wait for the thread to complete
    return x

def run4(selected,loop_count, name):
    x = []
    def run_in_thread():
        try:
            if len(name) < 5:
                st.warning("Please enter a name with at least 5 characters.")
                return

            for i in range(loop_count):
                result = TestCase4(selected,name)
                x.append(result)
                time.sleep(1)  # Optional delay between loops

        except ValueError:
            st.warning("Please enter a valid number.")

    # Start the thread for the test case execution
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()  # Wait for the thread to complete
    return x

def run5(selected, contact):
    x = []
    def run_in_thread():
        try:
            result = TestCase5(selected,contact)
            x.append(result)
            time.sleep(1)  # Optional delay between loops

        except ValueError:
            st.warning("Please enter a valid number.")

    # Start the thread for the test case execution
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()  # Wait for the thread to complete
    return x
