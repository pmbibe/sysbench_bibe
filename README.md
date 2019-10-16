# sysbench_bibe
It works based on Sysbench. But it only use for testing MySQL Database. If you want to use it, you should test on MySQL version 5.6. It doesn't work with version higher, lower neither.
# Usage
Require Python version 2.7
python OS.py [options]
# Options
--threads:	The total number of worker threads to create	1
--events:	Limit for total number of requests. 0 (the default) means no limit	0
--time:	Limit for total execution time in seconds. 0 means no limit	10
--rate:	Average transactions rate. The number specifies how many events (transactions) per seconds should be executed by all threads on average. 0 (default) means unlimited rate, i.e. events are executed as fast as possible	0
--report-interval:	Periodically report intermediate statistics with a specified interval in seconds. Note that statistics produced by this option is per-interval rather than cumulative. 0 disables intermediate reports	0
--debug	Print more debug info	off
