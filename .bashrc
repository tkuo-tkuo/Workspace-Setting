# General (tkuo) 
alias home='cd /home/denpo60606/'
alias work='cd /work/denpo60606/'
alias c='clear'
alias h='history'
alias setBash='vim ~/.bashrc'
alias restart='source ~/.bashrc && clear'
alias stree='tree --filelimit=20'
alias ls='ls -lh'
alias gpu='nvidia-smi'

# Screen (tkuo) 
alias exp1Screen='screen -r 172241'
alias exp2Screen='screen -r 110159'
alias exp3Screen='screen -r 173444'
alias reattach='screen -raAdx'

# UGATIT (tkuo)
alias setupUGATIT='conda activate UGATIT && cd /work/denpo60606/UGATIT-pytorch/ && clear'
alias trainUGATIT='setupUGATIT && python main.py --dataset img2anime'
alias clearImages='rm *1000.png && rm *2000.png && rm *3000.png && rm *4000.png && rm *5000.png && rm *6000.png && rm *7000.png && rm *8000.png && rm *9000.png'
