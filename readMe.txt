Git APIs usage

git log
git log --all --format=%H,%P,%an,%ci --simplify-merges <file>

Example:
git log --all --format=%H,%P,%an,%ci --simplify-merges index.html

Flag meanings
--  all > search all branches 
--  format > easier format to parse
--  simplify-merges > simplify the tree (https://git-scm.com/docs/git-log)


git diff
git diff --unified=0 --minimal <old commit hash> <new commit hash> <file>

Example:
git diff --unified=0 --minimal d327fbc0f4177ee11b0cb48688014595e96d0ae5 5ed5669967d0ca72cbdb90eb7e95dfca79c30d35 index.html

Flag meanings
--  unified=0 > reduce number of context lines
--  minimal > make sure the smallest possible diff is produced


CLI synopsis (usage of our CLI)

$ gitpraise -f [<path> | "all"] -s [date] -o [output format] -sc [threshold]

Options
-f <file | directory> | "all"
Specify a file or directory to analyse or all files currently tracked by git.
example
-f js/game_manager.js
-f all

-n <num>
max commits to look back from HEAD
num is optional, default at 200

eg. -n 100
only look at latest 100 commits

--since <date>
-s <date>
Only search for commits after date
eg. -s 13-02-2020
start searching from 13th Feb 2020

-sc <threshold>
Threshold of what the user defined as a significant change
eg. -sc 0.72
Significant change is defined to be 72%. If a line was change 72% and above, the author of the new commits becomes the owner.

-o [piechart] or [annotate] or [csv] or [txt]
annotate: output to console, similar to git blame
piechart: generate a piechart of contributions by authors
output is optional (default is annotate)
eg. -o piechart

Example of full command:
gitpraise -f js/game_manager.js -s 13-02-2020 -o piechart
Do analysis on js/game_manager.js , start searching from start searching from 13th Feb 2020, output a piechart
