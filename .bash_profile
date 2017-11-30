# alias 
alias ll="ls -la -t"
alias o="open ."
alias ln="ls -l"
alias pg="ping 8.8.8.8"
alias postgres="docker run -it --rm --link postgres_node1:postgres postgres psql -h postgres -U postgres"

# path settings
export M2_HOME=/usr/local/Cellar/maven/3.5.0/libexec
export M2=$M2_HOME/bin
export PATH=$PATH:$M2_HOME/bin  
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$PATH:/usr/local/bin/python2.7
# path to the bin folder of jmeter so that we don't need to enter the entire path to run the jmeter app
export PATH=$PATH:/Users/gnc6/Downloads/apache-jmeter-3.3/bin

# color names for readibility
reset=$(tput sgr0)
bold=$(tput bold)
black=$(tput setaf 0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
blue=$(tput setaf 4)
magenta=$(tput setaf 5)
cyan=$(tput setaf 6)
white=$(tput setaf 7)
user_color=$green
[ "$UID" -eq 0 ] && { user_color=$red; }
PS1="\[$reset\][\[$cyan\]\A\[$reset\]]\[$user_color\]\u@\h(\l)\
\[$white\]:\[$blue\]\W\[$reset\][\[$yellow\]\$?\[$reset\]]\[$white\]\
\\$\[$reset\] "

test -e "${HOME}/.iterm2_shell_integration.bash" && source "${HOME}/.iterm2_shell_integration.bash"
