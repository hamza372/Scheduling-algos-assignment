no_of_pro = raw_input("enter no of processes")
print(no_of_pro)

arrival_time = [0]*int(no_of_pro)
brust_time = [0]*int(no_of_pro)
exe_startTime = [0]*int(no_of_pro)
#priority = [0]*int(no_of_pro)

for i in range(0,int(no_of_pro)):
	arrival_time[i] = raw_input("enter arrival time = ");
	brust_time[i] = raw_input("enter brust time =  ");
        #priority[i] = raw_input("enter priority = ");

min = brust_time[0]
for i in range(0,int(no_of_pro)-1):
	for j in range(0,int(no_of_pro)-1-i):
		if arrival_time[j]>arrival_time[j+1]:
			arrival_time[j],arrival_time[j+1] = arrival_time[j+1],arrival_time[j];
			brust_time[j],brust_time[j+1] = brust_time[j+1],brust_time[j];

for i in range(0,int(no_of_pro)):
	print(brust_time[i])
	
time = 0;
jobs_remaining = int(no_of_pro)
k=int(0)
while jobs_remaining  != 0:
        
        #print(arrival_time[k])
        if int(time) >= int(arrival_time[k]) :
		#print("br"+brust_time[k])
		#print(k)
                exe_startTime[k] = time;
		jobs_remaining = jobs_remaining - 1
		time = time+int(brust_time[k])
                print(exe_startTime[k])

		
		if k+1 > int(no_of_pro)-1:
			k = 0
 		else: 
			k = k+1
			
	else:
		if k+1 > int(no_of_pro)-1:
			k = 0
 		else: 
			k=k+1
	#print(jobs_remaining )
        #print(time)
