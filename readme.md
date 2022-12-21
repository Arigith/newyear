## Frontend

```shell
cd frontend
npm install
npm install --save-dev @astrojs/react react react-dom
npm run dev
```

## Backend

```shell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Project Structure

The frontend data lives in `\frontend\`, while the backend data lives in `\backend\`.

### Frontend
Astro looks in the `pages` directory for any `.md` or `.astro` files and loads the components inside them. Astro can use React or other UI component libraries (Vue, Svelte, etc). 

Components are loaded from the `components/` directory. The React ones have a `.jsx` extension. Astro renders one-off by default, so you need to add `client:load="react"` for your components to work properly with dynamic data wherever you use them.

To make one page link to another just add an `<a href="/my_new_link>Click me</a>` to wherever you want.

### Backend
This is holding the actual api information.
The `database` page is where, after the command is given, that the system will check and create a database if one does not exist.
The `models` page is the page where the system will create the `table structure` of the database.
The `schemas` page is where we can limit what is shown from the `models` page. for example if we created a `get_model` query you can show the phone make and phone model only while the database can hold the unique_id, phone_make, phone_model and Price.
The `main` page is where the queries live. we can add, update, remove and get anything from our database in this page.

## FAQ

The `worklog.txt` file hold my basic worklog on the day I did it. At the start I was doing 4 hours on the project and 4 hours study.