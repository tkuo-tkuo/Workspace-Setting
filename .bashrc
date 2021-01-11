# Clear before executing any command
preexec () {
  clear
}
preexec_invoke_exec () {
    [ -n "$COMP_LINE" ] && return                     # do nothing if completing
    [ "$BASH_COMMAND" = "$PROMPT_COMMAND" ] && return # don't cause a preexec for $PROMPT_COMMAND
    local this_command=`history 1 | sed -e "s/^[ ]*[0-9]*[ ]*//g"`; # obtain the command from the history, removing the history number at the beginning
    preexec "$this_command"
}
trap 'preexec_invoke_exec' DEBUG

# Git
alias gls='git status'
alias gitGraph='git log --graph --all --oneline --decorate'
alias gitRemoteBranchListRefresh='git remote update origin --prune'

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
