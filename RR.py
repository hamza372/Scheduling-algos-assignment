no_of_pro = raw_input("enter no of processes")
print(no_of_pro)

arrival_time = [0]*int(no_of_pro)
brust_time = [0]*int(no_of_pro)
exe_startTime = [0]*int(no_of_pro)
input_Time = [0]*int(no_of_pro)
isNoted = [0]*int(no_of_pro)

timeSlice = int(4)
input_time = int(4)

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
        input_Time[i] = int(0)
	
time = 0;
jobs_remaining = int(no_of_pro)
k=int(0)
while jobs_remaining  != 0:
        
        
        if int(time) >= int(arrival_time[k])  and int(brust_time[k]) > int(0) and input_Time[k]<=int(0):
                if isNoted[k] == int(0):
                	exe_startTime[k] = time;
			isNoted[k] = 1
                brust_time[k] = int(brust_time[k])-int(timeSlice)
		for i in range (0,int(no_of_pro)):
			if i != k and input_Time[i]>int(0):
				if brust_time[k]<=0 :
					input_Time[i] = input_Time[i]-(int(brust_time[k])+timeSlice)
				else:
					input_Time[i] = input_Time[i]-timeSlice
				
		if brust_time[k]<=0:
			jobs_remaining = jobs_remaining - 1
			time = time+(int(brust_time[k])+timeSlice)
			print("job finished",k,"at time",time,"startTime = ",exe_startTime[k],"turnATime = ",time-exe_startTime	[k])
			#print("watting time = ",arrival_time[k]+(int(time)+exe_startTime[k]-int(brust_time[k])))
                     
		else:
			time = time+int(timeSlice)
                        input_Time[k] = 4
                #print(exe_startTime[k])

		
		if k+1 > int(no_of_pro)-1:
			k = 0
 		else: 
			k = k+1
			
	else:
                for i in range (0,int(no_of_pro)):
			input_Time[i] = input_Time[i] - 1
		if k+1 > int(no_of_pro)-1:
			k = 0
 		else: 
			k=k+1
	#print(jobs_remaining )