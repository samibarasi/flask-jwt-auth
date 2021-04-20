module.exports = {
  apps : [{
    name: 'flask-jwt-auth',
    script: 'npm run prod:uwsgi',
    watch: true,
  }],

  deploy : {
    production : {
      user : 'ubuntu',
      host : 'ec2-3-250-85-25.eu-west-1.compute.amazonaws.com',
      key  : '~/Work/AWS/keys/Irland/tutorial.pem',
      ref  : 'origin/main',
      repo : 'git@github.com:samibarasi/flask-jwt-auth.git',
      path : '/home/ubuntu/flask-jwt-auth',
      'pre-deploy-local': '',
      'post-deploy' : 'npm install && pm2 reload ecosystem.config.js --env production',
      'pre-setup': ''
    }
  }
};
