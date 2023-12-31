![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


## Bugs 
- Function wouldn't import and run properly for area1 - Called the function from within the file area_1 and used import on the choice to make it work.
- Created an infinite loop with the choice method for introduction - Added an input in the else statement to make sure to have another input before looping again. 
- Game was running start_game() twice - removed the second call 
- Game was asking for a restart every time an option was called - called the death function from inside the option.



## Credits

- References some descriptive material for the dinosaurs from [Live Science](https://www.livescience.com/24815-allosaurus.html)
- Some code taken from [Stack Overflow](https://r.search.yahoo.com/_ylt=AwrkLvnCDtBkEJkNzlB3Bwx.;_ylu=Y29sbwMEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1691385666/RO=10/RU=https%3a%2f%2fstackoverflow.com%2f/RK=2/RS=hF76jkJyIvI7mQ0w7b9zkILi5Vs-)