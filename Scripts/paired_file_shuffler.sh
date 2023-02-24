#! /bin/bash
# Author: Henry Marty
# Patch Author: John Knudson

#Program requires two inputs: Input 1 for Left Directory Input 2 for Right Directory 
#Example:  ./fileshuffle.sh /path_to_left /path_to_right
#Program requires paired data to have equal alphanumerical naming in their respective directories
#Program cannot handle nested directories 


#To create an automation use: 
####  sudo crontab -e 
#for weekly add this line
#0 0 * * 0   <path to paired_file_shuffle.sh> <path to left data> <path to right data> 
#for every 30 seconds add these two lines  
#* * * * *   <path to paired_file_shuffle.sh> <path to left data> <path to right data> 
#* * * * *   sleep 30; <path to paired_file_shuffle.sh> <path to left data> <path to right data> 

if [[ ! -d $1 ]]
then
    echo "Error: input path is not a directory"
    exit 1
fi


remake_files() {
    #create arrays for all files in the left and right directories 
    #The left/right arrays are created after sorting directories  
    local files_left=($( find "$1" -maxdepth 1 -type f | sort -V  )) 
    local files_right=($( find "$2" -maxdepth 1 -type f | sort -V )) 
    
    #local files=($( find "$0" -maxdepth 1 -type f ))

    #get size of each of the arrays
    local count_left=$(echo "${#files_left[@]}")
    local count_right=$(echo "${#files_right[@]}")


    local date_start=$(date)
    echo "date start of function is: $date_start"

    echo "files left: $count_left"
    echo "files right: $count_right"

    
   
    #check to make sure each directory is the same size
    #ASSERT: equal sized directories assumes all data is correctly paired
    if [ "$count_left" != "$count_right" ]
    then 
        echo "ERROR: Directories are not the same size - Unpaired data"
        exit 1
    fi 

    # append an 'a' to each file to avoid collision 
    # split file into name and extension to preserve extension 
    
    # for f in ${files_left[@]}
    #     do mv "$f" "${f%.*}a.${f##*.}" 
    # done

    # for f in ${files_right[@]}
    #     do mv "$f" "${f%.*}a.${f##*.}" 
    # done


    # append an 'a' to each file to avoid collision when renaming
    for f in ${files_left[@]}
        do 
            mv $f "$f""a"
    done

    for f in ${files_right[@]}
        do mv $f "$f""a"
    done


    #create an array of random numbers equaling the count of files in the left/right directories
    rand_names=( $(seq 0 $(($count_left-1)) | shuf) )
    
    #To get new born dates we need to create new files
    #create temp arrays to hold left/right data so we can use cp instead of mv 
    local temp_left=($( find "$1" -maxdepth 1 -type f | sort -V)) 
    local temp_right=($( find "$2" -maxdepth 1 -type f | sort -V)) 

    #increment through the left/right directories and update each pair with a random name
    #convert echo to log file if desired
    index=0
    while [ $index -lt $count_left ] 
    do 
        
        # echo "left file starting: ${files_left[index]}"a""
        # echo "right file starting : ${files_right[index]}"a""
        # start_time_left=$(stat -c '%w' ${files_left[index]}"a")
        # start_time_right=$(stat -c '%w' ${files_right[index]}"a")

        #copy files in temp directories back 
        cp --preserve=mode,ownership ${temp_left[index]}  $(realpath $1/"left${rand_names[index]}")
        cp --preserve=mode,ownership ${temp_right[index]}  $(realpath $2/"right${rand_names[index]}")



        # echo "shuffle time left: $start_time_left --> $(stat -c '%w' $1/"left${rand_names[index]}")"
        # echo "shuffle time right: $start_time_right --> $(stat -c '%w' $2/"right${rand_names[index]}")"

        # echo "left $index became: $1/"left${rand_names[index]}""
        # echo "right $index became: $2/"right${rand_names[index]}""

        # echo -e
         
        rm ${temp_left[index]}
        rm ${temp_right[index]} 
        index=$(( $index + 1 ))
        
    done

    # timedatectl
}

export -f remake_files


# get current time in seconds 
current_time=$(date +%s)

# generate random offset of seconds between 5 minutes and 10 days
randoffset=$(shuf -i 300-864000 -n 1)
randdate=$(($current_time - $randoffset))

timedatectl
# stop chrony service
#sudo systemctl stop chronyd


#for Debian 
sudo service cron stop 
sudo timedatectl set-ntp false

#timedatectl
# set time to time within the last 10 days and suppress output
# https://stackoverflow.com/a/32729736
: $(sudo date -s @$randdate)

timedatectl
#call remake files with initial arguments
remake_files $1 $2 

# restart chrony service to force time sync
#sudo systemctl restart chronyd

echo "randdate: $randdate"

backup_dir=$(date +'%m/%d/%Y')
echo $backup_dir
d1=$(date +'%s')
echo $d1

sudo timedatectl set-ntp true
sudo service cron start
timedatectl
# systemctl restart systemd-timesyncd


# mv "${files_left[index]}"a"" $(realpath $1/"left${rand_names[index]}")
# mv "${files_right[index]}"a"" $(realpath $2/"right${rand_names[index]}")
