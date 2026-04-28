# Twitter Clone

## Author

xxHAKRxx

## Description

A social media website that's basically Twitter but without the toxicity. A niche little site to use if you want to just hang out and chat without the toxic cesspool that you find on most popular sites. To view this website:

1. Make sure you have Git installed if you're doing this on Windows (Git comes pre-installed on Linux).
2. Clone the repo into any directory you want.
   * ```git clone github_link```
3. Go into the newly cloned repo, create a python virtual environment, then activate it.
   * ```(winpty) python -m venv .venv```
   * ```. .venv/Scripts/activate```
4. Install all of the packages found in a text file called requirements.txt.
   * ```python -m pip install -r requirements.txt```
5. Create a superuser so you can log yourself in.
   * ```(winpty) python manage.py createsuperuser```
6. Run the localhost server and log yourself in.
   * ```(winpty) python manage.py runserver```
7. You're officially in the site!

> [!IMPORTANT]
> MAKE SURE ENVIRONS AND GUNICORN ARE UPDATED TO LATEST VERSIONS. I BUILT THESE WITH OUTDATED VERSIONS WHICH WILL CAUSE ERRORS WHEN DEPLOYING. TO UPGRADE, TYPE THESE COMMANDS:
> * ```pip install --upgrade environs```
> * ```pip install --upgrade gunicorn```

## Outside Resources Used

Bootstrap for CSS styling: https://getbootstrap.com/docs/5.3/examples/sticky-footer-navbar/

jQuery for implementing like functionality: https://releases.jquery.com/

## Known Problems, Issues, And/Or Errors in the Program

None
