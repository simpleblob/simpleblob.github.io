# Temporarily store uncommited changes
# git stash

# Verify correct branch
git checkout develop

# Build new files
stack build
stack exec myblog clean
stack exec myblog build

# Get previous files
git fetch --all
git checkout master

# Overwrite existing files with new files
cp -a _site/. ../

# Commit
cd ../
git add -A
git commit -m "Publish."

# Push
git push origin master

# Restoration
git checkout develop
git stash pop
# cd myblog
