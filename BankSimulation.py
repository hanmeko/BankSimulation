import queue 
import threading
import time
import random

bank_line = queue.Queue()
cust_wait_times = []

def Teller(numOfTellers):
    while True:
        if bank_line.empty():
            print(f"There aren't any customers for Teller {numOfTellers} to help.")
            time.sleep(1)
        else:
            customer, arrival_time = bank_line.get()
            wait_time = time.time() - arrival_time
            print(f"Teller {numOfTellers} is serving customer {customer}.")
            service_num= random.randint(3, 9)
            if service_num == 3:
                print(f"Teller {numOfTellers} is helping customer {customer} with a withdrawing money.") 
                time.sleep(3)
                cust_wait_times.append(3)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 3 minutes to help this customer. Their wait time was: {wait_time:.2f} minutes.")
            elif service_num == 4:  
                print(f"Teller {numOfTellers} is helping customer {customer} with a depositing money.") 
                time.sleep(4)
                cust_wait_times.append(4)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 4 minutes to help this customer.Their wait time was: {wait_time:.2f} minutes.")
            elif service_num == 5:
                print(f"Teller {numOfTellers} is helping customer {customer} with a sending money.") 
                time.sleep(5)
                cust_wait_times.append(5)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 5 minutes to help this customer.Their wait time was: {wait_time:.2f} minutes.")
            elif service_num == 6:
                print(f"Teller {numOfTellers} is helping customer {customer} with a opening an account.") 
                time.sleep(6)
                cust_wait_times.append(6)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 6 minutes to help this customer. Their wait time was: {wait_time:.2f} minutes")
            elif service_num == 7:
                print(f"Teller {numOfTellers} is helping customer {customer} with a closing an account.") 
                time.sleep(7)
                cust_wait_times.append(7)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 7 minutes to help this customer. Their wait time was: {wait_time:.2f} minutes")
            elif service_num == 8:
                print(f"Teller {numOfTellers} is helping customer {customer} with a applying for a new credit line.") 
                time.sleep(8)
                cust_wait_times.append(8)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 8 minutes to help this customer.Their wait time was: {wait_time:.2f} minutes")
            elif service_num == 9:  
                print(f"Teller {numOfTellers} is helping customer {customer} with a getting bank dcuments for the last 6 months.") 
                time.sleep(9)
                cust_wait_times.append(9)
                bank_line.task_done()
                print (f" Teller {numOfTellers} took 9 minutes to help this customer. Their wait time was: {wait_time:.2f} minutes")
        

def Customer_arrival(numOfCustomers):
    for customer_num in range(1, numOfCustomers+1):
        arrival_time = time.time()
        bank_line.put((customer_num, arrival_time))
        print(f"Customer {customer_num} has joined the queue.")
        time.sleep(random.randint(1, 7))
   
def main():

    print("Welcome to the Bank Simulation!")
    number_of_customers = int(input(f"How many total customers would you like to see in one day?: "))
    number_of_tellers = int(input(f"How many tellers would you like to have for this simulation?: "))

    customer_thread = threading.Thread(target=Customer_arrival, args=(number_of_customers,))
    customer_thread.start()

    teller_threads = []
    for teller_num in range(1, number_of_tellers+1):
        teller_thread = threading.Thread(target=Teller, args=(teller_num,))
        teller_threads.append(teller_thread)
        teller_thread.start()
        
    
    customer_thread.join()  
    bank_line.join()

    avg_wait_time = sum(cust_wait_times) / len(cust_wait_times)
    print(f"The average wait time for all customers was: {avg_wait_time:.2f} minutes.")
    
    for teller_thread in teller_threads:
        teller_thread.join()
        print(f"The tellers have finished serving all the customers. Simulation concluded.")