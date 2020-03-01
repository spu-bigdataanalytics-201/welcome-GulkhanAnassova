# Welcome :grey_exclamation:

![Big Data](readme-contents/large-data-keyboard-computer.jpg)

You made it! This is our start of a journey for the next few months! 

In this introductory repository, you will be guided to the concepts and ways of how we will be doing the class, assignments, and participations. Each section in below will tell you about itself.

## How to Prepare to the First Class

Things you will need to prepare before the first class is the things you will be using during the course of this class. Following is the stuff you need to be prepared for.

1. Python
2. Git
3. SQL
4. Integrated Development Editor (IDE)

Going over to the list above won't take more than a few hours of your time. 

### Python

In this course, we use Python. You can use either [standard python](https://www.python.org/), or [anaconda distribution](https://www.anaconda.com/distribution/), up to your preference.

It is better to know Python syntax and learn some few stuff and sharpen your existing skills of Python ahead of the assignments. For that, you can use the following stuff.

- Learn the syntax, [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- Online Tool to Learn Python, [learnpython.org](https://www.learnpython.org/)
- A rather broader place to learn Python, [Geek for Geeks](https://www.geeksforgeeks.org/python-programming-language/)

### Git 

The assignments are stored and shared using [GitHub](https://github.com/) and we use [Git](https://git-scm.com/) to be able to version and interact with our repositories.

My recommendation is go over the following stuff.

- Your first steps towards Git, [Learn to use Git](https://guides.github.com/activities/hello-world/)
- Useful to understand how Git works, [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- Useful to understand how GitHub works, [Github Flow](https://enterprise.github.com/downloads/en/-github-flow-cheatsheet.pdf)
- Useful for your README.md files, [Github Flawored Markdown Cheat Sheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)

### SQL

SQL is the heartbeat of your Analytical life! You need to know it to some extend! Following are some links to check out.

- Learn the syntax, [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- Interactive Online SQL Learning Tool, [SQLBolt](https://sqlbolt.com/)
- Free class on SQL, [CodeAcademy SQL](https://www.codecademy.com/learn/learn-sql)

### IDE

My favorite, bittersweet tool, [Visual Studio Code](https://code.visualstudio.com/), use it and you'll love it!

There are alternatives of course, you are welcome to use those as well. The point is an IDE will make your life much easier if you choose to use one!

Alternatives

- [Atom](https://atom.io/)
- [Sublime](https://www.sublimetext.com/)
- [Notepad++](https://notepad-plus-plus.org/) (I use it as an advanced Notepad, rather than an IDE) 
- And many, many more over [here](https://www.google.com/search?q=integrated+development+editor).

## Class Tools!

Following are some of the tools you can utilize for doing the assignments on this course.

Tool | Owner | Description | How to Guide
---- | ----- | ----------- | ------------
Google Colab | Google | Colaboratory is built on top of Jupyter Notebook. | [basic_features_overview.ipynb](https://colab.research.google.com/notebooks/basic_features_overview.ipynb), [welcome.ipynb](https://colab.research.google.com/notebooks/welcome.ipynb)
Databricks Community Edition | DataBricks | Databricks is a micro-cluster as well as a cluster manager and notebook environment. | [FAQ](https://databricks.com/product/faq/community-edition), [Login to Community Edition](https://community.cloud.databricks.com/login.html)
Data Science Lab | Saint Peter's University (SPU) | SPU's computation resource is a cluster of workstations that can work together as one big systems. Be proud of it! | [Website](https://dsl.saintpeters.edu/), [How do you ...](https://dsl.saintpeters.edu/doku.php?id=how_do_i)
You computer | You! | Your local computer where you can use local tools to do your stuff. | [ssh](https://en.wikipedia.org/wiki/Secure_Shell), [Putty (for windows users)](https://www.chiark.greenend.org.uk/~sgtatham/putty/), [Jupyter Notebooks](https://jupyter.org/), [Anaconda Distribution](https://www.anaconda.com/distribution/)

<h2>Assignments</h2>

We use Github Classroom for assignments. Basically, how it works is described in down.

1. I give you a link.
2. You click on a link, and you are hacked, and I demand for a small randsom!
3. Ignore the second step, you click the link, it will automatically create a repository for you under our GitHub webpage.
4. You download this repository using `git clone https://github.com/..../welcome.git`.
5. You work on the assignment, do a few commits, and `git push` it to GitHub.
6. When you are done with the assignment, you go back to your repository, and **download** it, and upload it to the [blackboard](https://saintpeters.blackboard.com/).
7. I read it after the deadline passes, and give you a big 0.
8. Ignore the 7th step, you will be graded.

## Final Project

Your final project will be about a data science task, and the goal is to be able to analyze a large dataset using [Apache Spark](https://spark.apache.org/).

The task is an open discussion, and **you are required to participate** in this discussion!

At the end of this course, we will replace this line with the task we come up for our final project!

## Grading

Grading will be based on syllabus. We will have assignments, midterm, and final project.

The letter grade of your final grade will be calculated using the following function. You can test this code by starting python from this folder's place.

``` py
from grader import calculate_letter_grade

# this can be you!
grade = calculate_letter_grade(
    assignments=[100, 100, 100, 90, 60, 100],
    final_project=100,
    midterm=90,
    return_grade=True
)

# gets A (97)
print(grade)
```

## Your To-Do List for This Task

- [x] You will mark things you did in this list, like this one.
- [ ] Go over on this README file, entirely.
- [ ] Go over the links in [the things you need to prepared for](#how-to-prepare-to-the-first-class) section.
- [ ] Review the [commit history](https://github.com/spu-bigdataanalytics-201/welcome/commits/master) on this repository.
- [ ] Try the grading function in [grading](#grading) section.
- [ ] [Participate](https://github.com/spu-bigdataanalytics-201/welcome/issues/1) in final project discussion!
- [ ] Follow steps in [assignments](#assignments), and push your final changes to GitHub, to your repository. 

## Conclusion

That's it! To a wonderful semester, 

Happy coding!

By [@metinsenturk](https://github.com/metinsenturk).
