import os
import psutil

def select_phoneme(list,k):
        start,end=k,k
        while ((end+1)<len(list)) and (list[k]==list[end+1]):
            end+=1
        try:
            while ((start-1)>=0) and (list[k]==list[start-1]):
                start-=1
        except:
            print(start,k, len(list))
        return start,end

def get_libri_phoneme(fname):
    with open(fname) as file:
        phoneme_list = []
        while(True):
            aline = file.readline()
            if not aline : break
            phoneme_list.append(aline.split("\n")[0])
        
    return phoneme_list

def get_memory_usege():
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

def most_list(p_list,a_list,t_len):
    phoneme = max(p_list, key=p_list.count)
    accent=0
    timming=0
    for i in range(len(p_list)): 
        if p_list[i] == phoneme:
            accent=(accent+a_list[i])/2
        timming+=t_len
    return phoneme,accent,timming
