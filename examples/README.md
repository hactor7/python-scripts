# Remote Command Executor

### Introduction:
With my learnings on python I came to a situation where I need to run some adhock command on the server, to get relevant information quickly without any special arrangement.  
One of the possible solution is **Ansible**, to be run in an adhock way. But I need something more simple than installation and configuration of ansible on my server.  
Thus I look for scripts, and with python I found a simple solution [Here](https://gist.github.com/batok/2352501).  
I have updated script to be more user interactive.


### Configuration:
* Prerequisite
	* Python3
	* paramiko
		* Install paramiko using `pip install paramiko` 



* Setup:
    *  Create alias using `alias runc='python3 /path/to/remote-command-executor.py'`
    *  To run   
    **`runc -H localhost  -i ~/.ssh/id_rsa -s 'lsb_release -a'`**
    
        OR
    
    * Run directly as   
    **`python3 remote-command-executor.py -H localhost  -i ~/.ssh/id_rsa -s 'free -m'`**  
    




