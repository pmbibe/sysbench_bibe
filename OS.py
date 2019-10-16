import os
import argparse
from subprocess import Popen, PIPE
def Import_Database(host,port,username,password):
             os.system("sudo yum -y install bzip2 wget \
                && sudo wget https://launchpad.net/test-db/employees-db-1/1.0.6/+download/employees_db-full-1.0.6.tar.bz2 \
                && sudo bzip2 -dfv employees_db-full-1.0.6.tar.bz2 \
                && sudo tar -xf employees_db-full-1.0.6.tar")
             os.putenv('host',host)
             os.putenv('port',port)
             os.putenv('username',username)
             os.putenv('password',password)
             os.system("mysql --host=$host --port=$port --user=$username --password=$password < employees.sql")
def Checkversion_Sysbench():
#Check version sysbench
             sysbench_checkversion = Popen("sysbench --version | awk '{print $1}' ",stdout=PIPE,shell=True)
             (version_sysbench,response) = sysbench_checkversion.communicate()
             if "sysbench" not in version_sysbench :
                     os.system("curl -s https://packagecloud.io/install/repositories/akopytov/sysbench/script.rpm.sh | sudo bash \
			&& sudo yum -y install sysbench \
			&& wget https://github.com/pmbibe/sysbench_bibe/archive/master.zip \
                        && unzip master.zip \
                        && cp $PWD/sysbench_bibe-master/test.lua /usr/share/sysbench/ ")
def Sysbench(host,port,username,password,threads,events,time,rate,report_interval,mysql_db):
             host=host
             port=port
             username=username
             password=password
             threads=threads
             events=events
             time=time
             rate=rate
             report_interval=report_interval
             mysql_db=mysql_db
             os.putenv('host',host)
             os.putenv('port',port)
             os.putenv('username',username)
             os.putenv('password',password)
             os.putenv('threads',threads)
             os.putenv('events',events)
             os.putenv('time',time)
             os.putenv('rate',rate)
             os.putenv('report_interval',report_interval)
             os.putenv('mysql_db',mysql_db)
             os.system("sysbench /usr/share/sysbench/test.lua --mysql-host=$host --mysql-port=$port --mysql-user=$username --mysql-password=$password --threads=$threads --events=$events --time=$time --rate=$rate --report-interval=$report_interval --mysql-db=$mysql_db run")
def main():
             Checkversion_Sysbench()
             mysql_checkversion = Popen("mysql --version",stdout=PIPE,shell=True)
             (version_mysql,response) = mysql_checkversion.communicate()
             if "5.6" not in version_mysql :
                     print ("""
                                          ***************************************************
                                          *                                                 * 
                                          *         You should use MySQL 5.6                *
                                          *                                                 *
                                          ***************************************************

                                                                                                  """)
             else:
                          parser = argparse.ArgumentParser(description='Option')
                          parser.add_argument('--host', dest='host', default='127.0.0.1', action='store')
                          parser.add_argument('--port', dest='port', default='3306', action='store')
                          parser.add_argument('--username', dest='username', default='root', action='store')
                          parser.add_argument('--password', dest='password', default='root', action='store')
                          parser.add_argument('--threads', dest='threads',  default=1, action='store')
                          parser.add_argument('--events', dest='events',  default=0, action='store')
                          parser.add_argument('--time', dest='time',  default=10, action='store')
                          parser.add_argument('--rate', dest='rate',  default=0, action='store')
                          parser.add_argument('--report-interval', dest='report_interval',  default=0, action='store')
                          parser.add_argument('--mysql-db',dest='mysql_db', default='employees', action='store')
                          parser.add_argument('--prepare',dest='prepare', default=0, action='store')
                          args = parser.parse_args()
                          prepare = args.prepare
                          host = args.host
                          port = args.port
                          username = args.username
                          password = args.password
                          threads = str(args.threads)
                          events = str(args.events)
                          time = str(args.time)
                          rate = str(args.rate)
                          report_interval = str(args.report_interval)
                          mysql_db = args.mysql_db
                          if prepare == 1 :
                                       Import_Database(host,port,username,password)
                          else:
                                       Sysbench(host,port,username,password,threads,events,time,rate,report_interval,mysql_db)
main()




        

