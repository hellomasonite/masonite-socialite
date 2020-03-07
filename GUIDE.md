# Getting credentials from providers

## Table of Contents
- [GitHub](#github)
- [Twitter](#twitter)
- [Facebook](#facebook)

## GitHub

- Login to you GitHub account and go to settings

- Click on "Developer settings"

- Click on "New GitHub App"

- Fill the "Register new GitHub App" form. Make sure to add the appropriate callback URL. If you need to add any scopes or permissions, do it.

## Twitter

- Register a new app at https://developer.twitter.com/apps

- Fill the form

![Create App](https://user-images.githubusercontent.com/11293401/75823222-a3f3c080-5da1-11ea-8534-e7174d7ccd4f.png "Create App")

> Twitter doesn’t make use of localhost. You can use a tool like [ngrok](https://ngrok.com/) in development.

- After creating the app, click on "Settings" and get the keys.

## Facebook

- Visit [https://developers.facebook.com/apps](https://developers.facebook.com/apps)

- Under "My Apps" menu, click on "Create App" button. A modal would show you what's required.

![Create App](https://user-images.githubusercontent.com/11293401/75821287-40b45f00-5d9e-11ea-84ea-f820899ff50a.png "Create App")

- You’ll be redirected to this page:

![Product page](https://user-images.githubusercontent.com/11293401/75821628-e8ca2800-5d9e-11ea-99fd-fdcd3b9c5a63.png "Product page")

- Click on Basic under the Settings tab by the left of the page

- Fill in the details of App Domains:

![App Domains](https://user-images.githubusercontent.com/11293401/75822490-575bb580-5da0-11ea-8ab1-19c93111231e.png "App Domains")

- Click on the button “Add Platform” (on the bottom of the page). Select website.

- Enter your website URL. In developement, [http://localhost:8000/](http://localhost:8000/).

- Now, you can copy your `App ID` and `App Secret`.

