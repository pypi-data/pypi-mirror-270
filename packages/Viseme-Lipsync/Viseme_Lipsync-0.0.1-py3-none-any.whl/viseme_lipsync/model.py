import numpy as np
from pathlib import Path
import torch
from torch import nn



from viseme_lipsync.conformer_ppg.model import PPGPhonemeModel
from viseme_lipsync.phonemedata import *
from viseme_lipsync.util import *
                            

class VisemeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.SAMPLE_RATE = 9600
        self.phoneme_len = 1/60
        self.chunk = 160

    def get_active_phoneme(self,audio,SR):
        audio_length = len(audio)
        audio = audio.reshape(1, audio_length)
        input_audio = torch.tensor(audio)

        ppg_model = PPGPhonemeModel.from_static(SR)
        output = ppg_model(input_audio)
        output = output.numpy()[0]

        # output phoneme post-processing
        output_len = output.shape[0]

        active_phoneme = np.zeros(shape=(output.shape))
        for i in range(output_len):
            idx = np.argmax(output[i])
            active_phoneme[i, idx] = 1

        # Phoneme print
        active_phoneme_list = []
        librispeech_path=Path(__file__).parent.joinpath("librispeech_phoneme.txt")
        phoneme_list=get_libri_phoneme(librispeech_path)
        
        for i in range(output_len):
            idx = np.argmax(active_phoneme[i])
            active_phoneme_list.append(phoneme_list[idx])
        
        return active_phoneme_list    

    def get_closest_vowel(self,phoneme_list,j,k,i):
        right=int(k+(1+i)/2)
        left=int(k-(1+i)/2)

        if right>=len(phoneme_list) or (left >=0 and (right-j)>(j-left)):
            select=phoneme_list[left]
            direc=-1
        else:
            select=phoneme_list[right]
            direc=1

        if select in phoneme_vowel_list :
            return select
        else:
            k=k+direc/2
            i+=1
            result=self.get_closest_vowel(phoneme_list,j,k,i)
            return result 

    def get_amplitude(self,audio,len):
        chunk = self.chunk
        amp=[]
        amplitude = []
        for i in range(len):
            arr = np.split(audio, [chunk])
            if np.isnan(np.mean(abs(arr[0]))):
                amplitude.append(0)
            else:
                amplitude.append(np.mean(abs(arr[0])))
                audio = arr[1]
            amp.append((1-5**(-1*np.exp(1)*1.3*amplitude[-1]))*1.7+0.7)
        return amp,amplitude
    
    def Diphthong_phoneme(self,phoneme_list,start,end):
        viseme_list=[]
        Diphthong_len=end-start+1
        Diphthong_phoneme=phoneme_list[start]
        split_num=Diphthong_len//2+1
        Diphthong_1=[phoneme_vowel_viseme_dict[Diphthong_phoneme][0]]*split_num
        Diphthong_2=[phoneme_vowel_viseme_dict[Diphthong_phoneme][1]]*split_num
        
        viseme_list.extend(Diphthong_1)
        viseme_list.extend(Diphthong_2)
        return viseme_list,start+2*split_num-1    
    
    def phonme_to_viseme(self,phoneme,amplitude_list):
        viseme_list = phoneme[:]
        i=0
        while i <len(phoneme):
            start,end = select_phoneme(phoneme,i)          
            #모음
            if start==end:
                viseme_list[start]=viseme_list[start-1]
            elif phoneme[i] in phoneme_vowel_viseme_dict:   
                #이중 모음      
                if len(phoneme_vowel_viseme_dict[phoneme[i]])>1:
                    viseme,end=self.Diphthong_phoneme(phoneme,start,end)
                    viseme_list[start:end+1]=viseme
                else:
                    viseme_list[start:end+1]=phoneme_vowel_viseme_dict[phoneme[i]]*(end-start+1)
            #자음 - 양순음
            elif phoneme[i] in phoneme_bilabial_dict:
                viseme_list[start:end+1]=phoneme_bilabial_dict[phoneme[i]]*(end-start+1)

            else:
                viseme_list[start:end+1]=[phoneme[i]]*(end-start+1)
            i=end+1

        viseme_list_vowel=viseme_list[:]
        k=0
        while k <len(viseme_list):
            start,end = select_phoneme(viseme_list,k)
            if viseme_list_vowel[k] not in phoneme_FL_list:
                clo_vow=self.get_closest_vowel(viseme_list_vowel,k,k,1)
                #자음 예외 1, 치경음
                if viseme_list_vowel[k] in phoneme_alveolar_list :
                    amplitude_list[start:end+1]=[i*0.9 for i in amplitude_list[start:end+1]]
                viseme_list[start:end+1]=[clo_vow]*(end-start+1)
                #입술이 많은 viseme에 대한 예외처리
            elif viseme_list_vowel[k] in ['Oh','Woo']:
                start_o=0 if start<2 else start-2
                end_o=len(viseme_list)-1 if end>=len(viseme_list)-3 else end+2
                if start>0 and viseme_list_vowel[start-1] not in ['PBM1','PBM2']:
                    viseme_list[start_o:start]=[viseme_list_vowel[k]]*2
                if end+1<len(viseme_list) and viseme_list_vowel[end+1] not in ['PBM']:
                    viseme_list[end+1:end_o+1]=[viseme_list_vowel[k]]*2
                    end+=2
                #자음 예외 2, 원순성 모음 + 양순음
            elif viseme_list_vowel[k] =='PBM':
                if (start>0 and viseme_list_vowel[start-1] in ['Oh','Woo']) or(end+1<len(viseme_list) and viseme_list_vowel[end+1] in ['Oh','Woo']):
                    viseme_list[start:end+1]=['PBM2']*(end-start+1)
                else:
                    viseme_list[start:end+1]=['PBM1']*(end-start+1)
            k=end+1
        return viseme_list,amplitude_list

    def viseme_to_pose(self,viseme_list):
        viseme_list_pose=[]
        for k  in range( len(viseme_list)):
            if viseme_list[k] in phoneme_to_pose_dict:
                viseme_list_pose.extend(phoneme_to_pose_dict[viseme_list[k]])
            else:
                viseme_list_pose.append(viseme_list[k])
                print(k,viseme_list[k])
        return viseme_list_pose
    
    def forward(self,audio,SR=9600):
        self.SAMPLE_RATE = SR
        wav_length=len(audio)/SR

        active_phoneme_list = self.get_active_phoneme(audio,SR)
        phoneme_len=wav_length/len(active_phoneme_list)
        self.phoneme_len = phoneme_len  
        self.chunk= round(phoneme_len * SR)

        amplitude_list,amp= self.get_amplitude(audio,len(active_phoneme_list))
        viseme_list,amplitude_list=self.phonme_to_viseme(active_phoneme_list,amplitude_list)
        pose_list=self.viseme_to_pose(viseme_list)

        """print("##active_phoneme_list : " ,len(active_phoneme_list),active_phoneme_list)

        print("##amplitude_list : " ,len(amp),len(amplitude_list),amplitude_list)
        print("##viseme_list : " ,len(viseme_list),viseme_list)
        #rint("##pose_list : " ,len(pose_list),pose_list)"""
   

  
        return pose_list, amplitude_list, active_phoneme_list, viseme_list,amp
    
