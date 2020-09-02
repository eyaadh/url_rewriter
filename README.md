## URL Re-writer:
A web server that re-writes URL's which at the end of the day can be used as a URL shorten-er. It uses aiohttp as the web server and mongodb to store the Data.

### Cloning and Running:
1. `git clone https://github.com/eyaadh/url_rewriter.git`, to clone the repository.
2. `cd url_rewiter`, to enter the directory.
3. `pip3 install -r requirements.txt`, to install rest of the dependencies/requirements.
6. Create a new `config.ini` using the sample available at `server/working_dir`.
7. Run with `python3.8 -m server`, stop with <kbd>CTRL</kbd>+<kbd>C</kbd>.
> It is recommended to use [virtual environments](https://docs.python-guide.org/dev/virtualenvs/) while running the app, this is a good practice you can use at any of your python projects as virtualenv creates an isolated Python environment which is specific to your project.
