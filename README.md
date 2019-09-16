# Pythodoro

A Pomodoro / productivity app for the command line. You can set what task that you're going to focus on and the program will record how much total time has been spent working on the specified task. The program will also keep track of how many pomodoros the user has completed, and will alert the user when to take a break or when a break is over.



## Usage Guide


1. in the terminal run either `python3 pomodoro_runner.py` or `python3 pomodoro_runner.py <insert-task-name-here>`.   

2. Modify the app by editting settings.json. By default a pomodoro is 25 minutes of work, followed by a 5 minute break. 

3. After every minute, the program will output or update a file called `productivity-journal` so the user can keep track of the total minutes and hours spent being productive. After every pomodoro, then program will output or update a file called `pomodoro-journal` so the user can keep track of the total number of pomodoros he or she has completed. 



I plan on making a web and a mobile version of this app, which will be completely free. I will try to implement more features, such as graph and pie charts to give a visual representation of a person's  measure If you've found this at all useful you can donate to my patreon account. 