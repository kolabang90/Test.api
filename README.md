# Test.api
On Your Office Computer (Upload to GitHub)
# Inside your project directory
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo-name.git
git push -u origin main

On Your Home Computer (Clone the Repository from GitHub)

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

At Home (Making Changes and Pushing to GitHub)
Go into the cloned repository, make changes, and push them to GitHub.

# Inside your cloned repo directory
git add .
git commit -m "Description of the changes you made"
git push origin main

Back at the office, pull the changes from GitHub to your office computer to update your local repository.

# Inside your project directory
git pull origin main

