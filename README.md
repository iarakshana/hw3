# Homework 3: Salaries Revisited and Turtles

In large measure, this week's homework rehashes your work with salaries in week 1.
You'll answer the same questions, but use python to do so.

Even if you are familiar with it, please do not use `pandas`.

## Salaries Revisited

### Retrieving the data.

If you need to download it again, you can download the city salaries file like so:

```
curl data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv -s -o salaries.csv
```

### Exercises!

You now have salaries.csv in your homework directory.
The scripts `q*py` suggests formatting for stepping through these questions.
Fill you answers in, there following the format exactly -- we'll check this with a computer.
All of the "salaries" questions require the same pre-formatting.
You should implement that formatting a single time with a function in `helper.py`,
  which you can import into the `q*.py` files.
The individual question files will in turn just do some list comprehension,
  and set the `solution` variable.

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

<img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/pentagonal_tunnel.png" width="200"> <img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/checkerboard.png"      width="200"> <img src="https://raw.githubusercontent.com/harris-ippp/03-salaries-turtles/master/img/tilting_checkers.png"  width="200">



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

You should have committed five files: `q01.py` to `q10.py`, `t1.py` and `t2.py`, and `checkerboard.ps` and `pentagon_tunnel.ps`.

Make sure it's in before Wednesday October 18th at 1:30am!
