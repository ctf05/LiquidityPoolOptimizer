import random
import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')  # Add a touch of color

    layout = [[sg.Column([[sg.Text('Initial Investment:')], [sg.InputText('1000')],
                          [sg.Text('Cost to widthdraw and deposit:')], [sg.InputText('60')],  # automate this
                          [sg.Text('Average widthdraw and deposit frequency in days:')], [sg.InputText('30')],
                          [sg.Text('Percentage variance in widthdraw and deposit frequency')], [sg.InputText('25')],
                          [sg.Text('Average APR')], [sg.InputText('10')],
                          [sg.Text('APR vairance by day')], [sg.InputText('50')],
                          [sg.Button('Calculate')]])]]

    # Create the Window
    window = sg.Window('Liquidity Pool Optimizer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        try:
            principle = int(values[0])
            cost = int(values[1])
            with_freq = int(values[2])
            freq_var = int(values[3])
            apr = int(values[4])
            apr_var = int(values[5])
            print("calculating")
            with_array = get_with_array(with_freq, freq_var)
            apr_array = get_apr_array(apr, apr_var)
        except:
            print("You fucked up")
    window.close()


def get_with_array(with_freq, freq_var):
    number_of_with = int(365 / with_freq)
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
    print(array)
    return array

def get_apr_array(apr, apr_var):
    array = []
    for i in range(0,365):
        array.append(float(apr * random.randrange(int(((1 - (apr / 100)) * 10000)), int(((1 + (apr / 100))) * 10000)) / 10000))
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
    print(array, average, diff)
    return array

main()
