# Project name : Termux-Torrent 
 # Coded by: Khansaad1275 (You dont become a coder by just changing the credits) 
 # Github: https://github.com/khansaad1275/Termux-Torrent 
 # Date : 15/2/2022 
  
 clear 
 echo " " 
 echo " " 
 echo " " 
 echo -e "\e[032m" 
          _____                    _____                    _____                   _______               _____          
         /\    \                  /\    \                  /\    \                 /::\    \             |\    \         
        /::\    \                /::\____\                /::\    \               /::::\    \            |:\____\        
       /::::\    \              /:::/    /                \:::\    \             /::::::\    \           |::|   |        
      /::::::\    \            /:::/    /                  \:::\    \           /::::::::\    \          |::|   |        
     /:::/\:::\    \          /:::/    /                    \:::\    \         /:::/~~\:::\    \         |::|   |        
    /:::/__\:::\    \        /:::/    /                      \:::\    \       /:::/    \:::\    \        |::|   |        
    \:::\   \:::\    \      /:::/    /                       /::::\    \     /:::/    / \:::\    \       |::|   |        
  ___\:::\   \:::\    \    /:::/    /      _____    _____   /::::::\    \   /:::/____/   \:::\____\      |::|___|______  
 /\   \:::\   \:::\    \  /:::/____/      /\    \  /\    \ /:::/\:::\    \ |:::|    |     |:::|    |     /::::::::\    \ 
/::\   \:::\   \:::\____\|:::|    /      /::\____\/::\    /:::/  \:::\____\|:::|____|     |:::|    |    /::::::::::\____\
\:::\   \:::\   \::/    /|:::|____\     /:::/    /\:::\  /:::/    \::/    / \:::\    \   /:::/    /    /:::/~~~~/~~      
 \:::\   \:::\   \/____/  \:::\    \   /:::/    /  \:::\/:::/    / \/____/   \:::\    \ /:::/    /    /:::/    /         
  \:::\   \:::\    \       \:::\    \ /:::/    /    \::::::/    /             \:::\    /:::/    /    /:::/    /          
   \:::\   \:::\____\       \:::\    /:::/    /      \::::/    /               \:::\__/:::/    /    /:::/    /           
    \:::\  /:::/    /        \:::\__/:::/    /        \::/    /                 \::::::::/    /     \::/    /            
     \:::\/:::/    /          \::::::::/    /          \/____/                   \::::::/    /       \/____/             
      \::::::/    /            \::::::/    /                                      \::::/    /                            
       \::::/    /              \::::/    /                                        \::/____/                             
        \::/    /                \::/____/                                          ~~                                   
         \/____/                  ~~                                                                                     
                                                                                                                         

 echo -e "\e[032m" "   " 
 echo -e "\e[032m" "--------------------[LearnTermux.tech]-----------------------" 
 echo " " 
 # getting the latest file .torrent file 
 cd downloads 
 newf=$(ls -Art | tail -n 1) 
  
 # file info 
 echo " " 
 echo -e "\e[032m" "Downloading : ${newf}" 
 echo " " 
 echo "To Quit press ctrl + C Then Enter." 
  
  
 aria2c --seed-time=0 -d /data/data/com.termux/files/home/storage/shared/Torrent-Downloads "/data/data/com.termux/files/home/downloads/${newf}" 
  
 rm -rf /data/data/com.termux/files/home/downloads/* 
  
 # Quit Menu 
 echo " " 
 echo -e '\033[1m[Enter]Press Enter to Quit!"\033[0m' 
 echo " " 
 echo -e "\e[031m" "1. Delete all the data in Torrent-Downloads folder." 
 read bxx                                                              
  
 case $bxx in 
  
         1) echo -e "\e[031m" "Are you sure you want to Delete all the data in Torrent-Downloads folder(Y/n)" 
          
         read xconf 
  
         if [ "$xconf" != "${xconf#[Yy]}" ] ; then 
                 echo " Deleting all the data in the Torrent-Downloads folder..." 
                 cd /data/data/com.termux/files/home/storage/shared/Torrent-Downloads 
                 rm - rf * 
                 cd 
         else 
                 echo "Quiting the Menu.." 
  
         fi 
         ;; 
 esac