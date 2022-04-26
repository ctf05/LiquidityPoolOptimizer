import random
import PySimpleGUI as sg
import multiprocessing as mp
from collections import Counter
import threading
import time




def main():
    sg.theme('DarkAmber')  # Add a touch of color

    layout = [[sg.Column([[sg.Text('Initial Investment:')], [sg.InputText('5000')],
                          [sg.Text('Cost to widthdraw and deposit:')], [sg.InputText('55')],  # automate this
                          [sg.Text('Average widthdraw and deposit frequency in days:')], [sg.InputText('45')],
                          [sg.Text('Percentage variance in widthdraw and deposit frequency:')], [sg.InputText('25')],
                          [sg.Text('Average APR:')], [sg.InputText('50')],
                          [sg.Text('Percentage APR vairance by day:')], [sg.InputText('50')],
                          [sg.Text('Repetitions:')], [sg.InputText('100')],
                          [sg.Text('State:')], [sg.InputText('0')],
                          [sg.Button('Calculate')]])]]

    # Create the Window
    window = sg.Window('Liquidity Pool Optimizer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        try:
            start_time = time.time()
            principle = int(values[0])
            cost = int(values[1])
            with_freq = int(values[2])
            freq_var = int(values[3])
            apr = int(values[4])
            apr_var = int(values[5])
            repetitions = int(values[6])
            state = int(values[7]) # 0=normal, 1=threads, 2=multiprocessing
            range = int(principle * .15)
            print("calculating")

            #thread(with_freq, freq_var, apr, apr_var, principle, cost)
            if state == 2:
                return with_freq, freq_var, apr, apr_var, principle, cost, repetitions, state
            if state == 1:
                thread(with_freq, freq_var, apr, apr_var, principle, cost, repetitions)
                print("time: ", time.time() - start_time, "seconds")
            if state == 0:
                winners = {}
                determine(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners, range)
                print(max(winners, key=winners.get))
                print("time: ", time.time() - start_time, "seconds")


        except Exception as e:
            print("You fucked up:", e)
    window.close()


def get_with_array(with_freq, freq_var):
    number_of_with = int(365 / with_freq) + 2
    array = []
    for i in range(0,number_of_with):
        array.append(int(with_freq * random.randrange(int(((1 - (freq_var / 100)) * 10000)), int(((1 + (freq_var / 100))) * 10000)) / 10000))
    average = 0
    for i in array:
        average += i
    average = average / number_of_with
    diff = -(average - with_freq)
    if diff >= 1 or diff <= -1:
        new_array = array
        array = []
        diff = int(diff)
        for i in new_array:
            array.append(i + diff)
        average = 0
        for i in array:
            average += i
        average = average / number_of_with
    return array

def get_apr_array(apr, apr_var):
    array = []
    for i in range(0,365):
        array.append(float(apr * random.randrange(int(((1 - (apr_var / 100)) * 10000)),
                                                  int((1 + (apr_var / 100)) * 10000)) / 10000))
    average = 0
    for i in array:
        average += i
    average = average / 365
    diff = -(average - apr)
    new_array = array
    array = []
    for i in new_array:
        array.append(round(i + diff, 4))
    average = 0
    for i in array:
        average += i
    average = average / 365
    return array

def calculate(with_array, apr_array, principle, cost, range):
    unclaimed = 0
    with_counter = 0
    with_index = 0
    max_p = 0
    best_i = 0
    new_principle = principle
    for i in range(cost, range):
        for z in range(0, 364):
            unclaimed += new_principle * (apr_array[z] / 100 / 365)
            with_counter += 1
            if unclaimed >= i:
                new_principle += unclaimed - cost
            #    print(unclaimed)
                unclaimed = 0
                with_counter = 0
            if with_counter == with_array[with_index]:
            #    print("withdrew", with_counter)
                new_principle += unclaimed - cost
                unclaimed = 0
                with_counter = 0
                with_index += 1
        if (new_principle + unclaimed) > max_p:
            max_p = new_principle + unclaimed
            best_i = i
        #print(new_principle+unclaimed)
        new_principle = principle
        unclaimed = 0
        with_counter = 0
        with_index = 0
    print(max_p)
    return best_i

def determine(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners, range):
    for i in range(0, repetitions):
        with_array = get_with_array(with_freq, freq_var)
        apr_array = get_apr_array(apr, apr_var)
        winner = calculate(with_array, apr_array, principle, cost, range)
        try:
            winners[winner] = winners[winner] + 1
        except:
            winners[winner] = 1
    return winners

def thread(with_freq, freq_var, apr, apr_var, principle, cost, repetitions):
    winners1 = {}
    t1 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners1))
    winners2 = {}
    t2 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners2))
    winners3 = {}
    t3 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners3))
    winners4 = {}
    t4 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners4))
    winners5 = {}
    t5 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners5))
    winners6 = {}
    t6 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners6))
    winners7 = {}
    t7 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners7))
    winners8 = {}
    t8 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners8))
    winners9 = {}
    t9 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners9))
    winners10 = {}
    t10 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners10))
    winners11 = {}
    t11 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners11))
    winners12 = {}
    t12 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners12))
    winners13 = {}
    t13 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners13))
    winners14 = {}
    t14 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners14))
    winners15 = {}
    t15 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners15))
    winners16 = {}
    t16 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners16))
    winners17 = {}
    t17 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners17))
    winners18 = {}
    t18 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners18))
    winners19 = {}
    t19 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners19))
    winners20 = {}
    t20 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners20))
    winners21 = {}
    t21 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners21))
    winners22 = {}
    t22 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners22))
    winners23 = {}
    t23 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners23))
    winners24 = {}
    t24 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners24))
    winners25 = {}
    t25 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners25))
    winners26 = {}
    t26 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners26))
    winners27 = {}
    t27 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners27))
    winners28 = {}
    t28 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners28))
    winners29 = {}
    t29 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners29))
    winners30 = {}
    t30 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners30))
    winners31 = {}
    t31 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners31))
    winners32 = {}
    t32 = threading.Thread(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners32))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    t31.join()
    t32.join()
    print("joined")
    winners_end = Counter(winners1) + Counter(winners2) + Counter(winners3) + Counter(winners4) + Counter(winners5) + Counter(winners6) + Counter(winners7) + Counter(winners8) + Counter(winners9) + Counter(winners10) + Counter(winners11) + Counter(winners12) + Counter(winners13) + Counter(winners14) + Counter(winners15) + Counter(winners16) + Counter(winners17) + Counter(winners18) + Counter(winners19) + Counter(winners20) + Counter(winners21) + Counter(winners22) + Counter(winners23) + Counter(winners24) + Counter(winners25) + Counter(winners26) + Counter(winners27) + Counter(winners28) + Counter(winners29) + Counter(winners30) + Counter(winners31) + Counter(winners32)
    print(max(winners, key=winners.get))


with_freq, freq_var, apr, apr_var, principle, cost, repetitions, state = main()

if __name__ == '__main__' and state == 2:
    start_time = time.time()
    winners = {}
    print("Started")
    mp.set_start_method("spawn")
    process = mp.Process(target=determine, args=(with_freq, freq_var, apr, apr_var, principle, cost, repetitions, winners))
    process.start()
    process.join()
    print(winners)
    print("time: ", time.time() - start_time, "seconds")
else:
    main()
