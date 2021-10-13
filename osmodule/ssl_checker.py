import ssl
from datetime import datetime
import pytz
import OpenSSL
import socket
from datetime import timedelta




print("Program to check SSL certificate validity \n")
##opening file
ipfile=open('server_ip.txt')
for ip in ipfile:
    try:
        host = ip.strip().split(":")[0]
#        print("\n Checking certifcate for server ",host)
        ctx = OpenSSL.SSL.Context(ssl.PROTOCOL_TLSv1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(443)))
        cnx = OpenSSL.SSL.Connection(ctx, s)
        cnx.set_connect_state()
        cnx.do_handshake()
        cert=cnx.get_peer_certificate()
        s.close()
        server_name = cert.get_subject().commonName
        print (server_name)
        edate=cert.get_notAfter()
        edate=edate.decode('utf-8')
        exp_date = datetime.strptime(edate,'%Y%m%d%H%M%SZ')
        date = str(exp_date)
        print("Expiry date " + " " + "of" + " " + host  + ":",  date)
    except:
        print ("error on connection to Server,",host)


print ('\nCert check completed')