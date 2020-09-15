export REPO=$GITHUB_REPOSITORY
export VUE_APP_BASE_URL=$INPUT_ENDPOINT
cp form.yml /form.yml
python3 /script.py
cd /app
npm run build
cp -r /app/dist $GITHUB_WORKSPACE/dist