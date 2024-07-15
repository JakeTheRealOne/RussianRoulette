cd $HOME/Devloper/Games/RussianRoulette
rm papers/*
echo "alive" > .dealer_status
git add .
echo "Enter the main purpose of your commit: "
read purpose
git commit -m "$purpose"
git push origin master
if [ $? ]; then
    $HOME/.config/eww/spec/waiting_notification.sh &
    action=$(notify-send -a " repo: 2048" "the config has been saved on GitHub" -A "default=open link")
    if [[ $action == "default" ]]; then
        firefox --new-tab "https://github.com/JakeTheRealOne" &
    fi
else
    notify-send -a " repo: Russian Roulette" "an error occured while saving on GitHub"
fi
