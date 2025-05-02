import queue
import threading
import time
import random

bank_line = queue.Queue()
cust_wait_times = []
cust_service_times = []
simulation_running = True

def Teller(teller_id):
    while simulation_running or not bank_line.empty():
        if bank_line.empty():
            time.sleep(1)
        else:
            customer, arrival_time = bank_line.get()
            current_time = time.time()
            wait_time = (current_time - arrival_time)*60
            wait_min, wait_sec = divmod(wait_time,60)


            cust_wait_times.append(wait_time)
            print()
            print(f"Teller {teller_id} is now serving customer {customer}.")


            service_time = random.randint(3, 9)
            service_descriptions = {
                3: "withdrawing money",
                4: "depositing money",
                5: "sending money",
                6: "opening an account",
                7: "closing an account",
                8: "applying for a new credit line",
                9: "getting bank documents for the last 6 months"
            }
            description = service_descriptions[service_time]

            print(f"Teller {teller_id} is helping customer {customer} with {description}.")
            print()

            time.sleep(service_time)
        
            cust_service_times.append(service_time)
            bank_line.task_done()

            service_min, service_sec = divmod(service_time * 60, 60)
            print(f"Teller {teller_id} is done helping customer {customer}.")
            print(f"Teller {teller_id} took {int(service_min)} minutes and {int(service_sec)} seconds to help this customer.")
            print(f"wait time was: {int(wait_min)} minutes and {int(wait_sec)} seconds (from arrival to service start).")
            print()

def Customer_arrival(num_customers):
    for customer_id in range(1, num_customers+1):
        arrival_time = time.time()
        bank_line.put((customer_id, arrival_time))
        print(f"Customer {customer_id} has joined the queue.")
        print()
       
        if customer_id < num_customers:
            time.sleep(random.randint(1, 4))

    

def main():
    global simulation_running

    print("Welcome to the Bank Simulation!")
    number_of_customers = int(input("How many total customers would you like to see in one day?: "))
    number_of_tellers = int(input("How many tellers would you like to have for this simulation?: "))
    print()
    customer_thread = threading.Thread(target=Customer_arrival, args=(number_of_customers,))
    customer_thread.start()

    teller_threads = []
    for teller_num in range(1, number_of_tellers + 1):
        teller_thread = threading.Thread(target=Teller, args=(teller_num,))
        teller_threads.append(teller_thread)
        teller_thread.start()

    customer_thread.join()
    bank_line.join()
    simulation_running = False

    for teller_thread in teller_threads:
        teller_thread.join()

    if cust_wait_times:
        avg_wait_time = sum(cust_wait_times) / len(cust_wait_times)
        max_wait_time = max(cust_wait_times)
        avg_service_time = sum(cust_service_times) / len(cust_service_times)

        avg_wait_min, avg_wait_sec = divmod(avg_wait_time, 60)
        max_wait_min, max_wait_sec = divmod(max_wait_time, 60)
        avg_service_min, avg_service_sec = divmod(avg_service_time * 60, 60)

        print("\n----- SIMULATION STATISTICS -----\n")
        
        print(f"Total customers served: {len(cust_wait_times)}\n")
        print(f"The average wait time for all customers was: {int(avg_wait_min)} minutes and {int(avg_wait_sec)} seconds.")
        print(f"The maximum wait time was: {int(max_wait_min)} minutes and {int(max_wait_sec)} seconds")
        print(f"The average service time was: {int(avg_service_min)} minutes and {int(avg_service_sec)} seconds.\n")

    print("The tellers have finished serving all the customers. Simulation concluded.")

if __name__ == "__main__":
    main()
