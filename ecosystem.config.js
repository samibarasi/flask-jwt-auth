const dotenv = require('dotenv');

dotenv.config();

module.exports = {
  apps : [{
    name: 'flask-jwt-auth',
    script: 'npm run prod:gunicorn',
    watch: true,
  }],

  deploy : {
    production : {
      user : process.env.DEPLOY_USER,
      host : process.env.DEPLOY_HOST,
      key  : process.env.DEPLOY_KEY,
      ref  : 'origin/main',
      repo : 'git@github.com:samibarasi/flask-jwt-auth.git',
      path : process.env.DEPLOY_PATH,
      'pre-deploy-local': '',
      'post-deploy' : [
        'PIPENV_VENV_IN_PROJECT=True pipenv install',
        'source .venv/bin/activate',
        'rm -rf node_modules',
        'npm install',
        'pm2 reload ecosystem.config.js --env production'
      ].join(' && '),
      'pre-setup': ''
    }
  }
};
