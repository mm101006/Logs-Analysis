# Project: Logs Analysis 

This project is for the Nanodegree _Intro to Programming_. I chose 
_Back-End Development_ as my specialization. For the final project you are to design a reporting tool that prints out reports based on questions given by Udacity. The project requirements can be found at: 
	[Requirements](https://review.udacity.com/#!/rubrics/277/view) 

**Install Prerequisites**

1. Python 2.7
2. Linux-Based virtual machine(VM)
3. Vagrant

**Running Code**

In order to run the code you have to open up the directory where the Vagrantfile is in your command prompt. Within the command prompt type in `vagrant up` then type in `vagrant ssh`. If vagrant up is already running, just type in vagrant ssh. Then change the directory by typing in `cd /vagrant`. Type `ls` to reveal which folders are in the directory. Then change directory to the folder _news_ by typing in `cd news`. Finally, type in `python newsdatadb.py`, which will run the code.

**Views Used**

I used two views to complete the third question. 

1. create view sum_status as select date(time) as date, cast(count(*) as decimal) as total from log group by date;

2. create view sum_404 as select date(time) as date, cast(count(*) as decimal) as NOT_FOUND from log where status = '404 NOT FOUND' group by date order by date asc; 


