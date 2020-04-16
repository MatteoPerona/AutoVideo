import os
import random
from time import sleep
'''
file concatenator using ffmpeg
->built specifically to concatenate TikToks
'''
                
def sleeper(condition_file, directory, retries=0):#Sleeps Until specified file in specified directory is found
    if os.path.isfile(directory+condition_file):
        return True
    else:
        print(retries)
        sleep(5)
        sleeper(condition_file, directory, retries+1)
        

def resize(i, ffmpeg_location, directory, width=560, height=1024, reconcatDir='', o_cond=''):#returns ffmpeg command that resizes video files without changinf aspect ratio, height and width automatically set to 560x1024
    o = o_cond+'out'+i[3:len(i)]
    command = f'{ffmpeg_location} -i {directory}{i} -vf "scale=w={width}:h={height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1:1" {reconcatDir}{o}'
    return command


def resizeAll(directory='./Concat', file_type='.mp4', ffmpeg_location='./ffmpeg', waste_dir='./PythonWaste', reconcatDir='./ReConcReady', o_cond='food'):
    #resizes all the files
    outsNum=0
    for r,d,f in os.walk(directory):
        for file in f:
            if file_type in file:
                command = resize(file, ffmpeg_location, directory, reconcatDir=reconcatDir, o_cond=o_cond)
                os.popen(command)
                outsNum+=1
    
    sleeper(f'{o_cond}out{str(outsNum)}.mp4', directory=reconcatDir)#makes the function wait until all files are resized
    
    for r,d,f in os.walk(directory):#writes all new file paths to a text file
        for file in f:
            if file_type and 'old' in file:
                os.rename(directory+file, waste_dir+file)

    
def concatenate(file_name='output.mp4', directory='./ReConcReady', file_type='.mp4', ffmpeg='./ffmpeg', outDir='./Outputs'):#concat process
    #initializing vars
    inputList = []
    inputStr = ''
    filterStr = '"'
    
    n=0
    for r,d,f in os.walk(directory):#adding inputs and filters to respective list and string
        for file in f:
            if file_type in file:
                inputList.append(f' -i {directory}{file}')
                filterStr += f'[{n}:v:0][{n}:a:0]'
                n+=1
    #print(len(inputList))
    
    random.shuffle(inputList)#shuffling list for random input order and generating input string for command
    for i in inputList:
        inputStr+=i
        
    filterStr += f'concat=n={n}:v=1:a=1[outv][outa]"'#adding start and end clause to the filter string
    
    concatCommand = f'{ffmpeg}{inputStr} -filter_complex {filterStr} -map "[outv]" -map "[outa]" {outDir}{file_name}'#generates full ffmpeg command
    #print(concatCommand)
    os.system(concatCommand)#runs command