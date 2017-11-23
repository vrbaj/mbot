import msvcrt
from pywinusb import hid


filter1 = hid.HidDeviceFilter(vendor_id=0x0416, product_id=0xffff)
devices = filter1.get_devices()

if devices:
    device = devices[0]
    print("wifi serial line dongle connected")



while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        key_number = ord(key)
        print(key_number)  # kod klavesy.
        if key_number == 113:
            break
        if key_number == 56:  # vpred
            device.open()
            out_report = device.find_output_reports()[0]
            my_buffer = [0x0] * 31
            my_buffer[0] = 0x0
            my_buffer[1] = 0x02
            my_buffer[2] = 0x31
            my_buffer[3] = 0x0A
            out_report.set_raw_data(my_buffer)
            out_report.send(my_buffer)
            device.close()
        if key_number == 53:  # stop
            device.open()
            out_report = device.find_output_reports()[0]
            my_buffer = [0x0] * 31
            my_buffer[0] = 0x0
            my_buffer[1] = 0x02
            my_buffer[2] = 0x35
            my_buffer[3] = 0x0A
            out_report.set_raw_data(my_buffer)
            out_report.send(my_buffer)
            device.close()
        if key_number == 50:  # zpet
            device.open()
            out_report = device.find_output_reports()[0]
            my_buffer = [0x0] * 31
            my_buffer[0] = 0x0
            my_buffer[1] = 0x02
            my_buffer[2] = 0x32
            my_buffer[3] = 0x0A
            out_report.set_raw_data(my_buffer)
            out_report.send(my_buffer)
            device.close()
        if key_number == 52:  # vlevo
            device.open()
            out_report = device.find_output_reports()[0]
            my_buffer = [0x0] * 31
            my_buffer[0] = 0x0
            my_buffer[1] = 0x02
            my_buffer[2] = 0x33
            my_buffer[3] = 0x0A
            out_report.set_raw_data(my_buffer)
            out_report.send(my_buffer)
            device.close()
        if key_number == 54:  # vpravo
            device.open()
            out_report = device.find_output_reports()[0]
            my_buffer = [0x0] * 31
            my_buffer[0] = 0x0
            my_buffer[1] = 0x02
            my_buffer[2] = 0x34
            my_buffer[3] = 0x0A
            out_report.set_raw_data(my_buffer)
            out_report.send(my_buffer)
            device.close()
# 50 zpet, 56 vpred,52 vlevo,54 vpravo, 53 stop


