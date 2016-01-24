# FreeCodeCamp Django Basejump API Projects

## Setup On Cloud9

1. Click the create workspace button on the Cloud9 dashboard: 
    * Give workspace a name.
    * For the  **`Clone from Git or Mercurial URL`** part put in the repository (or fork of) https://github.com/dting/fcc-django-api-projects
    * Click **Create workspace**.

2. When the workspace is created it will ask you to login to github so it can pull down the repository.

3. Create the virtual environment:  
    ```
    $ mkvirtualenv py3 --python=/usr/bin/python3
    ```

4. Upgrade pip:  
    ```
    $ pip install -U pip
    ```
    
5. Install dependencies:  
    ```
    $ pip install -r requirements.txt
    ```
      
6. Create copy of the `.env.example` file and rename to `.env`.

7. Get a Google API key: 
    * Create a new project here: https://console.developers.google.com/home/dashboard
    * Enable the **Custom Search API** under **Other popular APIs**.
    * Click link for **Go To Credentials**.
    * Select "Web Browser (Javascript)" for "Where will you be calling the API from" dropdown.
    * Copy and paste the API Key into the `.env` for the `GOOGLE_API_KEY`.

8. Get Custom Search ID:
    * Go to https://cse.google.com
    * Click **New search engine**.
    * Type in a temporary domain for **Sites to search**, e.g. `www.example.com`.
    * Give the search a name and click **Create**.
    * Click the **Control Panel** button next to *Modify your search engine*.
    * For the **Sites to search** dropdown, select "Search the entire web but emphasize included sites".
    * Below that select the `www.example.com` domain and click the **Delete** button to remove the site.
    * Click **Update** to save the changes.
    * Next to **Details** on that same page, click the **Search engine ID** button. Copy and paste the search engine ID into the `.env` for the `GOOGLE_CX`. 

9. Run migration:  
    ```
    $ python manage.py migrate
    ```
    
10. Create super user:  
    ```
    $ python manage.py createsuperuser
    ```
    
11. Run server:  
    ```
    $ python manage.py runserver $IP:$PORT
    ```
