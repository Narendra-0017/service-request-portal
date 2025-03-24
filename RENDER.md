# Deploying Service Portal on Render

Follow these steps to deploy the Service Portal application on Render:

## 1. Create a New Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Select the repository containing the Service Portal code

## 2. Configure the Web Service

- **Name**: Service-Portal (or your preferred name)
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free (or select paid plan as needed)

## 3. Environment Variables

Add the following environment variables:
- `SECRET_KEY`: A secure random string for your app's security
- `PORT`: 10000 (this is handled by the code, but you can set it explicitly)

## 4. Database Setup (Optional)

If you want to use a persistent database:
1. Create a PostgreSQL database on Render
2. Render will automatically provide the DATABASE_URL environment variable
3. Our app is configured to use this if available

## 5. Deploy

Click "Create Web Service" and wait for deployment to complete.

## 6. Verify

Once deployment is complete, visit your Render URL to verify the application is working correctly.

## Troubleshooting

If you encounter issues:
1. Check Render logs for errors
2. Verify environment variables are set correctly
3. Ensure all dependencies are listed in requirements.txt
4. Contact Render support if needed

Good luck with your deployment! 