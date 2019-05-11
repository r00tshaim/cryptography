import nmap
import pandas as pd

def PortsScanner(network_ip):
	mydict=dict()
	nmScan=nmap.PortScanner()
	nmScan.scan(network_ip,"21-243")
	hosts=nmScan.all_hosts()
	print("{:<20}{:<20}").format("Host","State")
	for host in nmScan.all_hosts():
		#print("Host: %s State: %s" %(host,nmScan[host].state()))
		print("{:<20}{:<20}").format(host,nmScan[host].state())
		mydict[host]=nmScan[host].state()
	print(mydict)

	df=pd.DataFrame({'Hosts' : mydict.keys(),
			'State' : mydict.values()})	

	df.to_csv("report.csv")



network_ip=raw_input("Enter network ip:")
PortsScanner(network_ip)
	


