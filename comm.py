from pywinusb import hid

filter1 = hid.HidDeviceFilter(vendor_id=0x0416, product_id=0xffff)
devices = filter1.get_devices()

if devices:
    device = devices[0]
    print "success"

device.open()
out_report = device.find_output_reports()[0]
print(device.find_output_reports()[0])
my_buffer= [0x0]*31
my_buffer[0]=0x0
my_buffer[1]=0x02
my_buffer[2]=0x35
my_buffer[3]=0x0A
print(my_buffer)
out_report.set_raw_data(my_buffer)
print out_report
out_report.send(my_buffer)
device.close()