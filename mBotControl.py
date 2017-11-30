import msvcrt
from pywinusb import hid
# controling mBot thru serial wifi with numerical keys 2,4,5,6,8


filter1 = hid.HidDeviceFilter(vendor_id=0x0416, product_id=0xffff)  # find serial dongle
devices = filter1.get_devices()

if devices:
    device = devices[0]
    print("wifi serial line dongle connected")



while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        key_number = ord(key)
        print(key_number)  # stroked key number
        if key_number == 113:
            break
        if key_number == 56:  # go ahead
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
        if key_number == 53:  # stop moving
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
        if key_number == 50:  # backwards
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
        if key_number == 52:  # turn left
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
        if key_number == 54:  # turn right
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


