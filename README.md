# Homework 3: Salaries Revisited and Turtles

In large measure, this week's homework rehashes your work with salaries in week 1.
You'll answer the same questions, but use python to do so.
Even if you are familiar with it, please do not use `pandas`.

## Salaries Revisited

### Downloading some data.

In class, we played with the city salaries file. 
You can check out these data on the excellent [Chicago Data Portal](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w).
They have some nice interactive tools for grabbing and analyzing these data.
We'll get into some of their APIs, later on.
For now, we can just curl it:

```
curl data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv -s -o salaries.csv
```

### Exercises!

You now have salaries.csv in your homework directory.
The scripts `q*py` suggests formatting for stepping through these questions.
Fill you answers in, there


So: you will modify the files in the directory, and then send it back to GitHub.  Since you've made a copy of the repository by accepting the assignment, all of your work will be separate and will not interfere with your classmates.  We will see your edited files (provided that you uploaded them on git), and you can check this too, by navigating to your own repository on your GitHub page. 

#### Questions

Hint: you've done this before.  You're answers had better match!

1. Which salaried worker makes the most?
2. How many employees does the city list?
3. How many full-time workers are there in the file?
4. How many part-time workers are there in the file?  (Check you work for 1, with 2 and 3.)
5. What is the highest hourly wage in the city?
6. Excluding the top four workers (who are doctors), what is the highest hourly wage?
7. How many people work for the police department?
8. How many of them are detectives?
9. How much does the modal fireperson (employee of the fire department) make?
10. What are the most common women's names for police officers (incl. detectives)?  (It's a tie with 35 of each.../)

## Turtles

Using turtle and taking the pictures below as your model, fill in `t*.py` to create
1. A pentagonal "tunnel"
2. A checkerboard
The angle-dependent shading is and/or rotating squares are a "bonus."

<img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/pentagonal_tunnel.png" width="185"> <img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/checkerboard.png"      width="200"> <img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/tilting_checkers.png"  width="200">



## Push to GitHub

When you're all done, commit and push the code:
```
git add *py *ps # add the relevant files
git status # check that all your modified files are listed
git commit -m "phewff, all done!"
git push
```

Now go online to your GitHub page (with substitutions!), to check that everything is there:

* https://github.com/MyGitHubName/hw-3-salaries-turtles

You should have committed fifteen files: `q01.py` to `q10.py`, `t1.py` and `t2.py`, and `checkerboard.ps` and `pentagon_tunnel.ps`.

Make sure it's in before Wednesday October 18th at 1:30am!
